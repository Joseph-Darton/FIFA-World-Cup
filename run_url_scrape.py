import requests
from bs4 import BeautifulSoup

url = 'https://fbref.com/en/comps/1/schedule/World-Cup-Scores-and-Fixtures'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

urls = []    
for link in soup.find_all('a', string='Match Report'):
    local_href = link.get('href')
    full_link = 'https://www.fbref.com' + local_href
    urls.append(full_link)
