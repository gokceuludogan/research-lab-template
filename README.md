# Academic Research Lab Website Template

A streamlined, maintenance-free website template designed for academic research labs. This template allows you to manage team members, publications, and news without writing code.


##  Getting Started (Setup)

Follow these steps to create your own version of this lab website.

### 1. Fork the Repository
1. Look at the top-right corner of this page.
2. Click the **Fork** button.
3. Select **"Create a new fork"**.
4. Choose the repository owner (your personal account or your lab's organization).
5. Click **Create fork**.

### 2. Enable GitHub Actions
*Note: Sometimes GitHub disables automation on forked repositories for security.*
1. Go to the **Actions** tab in your new repository.
2. If you see a button that says **"I understand my workflows, go ahead and enable them"**, click it.

### 3. Configure GitHub Pages
1. Go to **Settings** (top navigation bar of the repo).
2. On the left sidebar, click **Pages**.
3. Under **Build and deployment** > **Source**, ensure "Deploy from a branch" is selected.
4. Under **Branch**, select `gh-pages` and save.
   * *Note: If you do not see `gh-pages` yet, you may need to make your first edit (see below) to trigger the workflow. Wait 2-3 minutes, then come back here.*

---

## How to Edit

### 1. Updating Team, News, or Publications
All dynamic data is stored in a simple text file.

1.  Open the file `data/lab_data.json`.
2.  Click the **Pencil Icon** (Edit file) in the top right.
3.  Add new entries following the existing pattern.
    * **For a new paper:** Copy an existing block in the `publications` list, paste it, and change the text.
    * **For a new member:** Add them to the `team` section.
    * **Missing Fields:** If a field is not relevant (e.g., `selected_projects`), simply delete that line or leave it out. The website will automatically hide that section.
4.  Scroll down and click **Commit changes**.

### 2. Updating Research Page
The content pages use Markdown, which is easy to write.

1.  Open `content/research.md`.
2.  You can write normally.
    * Use `#` for main headers.
    * Use `##` for sub-headers.
    * Use `*text*` for italics.
    * Use `-` for bullet points.

### 3. Adding a New Page (e.g., Teaching)
1.  Create a new file in the `content/` folder (e.g., `teaching.md`).
2.  Write your content using Markdown.
3.  *(Optional)* To make this page appear in the navigation bar, you may need to edit `templates/layout.html` to add the link, or ask the admin to do so.

## How it Works (Automated)

This website uses an automated "Continuous Deployment" approach. You do not need to run anything on your own computer.

**The Process:**
1.  Every time you **Commit** a change to a file on GitHub, a **Workflow** starts automatically.
2.  It reads your JSON data (`data/lab_data.json`).
3.  It reads your Markdown text (`content/`).
4.  It combines them into a modern HTML website.
5.  It publishes the result to the internet via GitHub Pages.

**Checking Status:**
You can see the progress of your update by clicking the **Actions** tab. A green checkmark means your site has been updated successfully.
