import requests, bs4
from selenium import webdriver
import time
url = 'https://www.parimatch.ru/prematch/all/1%7CCS%7CCS_DOTA2'
driver = webdriver.Firefox()
driver.get(url)
time.sleep(10)
htmlSource = driver.page_source

s = requests.get(url, headers={'User-agent': 'your bot 0.1'})
b = bs4.BeautifulSoup(s.text, "html.parser")
#pattern = re.compile(r'data-percent="(.*)">')
NB_N = []

for item in b.select("[title^='Vega Squadron']") or b(span="competitor-name"):
    NB_N.append(item.text.strip() + '\n\n')
print(NB_N)


time_team = b.find('span', class_='competitor-name')
print(time_team)