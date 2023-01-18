#HTML url request example
from requests_html import HTML, HTMLSession

session = HTMLSession()
r = session.get('https://webservices3.autotask.net/atservicesrest/v1.0/tickets/query?search={%22filter%22:[\
{%22op%22:%22contains%22,%22field%22:%22title%22,%22value%22:%22ZURICH%22},\
{%22op%22:%22contains%22,%22field%22:%22title%22,%22value%22:%22Uplink%20status%20changed%22},\
{%22op%22:%22noteq%22,%22field%22:%22status%22,%22value%22:5}]}')

print(r.html)

