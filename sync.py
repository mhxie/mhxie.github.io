import requests
from bs4 import BeautifulSoup, NavigableString
import markdownify as md
from datetime import datetime, timezone
import os
import re  # For regular expressions

url = 'https://reflect.site/g/xmh/minghao-xie--home-page/c65e893dc6f546f0b0867ec0158fb8ba'

def unwrap_nested_emphasis(soup_tag):
    """Unwrap nested <strong> and <em> tags, and remove empty/whitespace-only ones."""
    if not soup_tag:
        return

    # First, unwrap identical nested tags (e.g., <em><em>text</em></em> -> <em>text</em>)
    # Iterate multiple times or carefully, as unwrap changes the tree.
    # For simplicity and typical shallow nesting, one pass for direct children is often enough.
    # If deeper identical nesting is a concern, this part might need to be more robust (e.g., run multiple times).
    for tag_name in ['strong', 'em']:
        for outer_tag in soup_tag.find_all(tag_name):
            children_to_unwrap = []
            for inner_tag in outer_tag.find_all(tag_name, recursive=False):
                children_to_unwrap.append(inner_tag)
            for child in children_to_unwrap:
                if child.parent: # Ensure child is still in the tree and part of outer_tag
                    child.unwrap()

    # Second, unwrap empty or whitespace-only emphasis tags
    # Collect tags to unwrap in a list first to avoid issues with modifying the tree while iterating.
    tags_to_unwrap_empty = []
    for tag_name in ['strong', 'em']:
        for tag in soup_tag.find_all(tag_name):
            if not tag.get_text(strip=True): # If tag is empty or contains only whitespace
                tags_to_unwrap_empty.append(tag)
    
    for tag in tags_to_unwrap_empty:
        # Ensure tag still has a parent before trying to unwrap,
        # as a previous unwrap might have affected it or its parent.
        if tag.parent:
            tag.unwrap()

    # The commented-out section for potentially simplifying <strong><em>text</em></strong> to <strong>text</strong> 
    # (if em only contains text and is sole child of strong) is generally not desired
    # as it would remove intended dual emphasis. We keep it commented out.
    # for strong_tag in soup_tag.find_all('strong'):
    #     for em_tag in strong_tag.find_all('em', recursive=False):
    #         if all(isinstance(c, NavigableString) for c in em_tag.contents) and len(strong_tag.contents) == 1:
    #             pass # em_tag.unwrap()
    # for em_tag in soup_tag.find_all('em'):
    #     for strong_tag in em_tag.find_all('strong', recursive=False):
    #         if all(isinstance(c, NavigableString) for c in strong_tag.contents) and len(em_tag.contents) == 1:
    #             pass # strong_tag.unwrap()

def process_html_to_markdown(soup):
    """Convert HTML to markdown while preserving the original bullet point structure"""
    # Find the main content div
    main_content_div = soup.find('div', class_='reflect-static-editor remirror-editor ProseMirror')
    
    if not main_content_div:
        # Fallback to regular markdownify if we can't find the main content
        return md.markdownify(str(soup), heading_style="ATX", bullets="-")
    
    result_lines = []
    publication_counter = 1
    inside_publication_section = False
    last_element_type = None  # Track the type of the last element added
    
    for element in main_content_div.children:
        if hasattr(element, 'name'):
            if element.name == 'h1':
                # Skip the main title
                continue
            elif element.name == 'h2':
                heading_text = element.get_text(strip=True)
                
                # Add spacing after bullet points when transitioning to heading
                if last_element_type == 'list_item':
                    result_lines.append("")
                
                # Add spacing before heading if the last element wasn't empty
                if result_lines and last_element_type not in ['empty', 'list_item']:
                    result_lines.append("")
                
                result_lines.append(f"## {heading_text}")
                last_element_type = 'heading'
                
                if heading_text == "Publications":
                    inside_publication_section = True
                    publication_counter = 1
                else:
                    inside_publication_section = False
                    
            elif element.name == 'p':
                # Regular paragraph
                text = element.get_text(strip=True)
                if text:
                    # Add spacing after bullet points when transitioning to paragraph
                    if last_element_type == 'list_item':
                        result_lines.append("")
                    
                    # Add spacing before paragraph if needed
                    if result_lines and last_element_type in ['heading', 'paragraph']:
                        result_lines.append("")
                    
                    # Convert links and formatting
                    unwrap_nested_emphasis(element)

                    # Special handling for <em><strong>text</strong>,</em> pattern
                    for em_tag in element.find_all('em'):
                        if em_tag.contents:
                            last_content = em_tag.contents[-1]
                            if isinstance(last_content, NavigableString) and last_content.strip() == ',':
                                if len(em_tag.contents) > 1 and hasattr(em_tag.contents[-2], 'name') and em_tag.contents[-2].name == 'strong':
                                    # Move the comma out of the <em> tag
                                    comma_node = last_content.extract() # Removes comma from em_tag
                                    em_tag.parent.insert(em_tag.parent.contents.index(em_tag) + 1, comma_node)

                    markdown_text = md.markdownify(str(element), heading_style="ATX", bullets="-").strip()
                    result_lines.append(markdown_text)
                    last_element_type = 'paragraph'
                    
            elif 'prosemirror-flat-list' in element.get('class', []):
                # This is a bullet point in the original
                list_content = element.find('div', class_='list-content')
                if list_content:
                    text = list_content.get_text(strip=True)
                    if text:
                        # Convert links and formatting within the bullet point
                        unwrap_nested_emphasis(list_content)
                        markdown_text = md.markdownify(str(list_content), heading_style="ATX", bullets="-").strip()
                        # Remove any paragraph tags that markdownify might add
                        markdown_text = markdown_text.replace('\n\n', ' ').replace('\n', ' ')
                        
                        if inside_publication_section:
                            result_lines.append(f"{publication_counter}. {markdown_text}")
                            publication_counter += 1
                        else:
                            result_lines.append(f"- {markdown_text}")
                        last_element_type = 'list_item'
    
    # Add spacing after the last bullet points if the content ends with them
    if last_element_type == 'list_item':
        result_lines.append("")
    
    # Final cleanup: ensure proper spacing between sections
    final_lines = []
    for i, line in enumerate(result_lines):
        # Skip consecutive empty lines
        if line == "" and i > 0 and len(final_lines) > 0 and final_lines[-1] == "":
            continue
        final_lines.append(line)
    
    # Remove trailing empty lines
    while final_lines and final_lines[-1] == "":
        final_lines.pop()
    
    return '\n'.join(final_lines)

try:
    response = requests.get(url, timeout=30)
    if response.status_code != 200:
        print(f'Failed to retrieve the website. Status code: {response.status_code}')
        exit(1)
except requests.exceptions.RequestException as e:
    print(f'Error fetching the website: {e}')
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
                        # Adjust the names as needed
                        if name == "Minghao's Blog":
                            display_name = 'Blog'
                        elif name == "Google Scholar":
                            display_name = 'Scholar'
                        else:
                            display_name = name
                        social_links[display_name] = href

# Proceed with markdown conversion
markdown_content = process_html_to_markdown(soup)

LOCATOR = "## About Me"
start_index = markdown_content.find(LOCATOR)

if start_index != -1:
    start_index += len(LOCATOR) + 1
    markdown_content = markdown_content[start_index:]

# Clean up the markdown content
markdown_content = markdown_content.strip()

# Apply targeted regex replacements for lingering asterisk issues
# 1. Remove trailing asterisk from a word if it's followed by a bold-italic phrase
#    Example: particularly* ***phrase*** -> particularly ***phrase***
markdown_content = re.sub(r'(\S)\*(?=\s*\*\*\*\w)', r'\1', markdown_content)

# 2. Remove extra asterisk after a bold-italic phrase if it's followed by punctuation/space or end of line
#    Example: ***phrase****, -> ***phrase***,
markdown_content = re.sub(r'(\*\*\*[^\*]+\*\*\*)\*([,.)?!;\s]|$)', r'\1\2', markdown_content)

# 3. Normalize spacing and italics around "and" between bold-italic phrases.
#    Example: ***phrase1***  *and ***phrase2*** -> ***phrase1*** and ***phrase2***
markdown_content = re.sub(r'(\*\*\*[^\*]+\*\*\*)\s*\*?([aA][nN][dD])\*?\s+(?=\*\*\*[^\*]+\*\*\*)', r'\1 and ', markdown_content)

# 4. Specifically fix "***phrase***,* *next phrase*" to "***phrase***, *next phrase*"
markdown_content = re.sub(r'(\*\*\*[^\*]+\*\*\*,\s*)\*(?=\s+\*)', r'\1', markdown_content)

front_matter = "---\nlayout: default\n---\n\n"
new_content = front_matter + markdown_content

# Function to remove the last update line from the content
def remove_last_update_line(content):
    import re
    # Remove 'Last update on' line and any preceding blank lines
    content = re.sub(r'(\n\s*)*Last update on.*$', '', content.strip(), flags=re.MULTILINE)
    return content

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

# Build the new social links HTML with adjusted display names
social_links_html = ''
for name in ['Scholar', 'LinkedIn', 'Blog']:
    href = social_links.get(name)
    if href:
        if name == 'Scholar':
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