import csv
import string
import random

f = [''.join(i) for i in open('game.txt', encoding='utf-8')]
s = []
dikt = {}
k = 1
for i in f:
    i = i.split('$')
    s.append(i)
dikt['GameName'] = []
dikt['characters'] = []
dikt['nameError'] = []
dikt['date'] = []
for i in range(len(s) - 1):
    dikt['GameName'].append(s[k][0])
    dikt['characters'].append(s[k][1])
    dikt['nameError'].append(s[k][2])
    dikt['date'].append(s[k][3])
    k += 1

for err in dikt['nameError']:
    if '55' in err:
        el = dikt['nameError'].index(err)
        print(f'У персонажа {dikt["characters"][el]} нашлась ошибка с кодом {dikt["nameError"][el]}. Дата фиксации: '
              f'{dikt["date"][el]}.')
        dikt['nameError'][el] = dikt['nameError'][el].replace(dikt['nameError'][el], 'Done')
        dikt['date'][el] = dikt['date'][el].replace(dikt['date'][el], '0000-00-00')















