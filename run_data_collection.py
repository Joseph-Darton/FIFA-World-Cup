from rename_sheets import rename_all_sheets
from table_scrape import table_scrape_func
import requests
from bs4 import BeautifulSoup


url = 'http://fbref.com/en/comps/1/schedule/World-Cup-Scores-and-Fixtures'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')


urls = []    
for link in soup.find_all('a', string='Match Report'):
    local_href = link.get('href')
    full_link = 'https://www.fbref.com' + local_href
    urls.append(full_link)


for url in urls:
    table_scrape_func(url)
    rename_all_sheets(url)


print('Data Collection Finished')


if __name__ == '__main__':
    table_scrape_func()

