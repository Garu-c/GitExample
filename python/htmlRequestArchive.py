#HTML request example
from requests_html import HTML
with open('example.html') as html_file:
    source = html_file.read()
    html = HTML(html = source)

article = html.find('div.article', first=True)
print(article.text)