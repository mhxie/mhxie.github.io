import requests
from bs4 import BeautifulSoup
import markdownify as md
from datetime import datetime, timezone
import os
import re  # For regular expressions

url = 'https://reflect.site/g/xmh/minghao-xie--home-page/c65e893dc6f546f0b0867ec0158fb8ba'

def add_bullet_points(markdown_text):
    lines = markdown_text.split('\n')
    bulleted_lines = []
    inside_publication_section = False
    publication_counter = 1

    for line in lines:
        stripped_line = line.strip()

        if stripped_line.startswith('## Publication'):
            inside_publication_section = True
            bulleted_lines.append(line)
            continue

        if stripped_line.startswith('## ') and not stripped_line.startswith('## Publication'):
            inside_publication_section = False
            publication_counter = 1

        if stripped_line:
            if inside_publication_section:
                if not stripped_line.startswith('#'):
                    bulleted_lines.append(f'{publication_counter}. {line}')
                    publication_counter += 1
                else:
                    bulleted_lines.append(line)
            else:
                if not stripped_line.startswith('#') and not stripped_line.startswith('*'):
                    if line.endswith('\n'):
                        line = line[:-1]
                    bulleted_lines.append(f'- {line}')
                else:
                    bulleted_lines.append(line)
        else:
            bulleted_lines.append(line)

    new_bulleted_lines = []
    for i, line in enumerate(bulleted_lines):
        if i == 0 or i == len(bulleted_lines) - 1:
            new_bulleted_lines.append(line)
            continue
        if line == '' and bulleted_lines[i-1][0] == '-' and bulleted_lines[i+1][0] == '-':
            continue
        new_bulleted_lines.append(line)

    return '\n'.join(new_bulleted_lines)

response = requests.get(url)
if response.status_code != 200:
    print(f'Failed to retrieve the website. Status code: {response.status_code}')
    exit(1)

soup = BeautifulSoup(response.content, 'html.parser')

# Extract data from the website to update default.html
# Find the main content div
main_content_div = soup.find('div', class_='reflect-static-editor remirror-editor ProseMirror')

# Initialize variables
location = ''
preferred_contact = ''
social_links = {}

if main_content_div:
    list_contents = main_content_div.find_all('div', class_='list-content')

    for div in list_contents:
        p = div.find('p')
        if p:
            text = p.get_text(strip=True)
            if text.startswith('Location:'):
                location = text.replace('Location:', '').strip()
            elif text.startswith('Preferred Contact:'):
                a = p.find('a')
                if a and a.text:
                    preferred_contact = a.text.strip()
                else:
                    preferred_contact = text.replace('Preferred Contact:', '').strip()
            else:
                # Extract only the specific social links (excluding GitHub)
                for a in p.find_all('a'):
                    name = a.get_text(strip=True)
                    if name in ['Google Scholar', 'LinkedIn', "Minghao's Blog"]:
                        href = a['href']
                        # Adjust the name to 'Blog' if it's 'Minghao's Blog'
                        if name == "Minghao's Blog":
                            display_name = 'Blog'
                        else:
                            display_name = name
                        social_links[display_name] = href

# Proceed with markdown conversion
markdown_content = md.markdownify(str(soup), heading_style="ATX", bullets="-")

LOCATOR = "## About Me"
start_index = markdown_content.find(LOCATOR)

if start_index != -1:
    start_index += len(LOCATOR) + 1
    markdown_content = markdown_content[start_index:]

markdown_content = add_bullet_points(markdown_content)

front_matter = "---\nlayout: default\n---\n\n"
new_content = front_matter + markdown_content

# Function to remove the last update line from the content
def remove_last_update_line(content):
    lines = content.strip().split('\n')
    if lines and lines[-1].startswith("Last update on"):
        lines = lines[:-2]  # Remove the last update line and the empty line before it
    return '\n'.join(lines)

# Check if index.md exists and compare content
file_path = "index.md"
if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        existing_content = file.read()
    existing_content_without_update = remove_last_update_line(existing_content)

    if existing_content_without_update == new_content.strip():
        print("No changes detected. Markdown file is up-to-date.")
    else:
        current_date = datetime.now(timezone.utc).strftime('%Y-%m-%d')
        new_content += f"\n\nLast update on {current_date}"
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(new_content)
        print("Markdown file has been updated successfully.")
else:
    current_date = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    new_content += f"\n\nLast update on {current_date}"
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(new_content)
    print("Markdown file has been created successfully.")

# Now update default.html
default_html_path = os.path.join('_layouts', 'default.html')
with open(default_html_path, 'r', encoding='utf-8') as file:
    default_html = file.read()

import re

# Update the Location
default_html = re.sub(
    r'<p><strong>Location:</strong>.*?</p>',
    f'<p><strong>Location:</strong> {location}</p>',
    default_html,
    flags=re.DOTALL
)

# Update the Preferred Contact
default_html = re.sub(
    r'<p><strong>Preferred Contact:</strong>.*?</p>',
    f'<p><strong>Preferred Contact:</strong> <a href="mailto:{preferred_contact}">{preferred_contact}</a></p>',
    default_html,
    flags=re.DOTALL
)

# Build the new social links HTML with adjusted display name for the blog
social_links_html = ''
for name in ['Google Scholar', 'LinkedIn', 'Blog']:
    href = social_links.get(name)
    if href:
        if name == 'Google Scholar':
            icon_class = 'fas fa-graduation-cap'
        elif name == 'LinkedIn':
            icon_class = 'fab fa-linkedin'
        elif name == 'Blog':
            icon_class = 'fa-solid fa-network-wired'
        else:
            icon_class = ''
        social_links_html += f'''
                <li style="display: inline; margin-right: 15px;">
                  <a href="{href}" target="_blank">
                    <i class="{icon_class}"></i> {name}
                  </a>
                </li>'''
    else:
        # If the link is not found, you can choose to handle it appropriately
        pass

# Replace the existing navigation links without overwriting the GitHub-related code
# First, extract the existing GitHub-related code
github_section_pattern = r'({% if site\.github\.is_project_page %}.*?{% endif %}\s*{% if site\.github\.is_user_page %}.*?{% endif %})'
github_section_match = re.search(github_section_pattern, default_html, flags=re.DOTALL)

if github_section_match:
    github_section = github_section_match.group(1)
else:
    github_section = ''

# Build the new nav section, including the GitHub-related code
new_nav_section = f'''<nav>
            <ul style="list-style: none; padding: 0;">{social_links_html}
            </ul>
          </nav>
          {github_section}'''

# Replace the existing nav section (excluding the GitHub code)
default_html = re.sub(
    r'<nav>.*?</nav>(\s*{% if site\.github\.is_project_page %}.*?{% endif %}\s*{% if site\.github\.is_user_page %}.*?{% endif %})?',
    new_nav_section,
    default_html,
    flags=re.DOTALL
)

# Write the updated content back to default.html
with open(default_html_path, 'w', encoding='utf-8') as file:
    file.write(default_html)

print("default.html has been updated successfully.")