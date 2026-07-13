import pandas as pd
import requests
import os
from bs4 import BeautifulSoup

def table_scrape_func(url):
#reading page to be scraped
    html = requests.get(url).content
    dfs = pd.read_html(html, header=1)[-17:-2]
#creating file name of excel save file based on url/html
    bs = BeautifulSoup(html, 'html.parser')
    title = str(bs.find('h1'))
    file_name = BeautifulSoup(title, 'lxml').text
#creating excel writer and save location
    destination = "C:\\Users\\user\\World Cup Match Data\\"
    writer = pd.ExcelWriter(destination+file_name+'.xlsx', engine='xlsxwriter')   
#iterate through list of dfs to save each df to a new excel sheet
    sheet = int('0')
    for df in dfs:
        sheet = sheet+1
        df.to_excel(writer, sheet_name=str(sheet), index=False)
    writer.close()
