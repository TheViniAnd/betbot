import filecmp
import sqlite3
import requests, bs4
import difflib
import re
import pandas as pd
import json
import numpy

url = 'http://esportlivescore.com/c_frozendawn.html'

s = requests.get(url, headers={'User-agent': 'your bot 0.1'})
b = bs4.BeautifulSoup(s.text, "html.parser")
NB_N = []
for item in b.find("span") or b(
                        class_="team_1_overall_score_0"):
    NB_N.append(item.text.strip() + '\n\n')

print(NB_N)