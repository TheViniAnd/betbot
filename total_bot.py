import filecmp
import sqlite3
import requests, bs4
import difflib

url = 'https://ru.dotabuff.com/esports/teams'

s= requests.get(url, headers = {'User-agent': 'your bot 0.1'})
b=bs4.BeautifulSoup(s.text, "html.parser")
team_one = b.select('tbody')
data = []
datae = []
name = []
team_names = [['Evil Geniuses','Team Liquid', 'Team Secret', 'Virtus.pro', 'OG', 'Alliance', 'PSG.LGD', 'Fnatic', 'Vici Gaming', 'Natus Vincere', 'Ninjas in Pyjamas', 'Newbee', 'TNC Predator', 'Mineski',]]
for row in team_one:
    cols = row.find_all('span')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

#print(data)
time_team = b.select('td', class_='r-tab r-group-2')
#print(time_team)
for cow in time_team:
    c = cow.find_all('')
    colss = [ele.text.strip() for ele in c]
    datae.append([ele for ele in cols if ele])
#print(datae)

######################################
#############СРЕДНЕЕ ВРЕМЯ ИГРЫ#######
######################################
for td in b(class_="r-tab r-group-2"):
    if td.text:
        if "," not in td.text:
            print('среднее время = ',"".join(td.text))
    else:
        print('n')



f = open('team.txt', 'w')
f.write("\n".join(data[0]))
f.close()

#team_1 = 'team.txt'
#team_2 = 'team2.txt'


with open('team.txt', 'r') as file1:
    with open('team2.txt', 'r') as file2:
        same = set(file1).intersection(file2)

same.discard('\n')

with open('game_team.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)
        
#diff = difflib.ndiff(open(team_1).readlines(),open(team_2).readlines())
#print(''.join(diff))


#result=list(set(team_names) & set(data))
#print(result)


#print(b)
#pogoda1=team_one[0].getText()

#print(pogoda1)

####################################
##########DATABASE##################
####################################

conn = sqlite3.connect('teams.db')
c = conn.cursor()
try:
    c.execute('''CREATE TABLE team (id integer primary key AUTOINCREMENT, name, time, win varchar)''')
except:
    print('----')
