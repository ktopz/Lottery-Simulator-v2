from bs4 import BeautifulSoup
import requests, json, time

def fetch_names(html):
    retVal = []
    temp = []
    for team in html:
        try:
            split = str(team).split('title=')
            team = split[1].split('"')[1]
            temp.append(team)
        except:
            None
    for i in range(17,32,2):
        try:
            retVal.append(temp[i])
        except:
            None
    return retVal

source = requests.get('http://www.espn.com/nhl/standings/_/view/wild-card').text
soup = BeautifulSoup(source, 'html5lib')
table = soup.find_all('tbody', class_='Table2__tbody')
east_coast = table[0]
west_coast = table[2]
east = east_coast.find_all('a')
west = west_coast.find_all('a')
east_list = fetch_names(east)
west_list = fetch_names(west)
print(west_list)
