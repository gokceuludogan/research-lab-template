## Lab Website Template

This website is designed to be maintenance-free. You do not need to know HTML, CSS, or React.

### How to Edit

1. Updating Team, News, or Publications

Open the file data/lab_data.json.

This is a structured text file. Add new entries following the pattern.

For a new paper: Copy an existing block in publications, paste it, and change the text.

For a new member: Add them to the team section.

Save the file.

2. Updating Research Page

Open content/research.md.

This is a Markdown file. You can write normally.

Use # for headers.

Use *text* for italics.

Use - for bullet points.

3. Adding a New Page (e.g., Teaching)

Create a new file in the content/ folder, e.g., teaching.md.

Write your content.

(Optional) Ask the admin to add a link to the navigation bar in templates/layout.html.

### How it Works (Automated)

Every time you commit a change to GitHub, a "Workflow" runs automatically. It:

Reads your JSON data.

Reads your Markdown text.

Combines them into a modern HTML website.

Publishes it to the internet.

You don't need to run anything on your own computer.



