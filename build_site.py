import os
import json
import markdown
from jinja2 import Environment, FileSystemLoader
from datetime import datetime

# Configuration
CONTENT_DIR = 'content'
OUTPUT_DIR = 'public'
TEMPLATE_DIR = 'templates'
DATA_FILE = 'data/lab_data.json'

def load_data():
    """Loads the structured lab data (Team, Pubs) from JSON."""
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def build():
    # 1. Setup Environment
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template('layout.html')
    
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # 2. Load Global Data (The "Database")
    site_data = load_data()
    
    # 3. Process Markdown Content Pages
    # We look for simple markdown files in /content to turn into pages
    md = markdown.Markdown(extensions=['meta', 'fenced_code'])
    
    pages = []
    
    # Ensure content dir exists for the demo
    if not os.path.exists(CONTENT_DIR):
        os.makedirs(CONTENT_DIR)
        with open(os.path.join(CONTENT_DIR, 'research.md'), 'w') as f:
            f.write("# Research Focus\n\nWe study **protein folding** and *dynamic systems*.\n\n## Current Projects\n1. AlphaFold Analysis\n2. Wet Lab Synthesis")

    for filename in os.listdir(CONTENT_DIR):
        if filename.endswith('.md'):
            name = filename[:-3] # remove .md
            with open(os.path.join(CONTENT_DIR, filename), 'r', encoding='utf-8') as f:
                text = f.read()
                html_content = md.convert(text)
                
                # Create a page object
                page_info = {
                    'slug': name,
                    'title': name.capitalize(),
                    'content': html_content,
                    'is_active': name
                }
                pages.append(page_info)

    # 4. Render Pages
    
    # Render Home (Special case, uses data directly)
    home_html = template.render(
        page_title="Home",
        active_page="home",
        data=site_data,
        content=None,
        is_home=True
    )
    with open(os.path.join(OUTPUT_DIR, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(home_html)
        
    # Render Markdown Pages (Research, Contact, etc.)
    for page in pages:
        html = template.render(
            page_title=page['title'],
            active_page=page['slug'],
            data=site_data,
            content=page['content'],
            is_home=False
        )
        with open(os.path.join(OUTPUT_DIR, f"{page['slug']}.html"), 'w', encoding='utf-8') as f:
            f.write(html)

    print(f"✅ Website built successfully in '{OUTPUT_DIR}' directory.")

if __name__ == "__main__":
    # Create dummy data if it doesn't exist for the user to start
    if not os.path.exists('data'):
        os.makedirs('data')
    
    if not os.path.exists('templates'):
        os.makedirs('templates')

    build()
