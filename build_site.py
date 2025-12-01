import json
import os
import markdown
from jinja2 import Environment, FileSystemLoader

# Configuration
CONTENT_DIR = 'content'
DATA_DIR = 'data'
OUTPUT_DIR = 'public'
TEMPLATE_DIR = 'templates'

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

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

# 4. Generate pages from Markdown (if any)
md_files = [
    f for f in os.listdir(CONTENT_DIR)
    if os.path.isfile(os.path.join(CONTENT_DIR, f))
    and f.lower().endswith('.md')
]

print("Found markdown files:", md_files)

for filename in md_files:
    file_path = os.path.join(CONTENT_DIR, filename)

    with open(file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    html_content = markdown.markdown(md_content)

    base_name = os.path.splitext(filename)[0]
    base_lower = base_name.lower()

    if base_lower in ['home', 'index']:
        output_filename = 'index.html'
        is_home = True
        page_title = "Home"
        active_page = "Home"
        print(f"Generating HOME page from {filename} -> {output_filename}")
    else:
        output_filename = f"{base_lower}.html"
        is_home = False
        page_title = base_name.capitalize()
        active_page = page_title
        print(f"Generating page from {filename} -> {output_filename}")

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

# 5. ALWAYS build index.html even if there was no home.md / index.md
# Try to get homepage content from lab_data if available
default_home_md = lab_data.get(
    "home_markdown",
    f"# {lab_data.get('lab_name', 'Welcome')}\n\nWelcome to our lab website."
)

home_html_content = markdown.markdown(default_home_md)

index_html = template.render(
    content=home_html_content,
    nav_items=nav_items,
    data=lab_data,
    is_home=True,
    page_title="Home",
    active_page="Home"
)

with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)

print(f"Site generated successfully. Processed {len(md_files)} markdown pages.")
