import requests
from bs4 import BeautifulSoup
import markdownify

url = 'https://reflect.site/g/mhx/minghao-xie--home-page/c65e893dc6f546f0b0867ec0158fb8ba'

response = requests.get(url)
if response.status_code != 200:
    print(f'Failed to retrieve the website. Status code: {response.status_code}')
    exit(1)

soup = BeautifulSoup(response.content, 'html.parser')

markdown_content = markdownify.markdownify(str(soup), heading_style="ATX")

start_index = markdown_content.find("# Minghao Xie | Home Page")

if start_index != -1:
    markdown_content = markdown_content[start_index:]

with open("index.md", "w", encoding="utf-8") as file:
    file.write(markdown_content)

print("Markdown file has been created successfully.")
