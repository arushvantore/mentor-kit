"""Build shareable deliverables from export/<name>-questions.md:
HTML (printable) + PDF.  Usage:
    .venv/bin/python export_html_pdf.py export/PSP-questions.md
Outputs <same-base>.html and <same-base>.pdf next to the input."""
import html
import pathlib
import re
import sys

import scrape as S


def build(md_path):
    md_path = pathlib.Path(md_path)
    md = md_path.read_text(encoding="utf-8")
    out, in_pre, in_ul, h1_seen = [], False, False, False

    def inline(t):
        t = html.escape(t)
        t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
        t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
        t = re.sub(r"(https?://[^\s<]+)", r'<a href="\1">\1</a>', t)
        return t

    for line in md.split("\n"):
        if line.strip().startswith("```"):
            if in_ul:
                out.append("</ul>")
                in_ul = False
            out.append("<pre>" if not in_pre else "</pre>")
            in_pre = not in_pre
            continue
        if in_pre:
            out.append(html.escape(line) + "\n")
            continue
        m = re.match(r"^(#{1,3})\s+(.*)$", line)
        if m:
            if in_ul:
                out.append("</ul>")
                in_ul = False
            lvl, text = len(m.group(1)), m.group(2)
            if lvl == 1:
                if h1_seen:
                    out.append("<hr>")
                h1_seen = True
                out.append("<h1 class='doc-title'>" + inline(text) + "</h1>")
            elif lvl == 2:
                out.append("<section><h2>" + inline(text) + "</h2>")
            else:
                out.append("<h3>" + inline(text) + "</h3>")
            continue
        if re.match(r"^---+\s*$", line):
            if in_ul:
                out.append("</ul>")
                in_ul = False
            out.append("</section><hr>")
            continue
        if line.startswith("- "):
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append("<li>" + inline(line[2:]) + "</li>")
            continue
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if line.strip() == "":
            out.append("<p class='gap'></p>")
        else:
            out.append("<p>" + inline(line) + "</p>")
    if in_ul:
        out.append("</ul>")

    body = "\n".join(out).replace("</section>\n<hr>", "</section><hr>")
    css = """
body{font-family:-apple-system,'Helvetica Neue',Arial,sans-serif;font-size:10.5pt;
line-height:1.45;color:#16181d;margin:0;padding:26px 30px;}
h1.doc-title{font-size:20pt;margin:0 0 8px;}
h2{font-size:15pt;color:#0b3d91;margin-top:8px;border-bottom:2px solid #0b3d91;
padding-bottom:4px;page-break-after:avoid;}
h3{font-size:12pt;margin:14px 0 6px;page-break-after:avoid;}
hr{border:0;border-top:1px solid #ccc;margin:16px 0;}
ul{margin:4px 0 10px 18px;padding:0}
li{margin:3px 0;word-wrap:break-word}
p{margin:5px 0}
p.gap{margin:0;min-height:2px}
pre{background:#f4f6f8;border:1px solid #dfe3e8;border-radius:6px;
padding:9px 11px;font-size:8.8pt;white-space:pre-wrap;word-wrap:break-word;
font-family:'SF Mono',Menlo,Consolas,monospace;page-break-inside:avoid;}
code{background:#eef1f4;border-radius:3px;padding:0 3px;font-size:9.5pt;
font-family:'SF Mono',Menlo,Consolas,monospace;}
@page{size:A4;margin:14mm 12mm 16mm;}
@media print{body{font-size:9.3pt} h2{page-break-before:always}
h2:first-of-type{page-break-before:avoid} pre{font-size:7.8pt}}
"""
    htmldoc = ("<!doctype html><html><head><meta charset='utf-8'><title>"
               + md_path.stem + "</title><style>" + css
               + "</style></head><body>" + body + "</body></html>")
    html_path = md_path.with_suffix(".html")
    html_path.write_text(htmldoc, encoding="utf-8")
    print("HTML", html_path, len(htmldoc), "bytes")

    with S.sync_playwright() as pw:
        browser = pw.chromium.launch(channel="chrome", headless=True)
        page = browser.new_page()
        page.goto("file://" + str(html_path.resolve()), wait_until="load")
        page.wait_for_timeout(1200)
        pdf_path = md_path.with_suffix(".pdf")
        page.pdf(path=str(pdf_path), format="A4",
                 margin={"top": "14mm", "bottom": "16mm", "left": "12mm",
                         "right": "12mm"}, print_background=True)
        browser.close()
    print("PDF", pdf_path)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    build(sys.argv[1])
