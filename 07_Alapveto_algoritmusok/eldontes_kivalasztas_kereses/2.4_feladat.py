print('2.4 Feladat')
print('\nFejlesszük tovább a 2.3 programot úgy, hogy a program egy listában tároljon öt darab szót, '
      'és abból véletlenszerűen válasszon egyet, aminek kapcsán a felhasználó megpróbálja kitalálni a betűit.')

import random

print('2.3 Feladat')
print(
    '\nFejlesszük tovább a 2.2 programot úgy, hogy a felhasználónak többször is legyen lehetősége újabb tippet '
    'megadnia.\nA bekérés addig folytatódjon, amíg a felhasználó nem ad meg betűt, csupán egy ENTER-t üt!')
print(
    '\nIgyekezz minél felhasználóbarátabbá tenni a programot! A programnak lehetnek egyéb hasznos funkciói,'
    '\npéldául gyűjtheti és kiírhatja a jó és a rossz tippeket (betűket).')

words = ['hosszúhajtás', 'okosak', 'expozé',  'özvegy', 'szerencselovag']
word = random.choice(words)
good_tip = []
bad_tip = []

while True:
    index = 0
    match = False
    print('\nA kilépéshez nyomj egy ENTER-t.')
    tip = input('Adj meg egy betűt: ')
    if tip == '':
        print(f'\nA keresett szó a(z) "{word}" volt.\nViszlát!')
        break

    while index < len(word) and not match:
        if word[index] == tip:
            good_tip.append(tip)
            print(f'\nA keresett betű benne van a szóban. \nJó tippek: {good_tip}')
            match = True
        index += 1

    if match is False:
        bad_tip.append(tip)
        print(f'\nA keresett betű nincs benne a szóban. \nRossz tippek: {bad_tip}')




