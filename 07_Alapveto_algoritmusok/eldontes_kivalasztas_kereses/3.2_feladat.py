print('3.2 Feladat')
print(
    '\nLegyen annyiban személyreszabható a játék, hogy a játékos határozhassa meg a négyzetalakú játéktér oldalhosszát!')

import random

ABC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
abc_lista = []
szamok = [szam for szam in range(1, 10)]

proba = 1
tippek = []

jatekter = int(input('Add meg a négyzetalakú játéktér oldalhosszát(max 9x9): '))

szamlalo = 0

for i in ABC:
    abc_lista.append(i)
    szamlalo += 1
    if szamlalo == jatekter:
        break

hajo_oszlop = random.choice(abc_lista)
hajo_sor = random.randint(1, jatekter)
index = 0
index2 = 0

while True:
    sor = 0
    print('\n!!!TORPEDÓ!!!\n')
    print(hajo_oszlop, hajo_sor)
    if proba > 1:
        rossz_tippek = ', '.join(tippek)
        print(f'Eddigi próbálkozások: {rossz_tippek}\n')
    while sor <= jatekter:
        oszlop = 0
        while oszlop <= jatekter:
            if sor == 0 and oszlop > 0:
                while index < jatekter:
                    print(f'{abc_lista[index]} ', end='')
                    index += 1
                    break
            elif sor > 0 and oszlop == 0:
                while index2 < jatekter:
                    print(f'{szamok[index2]} ', end='')
                    index2 += 1
                    break
            elif sor == 0 and oszlop == 0:
                print('  ', end='')
            else:
                print('. ', end='')
            oszlop += 1
        print()
        sor += 1

    felh_tipp = input('\nTaláld ki a hajó pozícióját (Pl: B2): ')
    felh_tipp = felh_tipp.upper()

    talalat = False
    index3 = 0

    while index3 < len(abc_lista) and not talalat:
        if abc_lista[index3] == felh_tipp[0]:
            if felh_tipp[0] == hajo_oszlop:
                talalat = True
        index3 += 1

    index = 0
    index2 = 0
    if talalat and felh_tipp[1] == str(hajo_sor):

        sor = 0
        print('\n!!!TORPEDÓ!!!\n')
        while sor <= jatekter:
            oszlop = 0
            while oszlop <= jatekter:
                if sor == 0 and oszlop == 0:
                    print('  ', end='')
                elif sor == 0 and oszlop > 0:
                    while index < jatekter:
                        print(f'{abc_lista[index]} ', end='')
                        index += 1
                        break
                elif sor > 0 and oszlop == 0:
                    while index2 < jatekter:
                        print(f'{szamok[index2]} ', end='')
                        index2 += 1
                        break
                elif oszlop == index3 and sor == hajo_sor:
                    print('X ', end='')
                else:
                    print('. ', end='')
                oszlop += 1
            print()
            sor += 1
        print(f'\nGRATULÁLOK!\n{proba} próbálkozásból elsüllyesztetted a hajót!')
        break
    else:
        tippek.append(felh_tipp)
        print('\nNem talált. Próbáld meg mégegyszer!')
        proba += 1





