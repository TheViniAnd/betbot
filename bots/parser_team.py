import filecmp
import sqlite3
import requests, bs4
import difflib
import re
import pandas as pd
import json
import numpy

url = 'https://dota2plusz.ru/team-statistics/'

s = requests.get(url, headers={'User-agent': 'your bot 0.1'})
b = bs4.BeautifulSoup(s.text, "html.parser")
pattern = re.compile(r'data-percent="(.*)">')

one_team = input('Первая команда: ')
two_team = input('Вторая команда: ')

t_1 = 'Neewbee NA'
t_2 = 'Vici Gaming'
t_3 = 'Team Secret'
t_4 = 'Virtus.Pro'
t_5 = 'Team Empire'
t_6 = 'Fnatic'
t_7 = 'Vega Squadron'
t_8 = 'Keen Gaming'
t_9 = 'Team Liquid'
t_10 = 'LGD Gaming'
t_11 = 'Ninjas in Pyjamas'
t_12 = 'Alliance'
t_13 = 'EHOME'
t_14 = 'Team Serenity'
t_15 = 'Natus Vincere'
t_16 = 'PaiN Gaming'
t_17 = 'Evil Geniuses'
t_18 = 'Gambit Esports'
t_19 = 'TNC Pro Team'
t_20 = 'Mineski'
t_21 = 'OG'
t_22 = 'Newbee'
t_23 = 'Royal Never Give Up'
t_24 = 'compLexity'
t_25 = 'Team Aster'
t_26 = 'Invictus Gaming'
t_27 = 'Winstrike'
t_28 = 'J Storm'
t_29 = 'Infamous'

team_one = []
team_two = []

one_team_fb = []
two_team_fb = []

one_team_f10 = []
two_team_f10 = []

one_team_win = []
two_team_win = []

one_team_kill47 = []
two_team_kill47 = []

one_team_min = []
two_team_min = []

for one in t_1, t_2, t_3, t_4, t_5, t_6, t_7,t_8,t_9,t_10,t_11,t_12,t_13,t_14,t_15,t_16,t_17,t_18,t_19,t_20,t_21,t_22,t_23,t_24,t_25,t_26,t_27,t_28,t_29:
    for two in t_1, t_2, t_3, t_4, t_5, t_6, t_7,t_8,t_9,t_10,t_11,t_12,t_13,t_14,t_15,t_16,t_17,t_18,t_19,t_20,t_21,t_22,t_23,t_24,t_25,t_26,t_27,t_28,t_29:
        if one_team == one and two_team == two:
            if one == 'Neewbee NA':
                ################## NEWBEE NA ##################
                NB_N = []
                for item in b.select("[title^='Подробная статистика команды Newbee NA']") or b(
                        class_="team_showall_rows"):
                    NB_N.append(item.text.strip() + '\n\n')
                    NB_N.append(re.findall(pattern, str(item)))
                dann = '"'.join(str(e) for e in NB_N)
                dann_three = dann.split()
                vivod = ' '.join(dann_three)
                if '"' in vivod:
                    lens = len(vivod)
                    kolvo = vivod[106:]

                    one_team_fb = kolvo[2:6]
                    one_team_f10 = kolvo[10:14]
                    one_team_win = kolvo[18:22]
                    one_team_kill47 = kolvo[26:30]
                    one_team_min = kolvo[34:38]

                    print('Neebee NA')
                    print('FB =', one_team_fb + '%')
                    print('F10 =', one_team_f10 + '%')
                    print('WIN = ', one_team_win + '%')
                    print('Тотал килл больше 47 =', one_team_kill47 + '%')
                    print('Тотал больше 34м =', one_team_min + '%')
            elif one == 'Vici Gaming':
                ################## VICI GAMING ##################
                VG = []
                for item2 in b.select("[title^='Подробная статистика команды Vici Gaming']") or b(
                        class_="team_showall_rows"):
                    VG.append(item2.text.strip() + '\n\n')
                    VG.append(re.findall(pattern, str(item2)))
                dann2 = '"'.join(str(e) for e in VG)
                dann_three2 = dann2.split()
                vivod2 = ' '.join(dann_three2)
                if '"' in vivod2:
                    lens = len(vivod2)
                    kolvo = vivod2[108:]
                    one_team_fb = kolvo[2:6]
                    one_team_f10 = kolvo[10:14]
                    one_team_win = kolvo[18:22]
                    one_team_kill47 = kolvo[26:30]
                    one_team_min = kolvo[34:38]
                    print('FB =', one_team_fb + '%')
                    print('F10 =', one_team_f10 + '%')
                    print('WIN = ', one_team_win + '%')
                    print('Тотал килл больше 47 =', one_team_kill47 + '%')
                    print('Тотал больше 34м =', one_team_min + '%')
            elif one == 'Team Secret':
                ################## TEAM SECRET ##################
                SECET = []
                for item3 in b.select("[title^='Подробная статистика команды Team Secret']") or b(class_="team_showall_rows"):
                    SECET.append(item3.text.strip()+'\n\n')
                    SECET.append(re.findall(pattern, str(item3)))
                dann3 = '"'.join(str(e) for e in SECET)
                dann_three3 = dann3.split()
                vivod3 = ' '.join(dann_three3)
                if '"' in vivod3:
                    lens = len(vivod3)
                    kolvo = vivod3[108:]
                    one_team_fb = kolvo[2:6]
                    one_team_f10 = kolvo[10:14]
                    one_team_win = kolvo[18:22]
                    one_team_kill47 = kolvo[26:30]
                    one_team_min = kolvo[34:38]
                    print('FB =',one_team_fb+'%')
                    print('F10 =', one_team_f10 + '%')
                    print('WIN = ', one_team_win + '%')
                    print('Тотал килл больше 47 =', one_team_kill47 + '%')
                    print('Тотал больше 34м =', one_team_min+'%')
            elif one == 'Virtus.Pro':
                ################## VIRTUS.PRO ##################
                VP = []
                for item4 in b.select("[title^='Подробная статистика команды Virtus Pro']") or b(class_="team_showall_rows"):
                    VP.append(item4.text.strip()+'\n\n')
                    VP.append(re.findall(pattern, str(item4)))
                dann4 = '"'.join(str(e) for e in VP)
                dann_three4 = dann4.split()
                vivod4 = ' '.join(dann_three4)
                if '"' in vivod4:
                    lens = len(vivod4)
                    kolvo = vivod4[110:]
                    one_team_fb = kolvo[2:6]
                    one_team_f10 = kolvo[10:14]
                    one_team_win = kolvo[18:22]
                    one_team_kill47 = kolvo[26:30]
                    one_team_min = kolvo[34:38]
                    print('FB =',one_team_fb+'%')
                    print('F10 =', one_team_f10 + '%')
                    print('WIN = ', one_team_win + '%')
                    print('Тотал килл больше 47 =', one_team_kill47 + '%')
                    print('Тотал больше 34м =', one_team_min+'%')
            elif one == 'Fnatic':
                ################## FNATIC ##################
                FNAT = []
                for item5 in b.select("[title^='Подробная статистика команды Fnatic']") or b(class_="team_showall_rows"):
                    FNAT.append(item5.text.strip()+'\n\n')
                    FNAT.append(re.findall(pattern, str(item5)))
                dann5 = '"'.join(str(e) for e in FNAT)
                dann_three5 = dann5.split()
                vivod5 = ' '.join(dann_three5)
                if '"' in vivod5:
                    lens = len(vivod5)
                    kolvo = vivod5[100:]
                    one_team_fb = kolvo[2:6]
                    one_team_f10 = kolvo[10:14]
                    one_team_win = kolvo[18:22]
                    one_team_kill47 = kolvo[26:30]
                    one_team_min = kolvo[34:38]
                    print('FB =',one_team_fb+'%')
                    print('F10 =', one_team_f10 + '%')
                    print('WIN = ', one_team_win + '%')
                    print('Тотал килл больше 47 =', one_team_kill47 + '%')
                    print('Тотал больше 34м =', one_team_min+'%')
            elif one == 'Team Empire':
                ################## Team Empire ##################
                TE = []
                for item6 in b.select("[title^='Подробная статистика команды Team Empire']") or b(class_="team_showall_rows"):
                    TE.append(item6.text.strip()+'\n\n')
                    TE.append(re.findall(pattern, str(item6)))
                dann6 = '"'.join(str(e) for e in TE)
                dann_three6 = dann6.split()
                vivod6 = ' '.join(dann_three6)
                if '"' in vivod6:
                    lens = len(vivod6)
                    kolvo = vivod6[99:]
                    one_team_fb = kolvo[2:6]
                    one_team_f10 = kolvo[10:14]
                    one_team_win = kolvo[18:22]
                    one_team_kill47 = kolvo[26:30]
                    one_team_min = kolvo[34:38]
                    print('FB =',one_team_fb+'%')
                    print('F10 =', one_team_f10 + '%')
                    print('WIN = ', one_team_win + '%')
                    print('Тотал килл больше 47 =', one_team_kill47 + '%')
                    print('Тотал больше 34м =', one_team_min+'%')
            elif one == 'Vega Squadron':
                ################## Vega Squadron ##################
                VS = []
                for item7 in b.select("[title^='Подробная статистика команды Vega Squadron']") or b(class_="team_showall_rows"):
                    VS.append(item7.text.strip()+'\n\n')
                    VS.append(re.findall(pattern, str(item7)))
                dann7 = '"'.join(str(e) for e in VS)
                dann_three7 = dann7.split()
                vivod7 = ' '.join(dann_three7)
                if '"' in vivod7:
                    lens = len(vivod7)
                    kolvo = vivod7[101:]
                    one_team_fb = kolvo[2:6]
                    one_team_f10 = kolvo[10:14]
                    one_team_win = kolvo[18:22]
                    one_team_kill47 = kolvo[26:30]
                    one_team_min = kolvo[34:38]
                    print('FB =',one_team_fb+'%')
                    print('F10 =', one_team_f10 + '%')
                    print('WIN = ', one_team_win + '%')
                    print('Тотал килл больше 47 =', one_team_kill47 + '%')
                    print('Тотал больше 34м =', one_team_min+'%')
            elif one == 'Keen Gaming':
                ################## Keen Gaming ##################
                KG = []
                for item8 in b.select("[title^='Подробная статистика команды Keen Gaming']") or b(class_="team_showall_rows"):
                    KG.append(item8.text.strip()+'\n\n')
                    KG.append(re.findall(pattern, str(item8)))
                dann8 = '"'.join(str(e) for e in KG)
                dann_three8 = dann8.split()
                vivod8 = ' '.join(dann_three8)
                if '"' in vivod8:
                    lens = len(vivod8)
                    kolvo = vivod8[105:]
                    one_team_fb = kolvo[2:6]
                    one_team_f10 = kolvo[10:14]
                    one_team_win = kolvo[18:22]
                    one_team_kill47 = kolvo[26:30]
                    one_team_min = kolvo[34:38]
                    print('FB =',one_team_fb+'%')
                    print('F10 =', one_team_f10 + '%')
                    print('WIN = ', one_team_win + '%')
                    print('Тотал килл больше 47 =', one_team_kill47 + '%')
                    print('Тотал больше 34м =', one_team_min+'%')
            elif one == 'Team Liquid':
                ################## Team Liquid ##################
                TL = []
                for item9 in b.select("[title^='Подробная статистика команды Team Liquid']") or b(class_="team_showall_rows"):
                    TL.append(item9.text.strip()+'\n\n')
                    TL.append(re.findall(pattern, str(item9)))
                dann9 = '"'.join(str(e) for e in TL)
                dann_three9 = dann9.split()
                vivod9 = ' '.join(dann_three9)
                if '"' in vivod9:
                    lens = len(vivod9)
                    kolvo = vivod9[105:]
                    one_team_fb = kolvo[2:6]
                    one_team_f10 = kolvo[10:14]
                    one_team_win = kolvo[18:22]
                    one_team_kill47 = kolvo[26:30]
                    one_team_min = kolvo[34:38]
                    print('FB =',one_team_fb+'%')
                    print('F10 =', one_team_f10 + '%')
                    print('WIN = ', one_team_win + '%')
                    print('Тотал килл больше 47 =', one_team_kill47 + '%')
                    print('Тотал больше 34м =', one_team_min+'%')
            elif one == 'LGD Gaming':
                ################## LGD Gaming ##################
                LGD = []
                for item10 in b.select("[title^='Подробная статистика команды LGD Gaming']") or b(class_="team_showall_rows"):
                    LGD.append(item10.text.strip()+'\n\n')
                    LGD.append(re.findall(pattern, str(item10)))
                dann10 = '"'.join(str(e) for e in LGD)
                dann_three10 = dann10.split()
                vivod10 = ' '.join(dann_three10)
                if '"' in vivod10:
                    lens = len(vivod10)
                    kolvo = vivod10[110:]
                    one_team_fb = kolvo[2:6]
                    one_team_f10 = kolvo[10:14]
                    one_team_win = kolvo[18:22]
                    one_team_kill47 = kolvo[26:30]
                    one_team_min = kolvo[34:38]
                    print('FB =',one_team_fb+'%')
                    print('F10 =', one_team_f10 + '%')
                    print('WIN = ', one_team_win + '%')
                    print('Тотал килл больше 47 =', one_team_kill47 + '%')
                    print('Тотал больше 34м =', one_team_min+'%')
            elif one == 'Ninjas in Pyjamas':
                ################## Ninjas in Pyjamas ##################
                NIP = []
                for item11 in b.select("[title^='Подробная статистика команды Ninjas in Pyjamas']") or b(class_="team_showall_rows"):
                    NIP.append(item11.text.strip()+'\n\n')
                    NIP.append(re.findall(pattern, str(item11)))
                dann11 = '"'.join(str(e) for e in NIP)
                dann_three11 = dann11.split()
                vivod11 = ' '.join(dann_three11)
                if '"' in vivod11:
                    lens = len(vivod11)
                    kolvo = vivod11[115:]
                    one_team_fb = kolvo[2:6]
                    one_team_f10 = kolvo[10:14]
                    one_team_win = kolvo[18:22]
                    one_team_kill47 = kolvo[26:30]
                    one_team_min = kolvo[34:38]
                    print('FB =',one_team_fb+'%')
                    print('F10 =', one_team_f10 + '%')
                    print('WIN = ', one_team_win + '%')
                    print('Тотал килл больше 47 =', one_team_kill47 + '%')
                    print('Тотал больше 34м =', one_team_min+'%')
            elif one == 'Alliance':
                ################## Alliance ##################
                ALL = []
                for item12 in b.select("[title^='Подробная статистика команды Alliance']") or b(class_="team_showall_rows"):
                    ALL.append(item12.text.strip()+'\n\n')
                    ALL.append(re.findall(pattern, str(item12)))
                dann12 = '"'.join(str(e) for e in ALL)
                dann_three12 = dann12.split()
                vivod12 = ' '.join(dann_three12)
                if '"' in vivod12:
                    lens = len(vivod12)
                    kolvo = vivod12[102:]
                    one_team_fb = kolvo[2:6]
                    one_team_f10 = kolvo[10:14]
                    one_team_win = kolvo[18:22]
                    one_team_kill47 = kolvo[26:30]
                    one_team_min = kolvo[34:38]
                    print('FB =',one_team_fb+'%')
                    print('F10 =', one_team_f10 + '%')
                    print('WIN = ', one_team_win + '%')
                    print('Тотал килл больше 47 =', one_team_kill47 + '%')
                    print('Тотал больше 34м =', one_team_min+'%')
            elif one == 'PaiN Gaming':
                ################## PaiN Gaming ##################
                PG = []
                for item13 in b.select("[title^='Подробная статистика команды PaiN Gaming']") or b(class_="team_showall_rows"):
                    PG.append(item13.text.strip()+'\n\n')
                    PG.append(re.findall(pattern, str(item13)))
                dann13 = '"'.join(str(e) for e in PG)
                dann_three13 = dann13.split()
                vivod13 = ' '.join(dann_three13)
                if '"' in vivod13:
                    lens = len(vivod13)
                    kolvo = vivod13[105:]
                    one_team_fb = kolvo[2:6]
                    one_team_f10 = kolvo[10:14]
                    one_team_win = kolvo[18:22]
                    one_team_kill47 = kolvo[26:30]
                    one_team_min = kolvo[34:38]
                    print('FB =',one_team_fb+'%')
                    print('F10 =', one_team_f10 + '%')
                    print('WIN = ', one_team_win + '%')
                    print('Тотал килл больше 47 =', one_team_kill47 + '%')
                    print('Тотал больше 34м =', one_team_min+'%')
            elif one == 'EHOME':
                ################## EHOME ##################
                EH = []
                for item14 in b.select("[title^='Подробная статистика команды EHOME']") or b(class_="team_showall_rows"):
                    EH.append(item14.text.strip()+'\n\n')
                    EH.append(re.findall(pattern, str(item14)))
                dann14 = '"'.join(str(e) for e in EH)
                dann_three14 = dann14.split()
                vivod14 = ' '.join(dann_three14)
                if '"' in vivod14:
                    lens = len(vivod14)
                    kolvo = vivod14[104:]
                    one_team_fb = kolvo[2:6]
                    one_team_f10 = kolvo[10:14]
                    one_team_win = kolvo[18:22]
                    one_team_kill47 = kolvo[26:30]
                    one_team_min = kolvo[34:38]
                    print('FB =',one_team_fb+'%')
                    print('F10 =', one_team_f10 + '%')
                    print('WIN = ', one_team_win + '%')
                    print('Тотал килл больше 47 =', one_team_kill47 + '%')
                    print('Тотал больше 34м =', one_team_min+'%')
            elif one == 'Team Serenity':
                ################## Team Serenity ##################
                TSE = []
                for item15 in b.select("[title^='Подробная статистика команды Team Serenity']") or b(class_="team_showall_rows"):
                    TSE.append(item15.text.strip()+'\n\n')
                    TSE.append(re.findall(pattern, str(item15)))
                dann15 = '"'.join(str(e) for e in TSE)
                dann_three15 = dann15.split()
                vivod15 = ' '.join(dann_three15)
                if '"' in vivod15:
                    lens = len(vivod15)
                    kolvo = vivod15[107:]
                    one_team_fb = kolvo[2:6]
                    one_team_f10 = kolvo[10:14]
                    one_team_win = kolvo[18:22]
                    one_team_kill47 = kolvo[26:30]
                    one_team_min = kolvo[34:38]
                    print('FB =',one_team_fb+'%')
                    print('F10 =', one_team_f10 + '%')
                    print('WIN = ', one_team_win + '%')
                    print('Тотал килл больше 47 =', one_team_kill47 + '%')
                    print('Тотал больше 34м =', one_team_min+'%')
            elif one == 'Natus Vincere':
                ################## Natus Vincere ##################
                NV = []
                for item16 in b.select("[title^='Подробная статистика команды Natus Vincere']") or b(class_="team_showall_rows"):
                    NV.append(item16.text.strip()+'\n\n')
                    NV.append(re.findall(pattern, str(item16)))
                dann16 = '"'.join(str(e) for e in NV)
                dann_three16 = dann16.split()
                vivod16 = ' '.join(dann_three16)
                if '"' in vivod16:
                    lens = len(vivod16)
                    kolvo = vivod16[107:]
                    one_team_fb = kolvo[2:6]
                    one_team_f10 = kolvo[10:14]
                    one_team_win = kolvo[18:22]
                    one_team_kill47 = kolvo[26:30]
                    one_team_min = kolvo[34:38]
                    print('FB =',one_team_fb+'%')
                    print('F10 =', one_team_f10 + '%')
                    print('WIN = ', one_team_win + '%')
                    print('Тотал килл больше 47 =', one_team_kill47 + '%')
                    print('Тотал больше 34м =', one_team_min+'%')
            elif one == 'Evil Geniuses':
                ################## Evil Geniuses ##################
                EG = []
                for item17 in b.select("[title^='Подробная статистика команды Evil Geniuses']") or b(class_="team_showall_rows"):
                    EG.append(item17.text.strip()+'\n\n')
                    EG.append(re.findall(pattern, str(item17)))
                dann17 = '"'.join(str(e) for e in EG)
                dann_three17 = dann17.split()
                vivod17 = ' '.join(dann_three17)
                if '"' in vivod17:
                    lens = len(vivod17)
                    kolvo = vivod17[112:]
                    one_team_fb = kolvo[2:6]
                    one_team_f10 = kolvo[10:14]
                    one_team_win = kolvo[18:22]
                    one_team_kill47 = kolvo[26:30]
                    one_team_min = kolvo[34:38]
                    print('FB =',one_team_fb+'%')
                    print('F10 =', one_team_f10 + '%')
                    print('WIN = ', one_team_win + '%')
                    print('Тотал килл больше 47 =', one_team_kill47 + '%')
                    print('Тотал больше 34м =', one_team_min+'%')
            elif one == 'Gambit Esports':
                ################## Gambit Esports ##################
                GE = []
                for item18 in b.select("[title^='Подробная статистика команды Gambit Esports']") or b(class_="team_showall_rows"):
                    GE.append(item18.text.strip()+'\n\n')
                    GE.append(re.findall(pattern, str(item18)))
                dann18 = '"'.join(str(e) for e in GE)
                dann_three18 = dann18.split()
                vivod18 = ' '.join(dann_three18)
                if '"' in vivod18:
                    lens = len(vivod18)
                    kolvo = vivod18[108:]
                    one_team_fb = kolvo[2:6]
                    one_team_f10 = kolvo[10:14]
                    one_team_win = kolvo[18:22]
                    one_team_kill47 = kolvo[26:30]
                    one_team_min = kolvo[34:38]
                    print('FB =',one_team_fb+'%')
                    print('F10 =', one_team_f10 + '%')
                    print('WIN = ', one_team_win + '%')
                    print('Тотал килл больше 47 =', one_team_kill47 + '%')
                    print('Тотал больше 34м =', one_team_min+'%')
            elif one == 'TNC Pro Team':
                ################## TNC Pro Team ##################
                TNC = []
                for item19 in b.select("[title^='Подробная статистика команды TNC Pro Team']") or b(class_="team_showall_rows"):
                    TNC.append(item19.text.strip()+'\n\n')
                    TNC.append(re.findall(pattern, str(item19)))
                dann19 = '"'.join(str(e) for e in TNC)
                dann_three19 = dann19.split()
                vivod19 = ' '.join(dann_three19)
                if '"' in vivod19:
                    lens = len(vivod19)
                    kolvo = vivod19[106:]
                    one_team_fb = kolvo[2:6]
                    one_team_f10 = kolvo[10:14]
                    one_team_win = kolvo[18:22]
                    one_team_kill47 = kolvo[26:30]
                    one_team_min = kolvo[34:38]
                    print('FB =',one_team_fb+'%')
                    print('F10 =', one_team_f10 + '%')
                    print('WIN = ', one_team_win + '%')
                    print('Тотал килл больше 47 =', one_team_kill47 + '%')
                    print('Тотал больше 34м =', one_team_min+'%')
            elif one == 'Mineski':
                ################## Mineski ##################
                MIN = []
                for item20 in b.select("[title^='Подробная статистика команды Mineski']") or b(class_="team_showall_rows"):
                    MIN.append(item20.text.strip()+'\n\n')
                    MIN.append(re.findall(pattern, str(item20)))
                dann20 = '"'.join(str(e) for e in MIN)
                dann_three20 = dann20.split()
                vivod20 = ' '.join(dann_three20)
                if '"' in vivod20:
                    lens = len(vivod20)
                    kolvo = vivod20[101:]
                    one_team_fb = kolvo[2:6]
                    one_team_f10 = kolvo[10:14]
                    one_team_win = kolvo[18:22]
                    one_team_kill47 = kolvo[26:30]
                    one_team_min = kolvo[34:38]
                    print('FB =',one_team_fb+'%')
                    print('F10 =', one_team_f10 + '%')
                    print('WIN = ', one_team_win + '%')
                    print('Тотал килл больше 47 =', one_team_kill47 + '%')
                    print('Тотал больше 34м =', one_team_min+'%')
            elif one == 'OG':
                ################## OG ##################
                OG = []
                for item21 in b.select("[title^='Подробная статистика команды OG']") or b(class_="team_showall_rows"):
                    OG.append(item21.text.strip()+'\n\n')
                    OG.append(re.findall(pattern, str(item21)))
                dann21 = '"'.join(str(e) for e in OG)
                dann_three21 = dann21.split()
                vivod21 = ' '.join(dann_three21)
                if '"' in vivod21:
                    lens = len(vivod21)
                    kolvo = vivod21[96:]
                    one_team_fb = kolvo[2:6]
                    one_team_f10 = kolvo[10:14]
                    one_team_win = kolvo[18:22]
                    one_team_kill47 = kolvo[26:30]
                    one_team_min = kolvo[34:38]
                    print('FB =',one_team_fb+'%')
                    print('F10 =', one_team_f10 + '%')
                    print('WIN = ', one_team_win + '%')
                    print('Тотал килл больше 47 =', one_team_kill47 + '%')
                    print('Тотал больше 34м =', one_team_min+'%')
            elif one == 'Newbee':
                ################## Newbee ##################
                NB = []
                for item22 in b.select("[title^='Подробная статистика команды Newbee']") or b(class_="team_showall_rows"):
                    NB.append(item22.text.strip()+'\n\n')
                    NB.append(re.findall(pattern, str(item22)))
                dann22 = '"'.join(str(e) for e in NB)
                dann_three22 = dann22.split()
                vivod22 = ' '.join(dann_three22)
                if '"' in vivod22:
                    lens = len(vivod22)
                    kolvo = vivod22[236:]
                    one_team_fb = kolvo[2:6]
                    one_team_f10 = kolvo[10:14]
                    one_team_win = kolvo[18:22]
                    one_team_kill47 = kolvo[26:30]
                    one_team_min = kolvo[34:38]
                    print('FB =',one_team_fb+'%')
                    print('F10 =', one_team_f10 + '%')
                    print('WIN = ', one_team_win + '%')
                    print('Тотал килл больше 47 =', one_team_kill47 + '%')
                    print('Тотал больше 34м =', one_team_min+'%')
            elif one == 'Royal Never Give Up':
                ################## RNGU ##################
                RNGU = []
                for item23 in b.select("[title^='Подробная статистика команды Royal Never Give Up']") or b(class_="team_showall_rows"):
                    RNGU.append(item23.text.strip()+'\n\n')
                    RNGU.append(re.findall(pattern, str(item23)))
                dann23 = '"'.join(str(e) for e in RNGU)
                dann_three23 = dann23.split()
                vivod23 = ' '.join(dann_three23)
                if '"' in vivod23:
                    lens = len(vivod23)
                    kolvo = vivod23[113:]
                    one_team_fb = kolvo[2:6]
                    one_team_f10 = kolvo[10:14]
                    one_team_win = kolvo[18:22]
                    one_team_kill47 = kolvo[26:30]
                    one_team_min = kolvo[34:38]
                    print('FB =',one_team_fb+'%')
                    print('F10 =', one_team_f10 + '%')
                    print('WIN = ', one_team_win + '%')
                    print('Тотал килл больше 47 =', one_team_kill47 + '%')
                    print('Тотал больше 34м =', one_team_min+'%')
            elif one == 'compLexity':
                ################## compLexity ##################
                COL = []
                for item24 in b.select("[title^='Подробная статистика команды compLexity']") or b(class_="team_showall_rows"):
                    COL.append(item24.text.strip()+'\n\n')
                    COL.append(re.findall(pattern, str(item24)))
                dann24 = '"'.join(str(e) for e in COL)
                dann_three24 = dann24.split()
                vivod24 = ' '.join(dann_three24)
                if '"' in vivod24:
                    lens = len(vivod24)
                    kolvo = vivod24[104:]
                    one_team_fb = kolvo[2:6]
                    one_team_f10 = kolvo[10:14]
                    one_team_win = kolvo[18:22]
                    one_team_kill47 = kolvo[26:30]
                    one_team_min = kolvo[34:38]
                    print('FB =',one_team_fb+'%')
                    print('F10 =', one_team_f10 + '%')
                    print('WIN = ', one_team_win + '%')
                    print('Тотал килл больше 47 =', one_team_kill47 + '%')
                    print('Тотал больше 34м =', one_team_min+'%')
            elif one == 'Team Aster':
                ################## Team Aster ##################
                TAS = []
                for item25 in b.select("[title^='Подробная статистика команды Team Aster']") or b(class_="team_showall_rows"):
                    TAS.append(item25.text.strip()+'\n\n')
                    TAS.append(re.findall(pattern, str(item25)))
                dann25 = '"'.join(str(e) for e in TAS)
                dann_three25 = dann25.split()
                vivod25 = ' '.join(dann_three25)
                if '"' in vivod25:
                    lens = len(vivod25)
                    kolvo = vivod25[98:]
                    one_team_fb = kolvo[2:6]
                    one_team_f10 = kolvo[10:14]
                    one_team_win = kolvo[18:22]
                    one_team_kill47 = kolvo[26:30]
                    one_team_min = kolvo[34:38]
                    print('FB =',one_team_fb+'%')
                    print('F10 =', one_team_f10 + '%')
                    print('WIN = ', one_team_win + '%')
                    print('Тотал килл больше 47 =', one_team_kill47 + '%')
                    print('Тотал больше 34м =', one_team_min+'%')
            elif one == 'Invictus Gaming':
                ################## Invictus Gaming ##################
                IG = []
                for item26 in b.select("[title^='Подробная статистика команды Invictus Gaming']") or b(class_="team_showall_rows"):
                    IG.append(item26.text.strip()+'\n\n')
                    IG.append(re.findall(pattern, str(item26)))
                dann26 = '"'.join(str(e) for e in IG)
                dann_three26 = dann26.split()
                vivod26 = ' '.join(dann_three26)
                if '"' in vivod26:
                    lens = len(vivod26)
                    kolvo = vivod26[109:]
                    one_team_fb = kolvo[2:6]
                    one_team_f10 = kolvo[10:14]
                    one_team_win = kolvo[18:22]
                    one_team_kill47 = kolvo[26:30]
                    one_team_min = kolvo[34:38]
                    print('FB =',one_team_fb+'%')
                    print('F10 =', one_team_f10 + '%')
                    print('WIN = ', one_team_win + '%')
                    print('Тотал килл больше 47 =', one_team_kill47 + '%')
                    print('Тотал больше 34м =', one_team_min+'%')
            elif one == 'Winstrike':
                ################## Winstrike ##################
                WINS = []
                for item27 in b.select("[title^='Подробная статистика команды Winstrike']") or b(class_="team_showall_rows"):
                    WINS.append(item27.text.strip()+'\n\n')
                    WINS.append(re.findall(pattern, str(item27)))
                dann27 = '"'.join(str(e) for e in WINS)
                dann_three27 = dann27.split()
                vivod27 = ' '.join(dann_three27)
                if '"' in vivod27:
                    lens = len(vivod27)
                    kolvo = vivod27[103:]
                    one_team_fb = kolvo[2:6]
                    one_team_f10 = kolvo[10:14]
                    one_team_win = kolvo[18:22]
                    one_team_kill47 = kolvo[26:30]
                    one_team_min = kolvo[34:38]
                    print('FB =',one_team_fb+'%')
                    print('F10 =', one_team_f10 + '%')
                    print('WIN = ', one_team_win + '%')
                    print('Тотал килл больше 47 =', one_team_kill47 + '%')
                    print('Тотал больше 34м =', one_team_min+'%')
            elif one == 'J Storm':
                ################## J Storm ##################
                JS = []
                for item28 in b.select("[title^='Подробная статистика команды J Storm']") or b(class_="team_showall_rows"):
                    JS.append(item28.text.strip()+'\n\n')
                    JS.append(re.findall(pattern, str(item28)))
                dann28 = '"'.join(str(e) for e in JS)
                dann_three28 = dann28.split()
                vivod28 = ' '.join(dann_three28)
                if '"' in vivod28:
                    lens = len(vivod28)
                    kolvo = vivod28[96:]
                    one_team_fb = kolvo[2:6]
                    one_team_f10 = kolvo[10:14]
                    one_team_win = kolvo[18:22]
                    one_team_kill47 = kolvo[26:30]
                    one_team_min = kolvo[34:38]
                    print('FB =',one_team_fb+'%')
                    print('F10 =', one_team_f10 + '%')
                    print('WIN = ', one_team_win + '%')
                    print('Тотал килл больше 47 =', one_team_kill47 + '%')
                    print('Тотал больше 34м =', one_team_min+'%')
            elif one == 'Infamous':
                ################## Infamous ##################
                INF = []
                for item29 in b.select("[title^='Подробная статистика команды Infamous']") or b(class_="team_showall_rows"):
                    INF.append(item29.text.strip()+'\n\n')
                    INF.append(re.findall(pattern, str(item29)))
                dann29 = '"'.join(str(e) for e in INF)
                dann_three29 = dann29.split()
                vivod29 = ' '.join(dann_three29)
                if '"' in vivod29:
                    lens = len(vivod29)
                    kolvo = vivod29[100:]
                    one_team_fb = kolvo[2:5]
                    one_team_f10 = kolvo[10:13]
                    one_team_win = kolvo[18:21]
                    one_team_kill47 = kolvo[26:29]
                    one_team_min = kolvo[34:37]
                    print('FB =',one_team_fb+'%')
                    print('F10 =', one_team_f10 + '%')
                    print('WIN = ', one_team_win + '%')
                    print('Тотал килл больше 47 =', one_team_kill47 + '%')
                    print('Тотал больше 34м =', one_team_min+'%')


            ##############


            if two == 'Neewbee NA':
                ################## NEWBEE NA ##################
                NB_N = []
                for item in b.select("[title^='Подробная статистика команды Newbee NA']") or b(
                            class_="team_showall_rows"):
                    NB_N.append(item.text.strip() + '\n\n')
                    NB_N.append(re.findall(pattern, str(item)))
                dann = '"'.join(str(e) for e in NB_N)
                dann_three = dann.split()
                vivod = ' '.join(dann_three)
                if '"' in vivod:
                    lens = len(vivod)
                    kolvo = vivod[100:]
                    two_team_fb = kolvo[2:6]
                    two_team_f10 = kolvo[10:14]
                    two_team_win = kolvo[18:22]
                    two_team_kill47 = kolvo[26:30]
                    two_team_min = kolvo[34:38]
                    print('Neebee NA')
                    print('FB =', two_team_fb + '%')
                    print('F10 =', two_team_f10 + '%')
                    print('WIN = ', two_team_win + '%')
                    print('Тотал килл больше 47 =', two_team_kill47 + '%')
                    print('Тотал больше 34м =', two_team_min + '%')
            elif two == 'Vici Gaming':
                ################## VICI GAMING ##################
                VG = []
                for item2 in b.select("[title^='Подробная статистика команды Vici Gaming']") or b(
                        class_="team_showall_rows"):
                    VG.append(item2.text.strip() + '\n\n')
                    VG.append(re.findall(pattern, str(item2)))
                dann2 = '"'.join(str(e) for e in VG)
                dann_three2 = dann2.split()
                vivod2 = ' '.join(dann_three2)
                if '"' in vivod2:
                    lens = len(vivod2)
                    kolvo = vivod2[107:]
                    two_team_fb = kolvo[2:6]
                    two_team_f10 = kolvo[10:14]
                    two_team_win = kolvo[18:22]
                    two_team_kill47 = kolvo[26:30]
                    two_team_min = kolvo[34:38]
                    print('FB =', two_team_fb + '%')
                    print('F10 =', two_team_f10 + '%')
                    print('WIN = ', two_team_win + '%')
                    print('Тотал килл больше 47 =', two_team_kill47 + '%')
                    print('Тотал больше 34м =', two_team_min + '%')
            elif two == 'Team Secret':
                ################## TEAM SECRET ##################
                SECET = []
                for item3 in b.select("[title^='Подробная статистика команды Team Secret']") or b(
                        class_="team_showall_rows"):
                    SECET.append(item3.text.strip() + '\n\n')
                    SECET.append(re.findall(pattern, str(item3)))
                dann3 = '"'.join(str(e) for e in SECET)
                dann_three3 = dann3.split()
                vivod3 = ' '.join(dann_three3)
                if '"' in vivod3:
                    lens = len(vivod3)
                    kolvo = vivod3[108:]
                    two_team_fb = kolvo[2:6]
                    two_team_f10 = kolvo[10:14]
                    two_team_win = kolvo[18:22]
                    two_team_kill47 = kolvo[26:30]
                    two_team_min = kolvo[34:38]
                    print('FB =', two_team_fb + '%')
                    print('F10 =', two_team_f10 + '%')
                    print('WIN = ', two_team_win + '%')
                    print('Тотал килл больше 47 =', two_team_kill47 + '%')
                    print('Тотал больше 34м =', two_team_min + '%')
            elif two == 'Virtus.Pro':
                ################## VIRTUS.PRO ##################
                VP = []
                for item4 in b.select("[title^='Подробная статистика команды Virtus Pro']") or b(
                        class_="team_showall_rows"):
                    VP.append(item4.text.strip() + '\n\n')
                    VP.append(re.findall(pattern, str(item4)))
                dann4 = '"'.join(str(e) for e in VP)
                dann_three4 = dann4.split()
                vivod4 = ' '.join(dann_three4)
                if '"' in vivod4:
                    lens = len(vivod4)
                    kolvo = vivod4[110:]
                    two_team_fb = kolvo[2:6]
                    two_team_f10 = kolvo[10:14]
                    two_team_win = kolvo[18:22]
                    two_team_kill47 = kolvo[26:30]
                    two_team_min = kolvo[34:38]
                    print('FB =', two_team_fb + '%')
                    print('F10 =', two_team_f10 + '%')
                    print('WIN = ', two_team_win + '%')
                    print('Тотал килл больше 47 =', two_team_kill47 + '%')
                    print('Тотал больше 34м =', two_team_min + '%')
            elif two == 'Fnatic':
                ################## FNATIC ##################
                FNAT = []
                for item5 in b.select("[title^='Подробная статистика команды Fnatic']") or b(
                        class_="team_showall_rows"):
                    FNAT.append(item5.text.strip() + '\n\n')
                    FNAT.append(re.findall(pattern, str(item5)))
                dann5 = '"'.join(str(e) for e in FNAT)
                dann_three5 = dann5.split()
                vivod5 = ' '.join(dann_three5)
                if '"' in vivod5:
                    lens = len(vivod5)
                    kolvo = vivod5[100:]
                    two_team_fb = kolvo[2:6]
                    two_team_f10 = kolvo[10:14]
                    two_team_win = kolvo[18:22]
                    two_team_kill47 = kolvo[26:30]
                    two_team_min = kolvo[34:38]
                    print('FB =', two_team_fb + '%')
                    print('F10 =', two_team_f10 + '%')
                    print('WIN = ', two_team_win + '%')
                    print('Тотал килл больше 47 =', two_team_kill47 + '%')
                    print('Тотал больше 34м =', two_team_min + '%')
            elif two == 'Team Empire':
                ################## Team Empire ##################
                TE = []
                for item6 in b.select("[title^='Подробная статистика команды Team Empire']") or b(
                        class_="team_showall_rows"):
                    TE.append(item6.text.strip() + '\n\n')
                    TE.append(re.findall(pattern, str(item6)))
                dann6 = '"'.join(str(e) for e in TE)
                dann_three6 = dann6.split()
                vivod6 = ' '.join(dann_three6)
                if '"' in vivod6:
                    lens = len(vivod6)
                    kolvo = vivod6[99:]
                    two_team_fb = kolvo[2:6]
                    two_team_f10 = kolvo[10:14]
                    two_team_win = kolvo[18:22]
                    two_team_kill47 = kolvo[26:30]
                    two_team_min = kolvo[34:38]
                    print('FB =', two_team_fb + '%')
                    print('F10 =', two_team_f10 + '%')
                    print('WIN = ', two_team_win + '%')
                    print('Тотал килл больше 47 =', two_team_kill47 + '%')
                    print('Тотал больше 34м =', two_team_min + '%')
            elif two == 'Vega Squadron':
                ################## Vega Squadron ##################
                VS = []
                for item7 in b.select("[title^='Подробная статистика команды Vega Squadron']") or b(
                        class_="team_showall_rows"):
                    VS.append(item7.text.strip() + '\n\n')
                    VS.append(re.findall(pattern, str(item7)))
                dann7 = '"'.join(str(e) for e in VS)
                dann_three7 = dann7.split()
                vivod7 = ' '.join(dann_three7)
                if '"' in vivod7:
                    lens = len(vivod7)
                    kolvo = vivod7[101:]
                    two_team_fb = kolvo[2:6]
                    two_team_f10 = kolvo[10:14]
                    two_team_win = kolvo[18:22]
                    two_team_kill47 = kolvo[26:30]
                    two_team_min = kolvo[34:38]
                    print('FB =', two_team_fb + '%')
                    print('F10 =', two_team_f10 + '%')
                    print('WIN = ', two_team_win + '%')
                    print('Тотал килл больше 47 =', two_team_kill47 + '%')
                    print('Тотал больше 34м =', two_team_min + '%')
            elif two == 'Keen Gaming':
                ################## Keen Gaming ##################
                KG = []
                for item8 in b.select("[title^='Подробная статистика команды Keen Gaming']") or b(
                        class_="team_showall_rows"):
                    KG.append(item8.text.strip() + '\n\n')
                    KG.append(re.findall(pattern, str(item8)))
                dann8 = '"'.join(str(e) for e in KG)
                dann_three8 = dann8.split()
                vivod8 = ' '.join(dann_three8)
                if '"' in vivod8:
                    lens = len(vivod8)
                    kolvo = vivod8[105:]
                    two_team_fb = kolvo[2:6]
                    two_team_f10 = kolvo[10:14]
                    two_team_win = kolvo[18:22]
                    two_team_kill47 = kolvo[26:30]
                    two_team_min = kolvo[34:38]
                    print('FB =', two_team_fb + '%')
                    print('F10 =', two_team_f10 + '%')
                    print('WIN = ', two_team_win + '%')
                    print('Тотал килл больше 47 =', two_team_kill47 + '%')
                    print('Тотал больше 34м =', two_team_min + '%')
            elif two == 'Team Liquid':
                ################## Team Liquid ##################
                TL = []
                for item9 in b.select("[title^='Подробная статистика команды Team Liquid']") or b(
                        class_="team_showall_rows"):
                    TL.append(item9.text.strip() + '\n\n')
                    TL.append(re.findall(pattern, str(item9)))
                dann9 = '"'.join(str(e) for e in TL)
                dann_three9 = dann9.split()
                vivod9 = ' '.join(dann_three9)
                if '"' in vivod9:
                    lens = len(vivod9)
                    kolvo = vivod9[102:]
                    two_team_fb = kolvo[2:6]
                    two_team_f10 = kolvo[10:14]
                    two_team_win = kolvo[18:22]
                    two_team_kill47 = kolvo[26:30]
                    two_team_min = kolvo[34:38]
                    print('FB =', two_team_fb + '%')
                    print('F10 =', two_team_f10 + '%')
                    print('WIN = ', two_team_win + '%')
                    print('Тотал килл больше 47 =', two_team_kill47 + '%')
                    print('Тотал больше 34м =', two_team_min + '%')
            elif two == 'LGD Gaming':
                ################## LGD Gaming ##################
                LGD = []
                for item10 in b.select("[title^='Подробная статистика команды LGD Gaming']") or b(
                        class_="team_showall_rows"):
                    LGD.append(item10.text.strip() + '\n\n')
                    LGD.append(re.findall(pattern, str(item10)))
                dann10 = '"'.join(str(e) for e in LGD)
                dann_three10 = dann10.split()
                vivod10 = ' '.join(dann_three10)
                if '"' in vivod10:
                    lens = len(vivod10)
                    kolvo = vivod10[110:]
                    two_team_fb = kolvo[2:6]
                    two_team_f10 = kolvo[10:14]
                    two_team_win = kolvo[18:22]
                    two_team_kill47 = kolvo[26:30]
                    two_team_min = kolvo[34:38]
                    print('FB =', two_team_fb + '%')
                    print('F10 =', two_team_f10 + '%')
                    print('WIN = ', two_team_win + '%')
                    print('Тотал килл больше 47 =', two_team_kill47 + '%')
                    print('Тотал больше 34м =', two_team_min + '%')
            elif two == 'Ninjas in Pyjamas':
                ################## Ninjas in Pyjamas ##################
                NIP = []
                for item11 in b.select("[title^='Подробная статистика команды Ninjas in Pyjamas']") or b(
                        class_="team_showall_rows"):
                    NIP.append(item11.text.strip() + '\n\n')
                    NIP.append(re.findall(pattern, str(item11)))
                dann11 = '"'.join(str(e) for e in NIP)
                dann_three11 = dann11.split()
                vivod11 = ' '.join(dann_three11)
                if '"' in vivod11:
                    lens = len(vivod11)
                    kolvo = vivod11[114:]
                    two_team_fb = kolvo[2:6]
                    two_team_f10 = kolvo[10:14]
                    two_team_win = kolvo[18:22]
                    two_team_kill47 = kolvo[26:30]
                    two_team_min = kolvo[34:38]
                    print('FB =', two_team_fb + '%')
                    print('F10 =', two_team_f10 + '%')
                    print('WIN = ', two_team_win + '%')
                    print('Тотал килл больше 47 =', two_team_kill47 + '%')
                    print('Тотал больше 34м =', two_team_min + '%')
            elif two == 'Alliance':
                ################## Alliance ##################
                ALL = []
                for item12 in b.select("[title^='Подробная статистика команды Alliance']") or b(
                        class_="team_showall_rows"):
                    ALL.append(item12.text.strip() + '\n\n')
                    ALL.append(re.findall(pattern, str(item12)))
                dann12 = '"'.join(str(e) for e in ALL)
                dann_three12 = dann12.split()
                vivod12 = ' '.join(dann_three12)
                if '"' in vivod12:
                    lens = len(vivod12)
                    kolvo = vivod12[102:]
                    two_team_fb = kolvo[2:6]
                    two_team_f10 = kolvo[10:14]
                    two_team_win = kolvo[18:22]
                    two_team_kill47 = kolvo[26:30]
                    two_team_min = kolvo[34:38]
                    print('FB =', two_team_fb + '%')
                    print('F10 =', two_team_f10 + '%')
                    print('WIN = ', two_team_win + '%')
                    print('Тотал килл больше 47 =', two_team_kill47 + '%')
                    print('Тотал больше 34м =', two_team_min + '%')
            elif two == 'PaiN Gaming':
                ################## PaiN Gaming ##################
                PG = []
                for item13 in b.select("[title^='Подробная статистика команды PaiN Gaming']") or b(
                        class_="team_showall_rows"):
                    PG.append(item13.text.strip() + '\n\n')
                    PG.append(re.findall(pattern, str(item13)))
                dann13 = '"'.join(str(e) for e in PG)
                dann_three13 = dann13.split()
                vivod13 = ' '.join(dann_three13)
                if '"' in vivod13:
                    lens = len(vivod13)
                    kolvo = vivod13[105:]
                    two_team_fb = kolvo[2:6]
                    two_team_f10 = kolvo[10:14]
                    two_team_win = kolvo[18:22]
                    two_team_kill47 = kolvo[26:30]
                    two_team_min = kolvo[34:38]
                    print('FB =', two_team_fb + '%')
                    print('F10 =', two_team_f10 + '%')
                    print('WIN = ', two_team_win + '%')
                    print('Тотал килл больше 47 =', two_team_kill47 + '%')
                    print('Тотал больше 34м =', two_team_min + '%')
            elif two == 'EHOME':
                ################## EHOME ##################
                EH = []
                for item14 in b.select("[title^='Подробная статистика команды EHOME']") or b(
                        class_="team_showall_rows"):
                    EH.append(item14.text.strip() + '\n\n')
                    EH.append(re.findall(pattern, str(item14)))
                dann14 = '"'.join(str(e) for e in EH)
                dann_three14 = dann14.split()
                vivod14 = ' '.join(dann_three14)
                if '"' in vivod14:
                    lens = len(vivod14)
                    kolvo = vivod14[104:]
                    two_team_fb = kolvo[2:6]
                    two_team_f10 = kolvo[10:14]
                    two_team_win = kolvo[18:22]
                    two_team_kill47 = kolvo[26:30]
                    two_team_min = kolvo[34:38]
                    print('FB =', two_team_fb + '%')
                    print('F10 =', two_team_f10 + '%')
                    print('WIN = ', two_team_win + '%')
                    print('Тотал килл больше 47 =', two_team_kill47 + '%')
                    print('Тотал больше 34м =', two_team_min + '%')
            elif two == 'Team Serenity':
                ################## Team Serenity ##################
                TSE = []
                for item15 in b.select("[title^='Подробная статистика команды Team Serenity']") or b(
                        class_="team_showall_rows"):
                    TSE.append(item15.text.strip() + '\n\n')
                    TSE.append(re.findall(pattern, str(item15)))
                dann15 = '"'.join(str(e) for e in TSE)
                dann_three15 = dann15.split()
                vivod15 = ' '.join(dann_three15)
                if '"' in vivod15:
                    lens = len(vivod15)
                    kolvo = vivod15[107:]
                    two_team_fb = kolvo[2:6]
                    two_team_f10 = kolvo[10:14]
                    two_team_win = kolvo[18:22]
                    two_team_kill47 = kolvo[26:30]
                    two_team_min = kolvo[34:38]
                    print('FB =', two_team_fb + '%')
                    print('F10 =', two_team_f10 + '%')
                    print('WIN = ', two_team_win + '%')
                    print('Тотал килл больше 47 =', two_team_kill47 + '%')
                    print('Тотал больше 34м =', two_team_min + '%')
            elif two == 'Natus Vincere':
                ################## Natus Vincere ##################
                NV = []
                for item16 in b.select("[title^='Подробная статистика команды Natus Vincere']") or b(
                        class_="team_showall_rows"):
                    NV.append(item16.text.strip() + '\n\n')
                    NV.append(re.findall(pattern, str(item16)))
                dann16 = '"'.join(str(e) for e in NV)
                dann_three16 = dann16.split()
                vivod16 = ' '.join(dann_three16)
                if '"' in vivod16:
                    lens = len(vivod16)
                    kolvo = vivod16[107:]
                    two_team_fb = kolvo[2:6]
                    two_team_f10 = kolvo[10:14]
                    two_team_win = kolvo[18:22]
                    two_team_kill47 = kolvo[26:30]
                    two_team_min = kolvo[34:38]
                    print('FB =', two_team_fb + '%')
                    print('F10 =', two_team_f10 + '%')
                    print('WIN = ', two_team_win + '%')
                    print('Тотал килл больше 47 =', two_team_kill47 + '%')
                    print('Тотал больше 34м =', two_team_min + '%')
            elif two == 'Evil Geniuses':
                ################## Evil Geniuses ##################
                EG = []
                for item17 in b.select("[title^='Подробная статистика команды Evil Geniuses']") or b(
                        class_="team_showall_rows"):
                    EG.append(item17.text.strip() + '\n\n')
                    EG.append(re.findall(pattern, str(item17)))
                dann17 = '"'.join(str(e) for e in EG)
                dann_three17 = dann17.split()
                vivod17 = ' '.join(dann_three17)
                if '"' in vivod17:
                    lens = len(vivod17)
                    kolvo = vivod17[112:]
                    two_team_fb = kolvo[2:6]
                    two_team_f10 = kolvo[10:14]
                    two_team_win = kolvo[18:22]
                    two_team_kill47 = kolvo[26:30]
                    two_team_min = kolvo[34:38]
                    print('FB =', two_team_fb + '%')
                    print('F10 =', two_team_f10 + '%')
                    print('WIN = ', two_team_win + '%')
                    print('Тотал килл больше 47 =', two_team_kill47 + '%')
                    print('Тотал больше 34м =', two_team_min + '%')
            elif two == 'Gambit Esports':
                ################## Gambit Esports ##################
                GE = []
                for item18 in b.select("[title^='Подробная статистика команды Gambit Esports']") or b(
                        class_="team_showall_rows"):
                    GE.append(item18.text.strip() + '\n\n')
                    GE.append(re.findall(pattern, str(item18)))
                dann18 = '"'.join(str(e) for e in GE)
                dann_three18 = dann18.split()
                vivod18 = ' '.join(dann_three18)
                if '"' in vivod18:
                    lens = len(vivod18)
                    kolvo = vivod18[108:]
                    two_team_fb = kolvo[2:6]
                    two_team_f10 = kolvo[10:14]
                    two_team_win = kolvo[18:22]
                    two_team_kill47 = kolvo[26:30]
                    two_team_min = kolvo[34:38]
                    print('FB =', two_team_fb + '%')
                    print('F10 =', two_team_f10 + '%')
                    print('WIN = ', two_team_win + '%')
                    print('Тотал килл больше 47 =', two_team_kill47 + '%')
                    print('Тотал больше 34м =', two_team_min + '%')
            elif two == 'TNC Pro Team':
                ################## TNC Pro Team ##################
                TNC = []
                for item19 in b.select("[title^='Подробная статистика команды TNC Pro Team']") or b(
                        class_="team_showall_rows"):
                    TNC.append(item19.text.strip() + '\n\n')
                    TNC.append(re.findall(pattern, str(item19)))
                dann19 = '"'.join(str(e) for e in TNC)
                dann_three19 = dann19.split()
                vivod19 = ' '.join(dann_three19)
                if '"' in vivod19:
                    lens = len(vivod19)
                    kolvo = vivod19[106:]
                    two_team_fb = kolvo[2:6]
                    two_team_f10 = kolvo[10:14]
                    two_team_win = kolvo[18:22]
                    two_team_kill47 = kolvo[26:30]
                    two_team_min = kolvo[34:38]
                    print('FB =', two_team_fb + '%')
                    print('F10 =', two_team_f10 + '%')
                    print('WIN = ', two_team_win + '%')
                    print('Тотал килл больше 47 =', two_team_kill47 + '%')
                    print('Тотал больше 34м =', two_team_min + '%')
            elif two == 'Mineski':
                ################## Mineski ##################
                MIN = []
                for item20 in b.select("[title^='Подробная статистика команды Mineski']") or b(
                        class_="team_showall_rows"):
                    MIN.append(item20.text.strip() + '\n\n')
                    MIN.append(re.findall(pattern, str(item20)))
                dann20 = '"'.join(str(e) for e in MIN)
                dann_three20 = dann20.split()
                vivod20 = ' '.join(dann_three20)
                if '"' in vivod20:
                    lens = len(vivod20)
                    kolvo = vivod20[101:]
                    two_team_fb = kolvo[2:6]
                    two_team_f10 = kolvo[10:14]
                    two_team_win = kolvo[18:22]
                    two_team_kill47 = kolvo[26:30]
                    two_team_min = kolvo[34:38]
                    print('FB =', two_team_fb + '%')
                    print('F10 =', two_team_f10 + '%')
                    print('WIN = ', two_team_win + '%')
                    print('Тотал килл больше 47 =', two_team_kill47 + '%')
                    print('Тотал больше 34м =', two_team_min + '%')
            elif two == 'OG':
                ################## OG ##################
                OG = []
                for item21 in b.select("[title^='Подробная статистика команды OG']") or b(
                        class_="team_showall_rows"):
                    OG.append(item21.text.strip() + '\n\n')
                    OG.append(re.findall(pattern, str(item21)))
                dann21 = '"'.join(str(e) for e in OG)
                dann_three21 = dann21.split()
                vivod21 = ' '.join(dann_three21)
                if '"' in vivod21:
                    lens = len(vivod21)
                    kolvo = vivod21[96:]
                    two_team_fb = kolvo[2:6]
                    two_team_f10 = kolvo[10:14]
                    two_team_win = kolvo[18:22]
                    two_team_kill47 = kolvo[26:30]
                    two_team_min = kolvo[34:38]
                    print('FB =', two_team_fb + '%')
                    print('F10 =', two_team_f10 + '%')
                    print('WIN = ', two_team_win + '%')
                    print('Тотал килл больше 47 =', two_team_kill47 + '%')
                    print('Тотал больше 34м =', two_team_min + '%')
            elif two == 'Newbee':
                ################## Newbee ##################
                NB = []
                for item22 in b.select("[title^='Подробная статистика команды Newbee']") or b(
                        class_="team_showall_rows"):
                    NB.append(item22.text.strip() + '\n\n')
                    NB.append(re.findall(pattern, str(item22)))
                dann22 = '"'.join(str(e) for e in NB)
                dann_three22 = dann22.split()
                vivod22 = ' '.join(dann_three22)
                if '"' in vivod22:
                    lens = len(vivod22)
                    kolvo = vivod22[238:]
                    two_team_fb = kolvo[2:6]
                    two_team_f10 = kolvo[10:14]
                    two_team_win = kolvo[18:22]
                    two_team_kill47 = kolvo[26:30]
                    two_team_min = kolvo[34:38]
                    print('FB =', two_team_fb + '%')
                    print('F10 =', two_team_f10 + '%')
                    print('WIN = ', two_team_win + '%')
                    print('Тотал килл больше 47 =', two_team_kill47 + '%')
                    print('Тотал больше 34м =', two_team_min + '%')
            elif two == 'Royal Never Give Up':
                ################## RNGU ##################
                RNGU = []
                for item23 in b.select("[title^='Подробная статистика команды Royal Never Give Up']") or b(
                        class_="team_showall_rows"):
                    RNGU.append(item23.text.strip() + '\n\n')
                    RNGU.append(re.findall(pattern, str(item23)))
                dann23 = '"'.join(str(e) for e in RNGU)
                dann_three23 = dann23.split()
                vivod23 = ' '.join(dann_three23)
                if '"' in vivod23:
                    lens = len(vivod23)
                    kolvo = vivod23[113:]
                    two_team_fb = kolvo[2:6]
                    two_team_f10 = kolvo[10:14]
                    two_team_win = kolvo[18:22]
                    two_team_kill47 = kolvo[26:30]
                    two_team_min = kolvo[34:38]
                    print('FB =', two_team_fb + '%')
                    print('F10 =', two_team_f10 + '%')
                    print('WIN = ', two_team_win + '%')
                    print('Тотал килл больше 47 =', two_team_kill47 + '%')
                    print('Тотал больше 34м =', two_team_min + '%')
            elif two == 'compLexity':
                ################## compLexity ##################
                COL = []
                for item24 in b.select("[title^='Подробная статистика команды compLexity']") or b(
                        class_="team_showall_rows"):
                    COL.append(item24.text.strip() + '\n\n')
                    COL.append(re.findall(pattern, str(item24)))
                dann24 = '"'.join(str(e) for e in COL)
                dann_three24 = dann24.split()
                vivod24 = ' '.join(dann_three24)
                if '"' in vivod24:
                    lens = len(vivod24)
                    kolvo = vivod24[104:]
                    two_team_fb = kolvo[2:6]
                    two_team_f10 = kolvo[10:14]
                    two_team_win = kolvo[18:22]
                    two_team_kill47 = kolvo[26:30]
                    two_team_min = kolvo[34:38]
                    print('FB =', two_team_fb + '%')
                    print('F10 =', two_team_f10 + '%')
                    print('WIN = ', two_team_win + '%')
                    print('Тотал килл больше 47 =', two_team_kill47 + '%')
                    print('Тотал больше 34м =', two_team_min + '%')
            elif two == 'Team Aster':
                ################## Team Aster ##################
                TAS = []
                for item25 in b.select("[title^='Подробная статистика команды Team Aster']") or b(
                        class_="team_showall_rows"):
                    TAS.append(item25.text.strip() + '\n\n')
                    TAS.append(re.findall(pattern, str(item25)))
                dann25 = '"'.join(str(e) for e in TAS)
                dann_three25 = dann25.split()
                vivod25 = ' '.join(dann_three25)
                if '"' in vivod25:
                    lens = len(vivod25)
                    kolvo = vivod25[98:]
                    two_team_fb = kolvo[2:6]
                    two_team_f10 = kolvo[10:14]
                    two_team_win = kolvo[18:22]
                    two_team_kill47 = kolvo[26:30]
                    two_team_min = kolvo[34:38]
                    print('FB =', two_team_fb + '%')
                    print('F10 =', two_team_f10 + '%')
                    print('WIN = ', two_team_win + '%')
                    print('Тотал килл больше 47 =', two_team_kill47 + '%')
                    print('Тотал больше 34м =', two_team_min + '%')
            elif two == 'Invictus Gaming':
                ################## Invictus Gaming ##################
                IG = []
                for item26 in b.select("[title^='Подробная статистика команды Invictus Gaming']") or b(
                        class_="team_showall_rows"):
                    IG.append(item26.text.strip() + '\n\n')
                    IG.append(re.findall(pattern, str(item26)))
                dann26 = '"'.join(str(e) for e in IG)
                dann_three26 = dann26.split()
                vivod26 = ' '.join(dann_three26)
                if '"' in vivod26:
                    lens = len(vivod26)
                    kolvo = vivod26[109:]
                    two_team_fb = kolvo[2:6]
                    two_team_f10 = kolvo[10:14]
                    two_team_win = kolvo[18:22]
                    two_team_kill47 = kolvo[26:30]
                    two_team_min = kolvo[34:38]
                    print('FB =', two_team_fb + '%')
                    print('F10 =', two_team_f10 + '%')
                    print('WIN = ', two_team_win + '%')
                    print('Тотал килл больше 47 =', two_team_kill47 + '%')
                    print('Тотал больше 34м =', two_team_min + '%')
            elif two == 'Winstrike':
                ################## Winstrike ##################
                WINS = []
                for item27 in b.select("[title^='Подробная статистика команды Winstrike']") or b(
                        class_="team_showall_rows"):
                    WINS.append(item27.text.strip() + '\n\n')
                    WINS.append(re.findall(pattern, str(item27)))
                dann27 = '"'.join(str(e) for e in WINS)
                dann_three27 = dann27.split()
                vivod27 = ' '.join(dann_three27)
                if '"' in vivod27:
                    lens = len(vivod27)
                    kolvo = vivod27[103:]
                    two_team_fb = kolvo[2:6]
                    two_team_f10 = kolvo[10:14]
                    two_team_win = kolvo[18:22]
                    two_team_kill47 = kolvo[26:30]
                    two_team_min = kolvo[34:38]
                    print('FB =', two_team_fb + '%')
                    print('F10 =', two_team_f10 + '%')
                    print('WIN = ', two_team_win + '%')
                    print('Тотал килл больше 47 =', two_team_kill47 + '%')
                    print('Тотал больше 34м =', two_team_min + '%')
            elif two == 'J Storm':
                ################## J Storm ##################
                JS = []
                for item28 in b.select("[title^='Подробная статистика команды J Storm']") or b(
                        class_="team_showall_rows"):
                    JS.append(item28.text.strip() + '\n\n')
                    JS.append(re.findall(pattern, str(item28)))
                dann28 = '"'.join(str(e) for e in JS)
                dann_three28 = dann28.split()
                vivod28 = ' '.join(dann_three28)
                if '"' in vivod28:
                    lens = len(vivod28)
                    kolvo = vivod28[96:]
                    two_team_fb = kolvo[2:6]
                    two_team_f10 = kolvo[10:14]
                    two_team_win = kolvo[18:22]
                    two_team_kill47 = kolvo[26:30]
                    two_team_min = kolvo[34:38]
                    print('FB =', two_team_fb + '%')
                    print('F10 =', two_team_f10 + '%')
                    print('WIN = ', two_team_win + '%')
                    print('Тотал килл больше 47 =', two_team_kill47 + '%')
                    print('Тотал больше 34м =', two_team_min + '%')
            elif two == 'Infamous':
                ################## Infamous ##################
                INF = []
                for item29 in b.select("[title^='Подробная статистика команды Infamous']") or b(
                        class_="team_showall_rows"):
                    INF.append(item29.text.strip() + '\n\n')
                    INF.append(re.findall(pattern, str(item29)))
                dann29 = '"'.join(str(e) for e in INF)
                dann_three29 = dann29.split()
                vivod29 = ' '.join(dann_three29)
                if '"' in vivod29:
                    lens = len(vivod29)
                    kolvo = vivod29[98:]
                    two_team_fb = kolvo[2:6]
                    two_team_f10 = kolvo[10:14]
                    two_team_win = kolvo[18:22]
                    two_team_kill47 = kolvo[26:30]
                    two_team_min = kolvo[34:38]
                    print('FB =', two_team_fb + '%')
                    print('F10 =', two_team_f10 + '%')
                    print('WIN = ', two_team_win + '%')
                    print('Тотал килл больше 47 =', two_team_kill47 + '%')
                    print('Тотал больше 34м =', two_team_min + '%')


import statistics
one_kill = ''.join(one_team_kill47)
two_kill = ''.join(two_team_kill47)
total_kills = [one_kill, two_kill]
total_kills = list(map(float, total_kills))

one_FB = ''.join(one_team_kill47)
two_FB = ''.join(two_team_kill47)
total_killsfb = [one_kill, two_kill]
total_killsfb = list(map(float, total_killsfb))

one_min = ''.join(one_team_min)
two_min = ''.join(two_team_min)
total_min = [one_min, two_min]
total_min = list(map(float, total_min))

print('\n')

kill_vivod = statistics.mean(total_kills)
min_vivod = statistics.mean(total_min)

print('*********************************************')

if kill_vivod > 50 and kill_vivod < 60:
    print('В последних играх среднее кол-во убийст доходящих 47+ киллов', kill_vivod, '%')
if kill_vivod < 50:
    print('В последних играх обе команды делают 47 килов с, ', kill_vivod, 'процентом проходимости. ')
if kill_vivod > 60:
     print('Ставь тотал больше 47 киллов.', kill_vivod,'%')

print('*********************************************')

if min_vivod > 50 and min_vivod < 60:
    print('Тотал времени. Риск. Проходимость', min_vivod, '%')
if min_vivod < 50:
    print('Ставь меньше 34 минут. Ведь проходимость', min_vivod,'%')
if min_vivod > 60:
    print('Смело ставь больше 34 минут. Проходимость', min_vivod,'%')

print('*********************************************')

if one_team_win > two_team_win:
    print('Победа 1 команды, c', one_team_win,' процентом')
else:
    print('Победа 2 команды, с', two_team_win,' процентом')

print('*********************************************')

if one_team_f10 > two_team_f10:
    print('Первая команда сделает первые 10 убийств с процентом', one_team_f10)
else:
    print('Вторая команда сделает первые 10 убийств с процентом', two_team_f10)

print('*********************************************')

print('Среднее кол-во больше 47 убийств 1 команды:',one_team_kill47,'\n','Среднее кол-во больше 47 убийств 2 команды:',two_team_kill47)
print('Среднее кол-во игр где было больше 34 минуты 1 команды:',one_team_min,'\n','Среднее кол-во игр где было больше 34 минуты 2 команды::',two_team_min)

print('*********************************************')

