import json
import os
import markdown
from jinja2 import Environment, FileSystemLoader

# Configuration
CONTENT_DIR = 'content'
DATA_DIR = 'data'
OUTPUT_DIR = 'docs' # GitHub Pages usually serves from 'docs' or root
TEMPLATE_DIR = 'templates'

# Ensure output directory exists
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# 1. Load Data
def load_json(filename):
    path = os.path.join(DATA_DIR, filename)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

lab_data = load_json('lab_data.json')
nav_config = load_json('navigation.json')

# 2. Build Navigation Menu List
# We convert the simple {"Page": true} json into a list of links for the template
nav_items = []

for page_name, is_enabled in nav_config.items():
    if is_enabled:
        # Special case for Home to map to index.html
        if page_name.lower() == "home":
            link = "index.html"
        else:
            link = f"{page_name.lower()}.html"
        
        nav_items.append({
            "name": page_name,
            "link": link
        })

# 3. Setup Jinja2 Environment
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
template = env.get_template('layout.html')

# 4. Generate Pages
# We iterate through the content files to generate the HTML
for filename in os.listdir(CONTENT_DIR):
    if filename.endswith('.md'):
        file_path = os.path.join(CONTENT_DIR, filename)
        
        with open(file_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
            
        # Convert Markdown to HTML
        html_content = markdown.markdown(md_content)
        
        # Determine output filename
        # If the md file is "home.md" or "index.md", save as "index.html"
        base_name = os.path.splitext(filename)[0].lower()
        if base_name in ['home', 'index']:
            output_filename = 'index.html'
        else:
            output_filename = f"{base_name}.html"

        # Render the template with all data
        output_html = template.render(
            content=html_content,
            nav_items=nav_items,  # Pass the dynamic menu
            **lab_data            # Pass team/news/publications data
        )
        
        # Write to file
        with open(os.path.join(OUTPUT_DIR, output_filename), 'w', encoding='utf-8') as f:
            f.write(output_html)
            
print(f"Site generated successfully with {len(nav_items)} menu items.")
