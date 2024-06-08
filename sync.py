import requests
from bs4 import BeautifulSoup
import markdownify as md
from datetime import datetime

url = 'https://reflect.site/g/mhx/minghao-xie--home-page/c65e893dc6f546f0b0867ec0158fb8ba'

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

markdown_content = md.markdownify(str(soup), heading_style="ATX", bullets="-")

start_index = markdown_content.find("## About Me")

if start_index != -1:
    markdown_content = markdown_content[start_index:]

markdown_content = add_bullet_points(markdown_content)

current_date = datetime.utcnow().strftime('%Y-%m-%d')
markdown_content += f"\n\nLast update on {current_date}"

front_matter = "---\nlayout: default\n---\n\n"
markdown_content = front_matter + markdown_content

with open("index.md", "w", encoding="utf-8") as file:
    file.write(markdown_content)

print("Markdown file has been created successfully.")
