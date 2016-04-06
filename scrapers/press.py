import requests
from BeautifulSoup import BeautifulSoup
url= 'https://www.oag.state.md.us/Press/index.htm'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

table = soup.findAll('table')[2]

for row in table.findAll('tr'):
    for cell in row.findAll('td'):
	    print cell.text
        if cell.find('a'):
            print cell.find('a') ['href']			