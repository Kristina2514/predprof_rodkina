
f = [''.join(i) for i in open('game.txt', encoding='utf-8')]
'''
Создаем предварительный список из значений каждой строки считанного файла, чтобы в далнейшем,
как указано в условии, разделить
каждые значения в строке файла по знаку $
'''
s = []
'''
Создаем тот самый список, в который будем записывать уже разделенные строки и превращенные в списки
'''
dikt = {}
'''
Заводим словарь, через который и будем изменять все нужные нам значения в определнном столбце
(в данном случае столбец nameError)
'''
for i in f:
    '''Перебираем в списке строки в списке f и разделяем каждую строку по знаку $'''
    i = i.split('$')
    s.append(i)
'''
Создаем ключи словаря, в котором будут определенные списки значений 
'''
dikt['GameName'] = []
dikt['characters'] = []
dikt['nameError'] = []
dikt['date'] = []

'''
Проходимся по длине всего списка s, при этом вычитаем 1 из длины, поскольку первая строка это название столбцов
каждого из значений. Соответственно первый индекс означает то, в какой строке мы забираем значение, а второй означает 
то, в какой столбце берем значение.
'''
for i in range(len(s) - 1):
    dikt['GameName'].append(s[i+1][0])
    dikt['characters'].append(s[i+1][1])
    dikt['nameError'].append(s[i+1][2])
    dikt['date'].append(s[i+1][3])

'''
Проходимся по элементам в словаре в стобце 'nameError' и если находим в ошибке число 55, сразу же узнаем 
индекс в словаре данной ошщибки и изменяем ее на Done, время ставим '0000-00-00' так же по этому индексу
'''
for err in dikt['nameError']:
    if '55' in err:
        el = dikt['nameError'].index(err)
        print(f'У персонажа {dikt["characters"][el]} нашлась ошибка с кодом {dikt["nameError"][el]}. Дата фиксации: '
              f'{dikt["date"][el]}.')

        dikt['nameError'][el] = dikt['nameError'][el].replace(dikt['nameError'][el], 'Done')
        dikt['date'][el] = dikt['date'][el].replace(dikt['date'][el], '0000-00-00')














