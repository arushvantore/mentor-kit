# uh4th8cl61s2  [eq7lnkj6lo7s]
URL: https://my.newtonschool.co/course/eq7lnkj6lo7s/lecture/uh4th8cl61s2?lectureTab=assignment
Captured: 2026-11-06T04:32:39 by lecture harvester (read-only).

---

=== Assignments tab (quiz cards + in-class + post-class sections) ===
Assignments1
In-class Quizzes
5
Lecture Notes
QUIZ
CLI File & Directory Management, CLI Package Management, CLI Flags, Options & Op ... - Revision
Attempt duration - Sep 10th 2026 6:05 pm to Sep 15th 2026 6:05 pm
Attempted on Sep 12th 2026 12:50 am
View Solutions
In class assignments
This section contains the assignments and questions solved in the class
No in-class assignments for this lecture
Post class assignments
This section contains the assignments related to the topics covered in this lecture
Q1. Advanced File Managementmedium

You are helping your team clean up and organize project files. 

Steps to follow:

Create a folder called project-files.

Inside it, create three files:

report.docx

summary.docx

draft.docx

Make a copy of report.docx and name it report_backup.docx.

Create a new folder called old. Move draft.docx into old/.

Rename summary.docx to final_summary.docx.

Copy final_summary.docx into the old/ folder as well.

Delete report_backup.docx.

Final structure should look like this:

project-files/
├── report.docx
├── final_summary.docx
└── old/
    ├── draft.docx
    └── final_summary.docx

Read More
Your Solution
Q2. Create a Project Folder Structuremedium

You have recently joined a backend team that develops services for an e-commerce platform.

To ensure consistency across projects, the team uses an internal command called create-service to generate the standard structure for new API services.

During the onboarding of several new developers, the team noticed that newly generated services are missing important files and some directories are named incorrectly.

The engineering manager asks you to investigate and repair the scaffold generator before the next batch of services is created.

Tasks:
Locate the create-service command.
Inspect the script used by the command.
Fix all issues in the script.
Ensure the command can be executed.
Run the command to generate a new service.

Expected Service Structure:
service/
├── controllers/
├── models/
├── routes/
├── middleware/
├── server.js
└── README.md


Expected README Content:
API Service


Expected server.js Content:
console.log("Server started");


Requirements:
Directory names must exactly match the expected structure.
The middleware directory must be present.
README.md must exist inside the service directory.
server.js must exist inside the service directory.
The contents of README.md must exactly match the expected text.
The contents of server.js must exactly match the expected text.
The command should execute successfully after your fixes.
Read More
Your Solution
Q3. Recover the Emergency Access Tokenmedium

You are assisting the Site Reliability Engineering (SRE) team during a production incident.

An emergency access token is required to restore a critical service. The token was intentionally stored somewhere inside a deeply nested backup directory structure for security reasons.

The backup system has created many nested folders containing many files. Most of these files are not readable due to permission restrictions.

The SRE team remembers only one thing:

The emergency token is stored in the only readable text file within the backup directory tree.

Your task is to locate the readable file, inspect its contents, and recover the token.

Tasks:
Explore the directory structure.
Find the readable file inside the backup directory tree.
Create a file named token.txt in the current directory containing only the token value.

Example Token Format:
ACCESS_TOKEN_VALUE=abc123xyz789


Expected Output File:
abc123xyz789


Requirements:
Do not modify any existing files.
token.txt must contain only the token value.
No additional text or whitespace should be present.
Read More
Your Solution
Q4. Locate and Extract the Recovery Keymedium

A production server experienced a critical failure overnight. Before shutting down, the backup system created multiple backup folders and scattered diagnostic files across them.

Your team needs to restore access, but the recovery key was saved in only one backup file. The file name and location are unknown.

Search through the backup directory tree, find the recovery key, and save only the key value (without RECOVERY_KEY=) into a file named key.txt in the current directory.

Task:
Locate the recovery key hidden somewhere inside the backups directory.
Extract only the recovery key value.
Save the key value into a file named key.txt in the current directory.

For example, if a file contains:

RECOVERY_KEY=7fK92mXqL8pR3vNz

then key.txt should contain:

7fK92mXqL8pR3vNz

The recovery key may be located in any file within the backups directory tree.

Read More
Your Solution

=== In-class Quizzes tab ===
In-class Quizzes
5
Lecture Notes
In-class Quizzes
These in-class quizzes are only for learning purposes and are not meant for evaluation.
Classroom Quiz - CLI File & Directory Management, CLI Package Management, CLI Flags, Options & Op ...
attempted
Total Questions
1 Questions
Your Score
2/2
Classroom Quiz - CLI File & Directory Management, CLI Package Management, CLI Flags, Options & Op ...
attempted
Classroom Quiz - CLI File & Directory Management, CLI Package Management, CLI Flags, Options & Op ...
attempted
Classroom Quiz - CLI File & Directory Management, CLI Package Management, CLI Flags, Options & Op ...
attempted
Classroom Quiz - CLI File & Directory Management, CLI Package Management, CLI Flags, Options & Op ...
attempted
Classroom Quiz - CLI File & Directory Management, CLI Package Management, CLI Flags, Options & Op ...
Revise
QUESTION 1/1
Your friend runs this command:
cowsay -f dragon "Deploy successful"
What does -f do here?
A
Creates a file template
Modifies the command behaviour
Explanation:-f is a command-line flag that modifies how cowsay behaves. Specifically, it tells cowsay to use the dragon character template instead of the default cow when displaying the message.
C
Deletes the dragon template
D
Finds the output message
CORRECT ANSWER

Newton School
