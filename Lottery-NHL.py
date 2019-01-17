from bs4 import BeautifulSoup
import requests

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

def fetch_points(table):
    retVal = []
    rows = table.find_all('tr')
    for row in rows:
        for i in range(11,19):
            concat = 'data-idx="' + str(i)
            if concat in str(row):
                cols = row.find_all('td')
                retVal.append(cols[4].text)
    return retVal

def patch(teams, points):
    list = []
    i = 0
    for team in teams:
        temp = {}
        temp['name'] = team
        temp['points'] = int(points[i])
        list.append(temp)
        i+=1
    return list

def point_sort(dict):
    return dict['points']

source = requests.get('http://www.espn.com/nhl/standings/_/view/wild-card').text
soup = BeautifulSoup(source, 'html5lib')
table = soup.find_all('tbody', class_='Table2__tbody')
east_coast = table[0]
west_coast = table[2]
east = east_coast.find_all('a')
west = west_coast.find_all('a')
east_team_names = fetch_names(east)
west_team_names = fetch_names(west)
east_points = fetch_points(table[1])
west_points = fetch_points(table[3])
all_teams = patch(east_team_names, east_points) + patch(west_team_names, west_points)
all_teams.sort(key=point_sort)
print(all_teams)
