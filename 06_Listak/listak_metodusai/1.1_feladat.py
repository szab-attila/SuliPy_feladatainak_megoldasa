print('1.1 Feladat')
print('\nA program tároljon egy listában színeket. Kérjen be a felhasználótól egy színt, és állapítsa meg,\nhogy a megadott szín már szerepel-e az adott listában. A vizsgálat eredményéről tájékoztassa a program a felhasználót,\nés írja ki egymás mellé vesszővel elválasztva a lista által tartalmazott színeket!')

paletta = ['kék', 'piros', 'fehér', 'fekete', 'zöld', 'sárga', 'barna', 'piros', 'fehér', 'szürke']

szin = input('\nAdj meg egy színt: ')

if szin in paletta:
    print('A szín szerepel a listában.')
else:
    print('A szín nem szerepel a listában.')


print('\nA lista színei:')
for szinek in paletta:
    print(szinek, end=', ')

