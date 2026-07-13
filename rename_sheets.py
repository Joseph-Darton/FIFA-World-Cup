import requests
import openpyxl
from bs4 import BeautifulSoup


def rename_all_sheets(url):
    html = requests.get(url).content
    bs = BeautifulSoup(html, 'html.parser')
    title = str(bs.find('h1'))
    file_name = BeautifulSoup(title, 'lxml').text


    #separate home and away team names to append to table descriptors
    all_words = file_name.split()
    home_team = all_words[0]
    away_team = all_words[2]


    #create new_sheet_names list and form dict to match new names with numbers
    new_sheet_names_list = [home_team + ' Summary', home_team + ' Passing', home_team + ' Pass Types', home_team + ' Defensive Actions', home_team + ' Possession', home_team + ' Miscellaneous Stats', home_team + ' Goalkeeper Stats',
                        away_team + ' Summary', away_team + ' Passing', away_team + ' Pass Types', away_team + ' Defensive Actions', away_team + ' Possession', away_team + ' Miscellaneous Stats', away_team + ' Goalkeeper Stats',
                        'Shots']
    new_sheet_names_dict = {str(x):element for x, element in enumerate(new_sheet_names_list,1)}


    #edit excel file with new_sheet_names_dict
    destination = "C:\\Users\\user\\World Cup Match Data\\"
    wb = openpyxl.load_workbook(destination+file_name+'.xlsx')


    for sheet in wb.sheetnames:
        new_sheet_name = new_sheet_names_dict[sheet]
        print(f'Changing Sheet name {sheet} to {new_sheet_name}')
        wb[sheet].title = new_sheet_name


    wb.save(file_name+'.xlsx')



