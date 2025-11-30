import json
import os
import markdown
from jinja2 import Environment, FileSystemLoader

# Configuration
CONTENT_DIR = 'content'
DATA_DIR = 'data'
OUTPUT_DIR = 'docs' 
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
nav_items = []
for page_name, is_enabled in nav_config.items():
    if is_enabled:
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
for filename in os.listdir(CONTENT_DIR):
    if filename.endswith('.md'):
        file_path = os.path.join(CONTENT_DIR, filename)
        
        with open(file_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
            
        html_content = markdown.markdown(md_content)
        
        # Determine basic file info
        base_name = os.path.splitext(filename)[0] # e.g., 'research'
        
        # Logic to identify Home vs Other pages
        if base_name.lower() in ['home', 'index']:
            output_filename = 'index.html'
            is_home = True
            page_title = "Home"
            active_page = "Home"
        else:
            output_filename = f"{base_name.lower()}.html"
            is_home = False
            # Capitalize first letter for title (e.g., "teaching" -> "Teaching")
            page_title = base_name.capitalize() 
            active_page = page_title

        # Render the template
        # NOTICE: We pass 'data=lab_data' because the HTML uses {{ data.lab_name }}
        output_html = template.render(
            content=html_content,
            nav_items=nav_items,
            data=lab_data,       
            is_home=is_home,
            page_title=page_title,
            active_page=active_page
        )
        
        with open(os.path.join(OUTPUT_DIR, output_filename), 'w', encoding='utf-8') as f:
            f.write(output_html)
            
print(f"Site generated successfully. Processed {len(os.listdir(CONTENT_DIR))} pages.")
