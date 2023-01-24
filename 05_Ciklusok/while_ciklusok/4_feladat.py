print('4. Feladat')
print('\nÍrj egy programot, amely a felhasználó által meghatározott alkalommal írja ki a bekért szöveget!')

bekert_szoveg = input('\nMit írjak ki? ')
hanyszor = int(input('Hányszor írjam ki? '))
print()


szamlalo = 1

while szamlalo <= hanyszor:
    print(bekert_szoveg)
    szamlalo += 1