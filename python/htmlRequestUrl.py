#HTML url request example
from requests_html import HTML, HTMLSession

session = HTMLSession()
r = session.get('')

print(r.html)