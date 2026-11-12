# kkx7ibjp1ztf  [eq7lnkj6lo7s]
URL: https://my.newtonschool.co/course/eq7lnkj6lo7s/lecture/kkx7ibjp1ztf?lectureTab=assignment
Captured: 2026-11-06T04:32:52 by lecture harvester (read-only).

---

=== Assignments tab (quiz cards + in-class + post-class sections) ===
Assignments1
Lecture Notes
QUIZ
Operating System, Filesystem Management, File Ownership and Permissions, PATH, O ... - Revision
Attempt duration - Sep 22nd 2026 4:00 pm to Sep 27th 2026 4:00 pm
Your submission was marked as “LATE SUBMISSION” because you have submitted after the deadline
View Solutions
In class assignments
This section contains the assignments and questions solved in the class
No in-class assignments for this lecture
Post class assignments
This section contains the assignments related to the topics covered in this lecture
Q1. Audit Trail Setupeasy

You are given the following folder structure inside the current directory.

audit_trail/
└── access.log

Perform the following operations:

Change the permissions of the audit_trail/ directory so that the owner has full access (read, write, execute), the group has read and execute only, and others have no access at all.
Inside audit_trail/, create a new file named summary.txt containing the exact text Audit Summary Generated.
Set the permissions of summary.txt so that the owner can read and write, the group can only read, and others have no access.
Read More
Your Solution
Q2. Three Levels of Accesseasy

After a security review, three files in the clearance directory were found with wide-open permissions. Each file must be tightened to a different clearance level using numeric chmod.

Given Directory Structure:

clearance/
├── public.txt     
├── team.txt      
└── private.txt   

Current Permissions:

All three files: full permissions for everyone.

Tasks to Complete:

public.txt: owner can read and write; group and others can only read.
team.txt: owner can read and write; group can only read; others get nothing.
private.txt: owner can read and write; group and others get nothing.
Do not modify the content of any file.
Read More
Your Solution
Q3. Deployment Project Permissionsmedium

You are preparing a shared deployment project where different roles (developers, CI system, general viewers) need different levels of access to different parts of the codebase. You need to set the correct permissions on each part of the project so it is accessed only as intended.

Given Directory Structure:

deployment/
├── app/
│   ├── server.py
│   ├── handler.py
│   └── settings.py
├── datasets/
│   ├── train.csv
│   └── test.csv
├── docs/
│   └── OVERVIEW.md
└── bin/
    ├── start.sh
    ├── stop.sh
    └── healthcheck.sh

All files currently have default permissions (644 for files, 755 for directories). Apply the following rules:

Python source files (every .py file inside deployment/app/):
Owner: read, write, execute
Group: no access
Others: no access
The datasets/ directory, and every file inside it:
Owner: read, write, execute
Group: read, write, execute
Others: no access
docs/OVERVIEW.md:
Owner: read, write
Group: read only
Others: read only
Every shell script (every .sh file inside deployment/bin/):
Owner: read, write, execute
Group: read, execute (no write)
Others: read, execute (no write)

Deliverable: Write the chmod command(s) you would run, one rule at a time, to reach the end state described above. You may use wildcards (e.g. *.py) instead of listing files individually.

Note: Run your commands from outside the deployment/ directory (i.e. paths should start with deployment/..., not be run from inside it).

Read More
Your Solution
Q4. Purge the Locked Workspacemedium

A corrupted draft is stuck inside a locked workspace. The draft itself is read-only, and the workspace directory has no write permission. Deleting a file requires write permission on the directory, not on the file. Delete the corrupted draft, create a clean replacement, and lock the workspace again.

Given Directory Structure:

workspace/     (Write access removed)
├── old_draft.txt   (Read-only, corrupted)
└── notes.txt

Current Permissions:

workspace/ directory: Write permission removed (chmod 555).
old_draft.txt: Read-only for everyone (chmod 444).

Tasks to Complete:

Delete workspace/old_draft.txt.
Create a new file workspace/final_draft.txt containing exactly Clean copy.
Using chmod, set the permissions of final_draft.txt to read and write for user, read for group and no permissions for others.
notes.txt must remain untouched.
Restore workspace/ permissions to read and execute for user, group and others.
Read More
Your Solution
Q5. Data Breach Responsehard

You have been tasked with handling Data Breach Response, a secure directory of evidence and reports from an active security incident. Some files and directories currently have restricted permissions that you must work around without permanently weakening security.

Given Directory Structure:

breach_response/
├── evidence/
│   └── log_dump.txt
├── secure/
├── reports/
│   └── incident_summary.txt
└── classified.txt


Pre-existing Permissions:

evidence/ directory — write permission removed (chmod 555)
log_dump.txt — read-only (chmod 444)
incident_summary.txt — read-only (chmod 444)
classified.txt — no permissions (chmod 000)

Actions to Perform:

Copy a file into breach_response/:
Copy evidence/log_dump.txt to breach_response/log_dump.txt.
Move the restricted directory:
Move the entire evidence/ directory into secure/, resulting in secure/evidence/.
evidence/ currently has no write permission (555). Since moving a directory into a new parent requires updating its own metadata, you'll need to temporarily add write permission to evidence/ before moving it.
After the move, restore secure/evidence/ to permission 555.
Edit the read-only report:
Append the exact line Breach confirmed to reports/incident_summary.txt.
incident_summary.txt currently has no write permission (444), so you'll need to temporarily adjust permissions to edit it.
Restore the file permissions to 444 afterward.
Create a new report:
Create secure/forensics_report.txt containing the exact text Forensics Complete.
Set its permissions to 600.
Append to the report again:
Append the exact line Escalated to security team to reports/incident_summary.txt.
As before, temporarily adjust permissions to write, then restore incident_summary.txt to 444 afterward.

Important: Do not modify classified.txt. It must remain unchanged with permission 000.

Read More
Complete Now
