import random

print('3.1 Feladat')
print(
    '\nTorpedó játék egyszerűsített változata. A játéktér legyen egy 3x3-as négyzetalakú rács, amiben az oszlopokat '
    'betűk (A, B, C),\na sorokat számok (1, 2, 3) jelölik.A program helyezzen el egy darab egy egység kiterjedésű '
    'hajót a játéktérben véletlenszerűen (Pl: B2).\nA játékos próbálja meg kitalálni a hajó pozícióját újabb és újabb '
    'tippek megadásával.\nA játék végén a program azt is írja ki a képernyőre, hogy hány próbálkozásból tudta a '
    'játékos kitalálni a pozíciót!')

proba = 1
hajo_oszlop = random.randint(1, 3)
hajo_sor = random.randint(1, 3)
tippek = []



while True:
    sor = 0
    print('\n!!!TORPEDÓ!!!\n')
    if proba > 1:
        rossz_tippek = ', '.join(tippek)
        print(f'Eddigi próbálkozások: {rossz_tippek}\n')
    while sor <= 3:
        oszlop = 0
        while oszlop <= 3:
            if sor == 0 and oszlop > 0:
                if oszlop == 1:
                    print('A ', end='')
                elif oszlop == 2:
                    print('B ', end='')
                elif oszlop == 3:
                    print('C ', end='')
            elif sor > 0 and oszlop == 0:
                if sor == 1:
                    print('1 ', end='')
                elif sor == 2:
                    print('2 ', end='')
                elif sor == 3:
                    print('3 ', end='')
            elif sor == 0 and oszlop == 0:
                print('  ', end='')
            else:
                print('. ', end='')
            oszlop += 1
        print()
        sor += 1

    felh_tipp2 = input('\nTaláld ki a hajó pozícióját (Pl: B2): ')
    felh_tipp = felh_tipp2

    if felh_tipp == 'A1' or felh_tipp == 'a1':
        felh_tipp = hajo_sor == 1 and hajo_oszlop == 1
    elif felh_tipp == 'A2' or felh_tipp == 'a2':
        felh_tipp = hajo_sor == 2 and hajo_oszlop == 1
    elif felh_tipp == 'A3' or felh_tipp == 'a3':
        felh_tipp = hajo_sor == 3 and hajo_oszlop == 1
    elif felh_tipp == 'B1' or felh_tipp == 'b1':
        felh_tipp = hajo_sor == 1 and hajo_oszlop == 2
    elif felh_tipp == 'B2' or felh_tipp == 'b2':
        felh_tipp = hajo_sor == 2 and hajo_oszlop == 2
    elif felh_tipp == 'B3' or felh_tipp == 'b3':
        felh_tipp = hajo_sor == 3 and hajo_oszlop == 2
    elif felh_tipp == 'C1' or felh_tipp == 'c1':
        felh_tipp = hajo_sor == 1 and hajo_oszlop == 3
    elif felh_tipp == 'C2' or felh_tipp == 'c2':
        felh_tipp = hajo_sor == 2 and hajo_oszlop == 3
    elif felh_tipp == 'C3' or felh_tipp == 'c3':
        felh_tipp = hajo_sor == 3 and hajo_oszlop == 3
    else:
        continue

    if felh_tipp:
        sor = 0
        print('\n!!!GRATULÁLOK!!!\n')
        while sor <= 3:
            oszlop = 0
            while oszlop <= 3:
                if sor == hajo_sor and oszlop == hajo_oszlop:
                    print('X ', end='')
                elif sor == 0 and oszlop > 0:
                    if oszlop == 1:
                        print('A ', end='')
                    elif oszlop == 2:
                        print('B ', end='')
                    elif oszlop == 3:
                        print('C ', end='')
                elif sor > 0 and oszlop == 0:
                    if sor == 1:
                        print('1 ', end='')
                    elif sor == 2:
                        print('2 ', end='')
                    elif sor == 3:
                        print('3 ', end='')
                elif sor == 0 and oszlop == 0:
                    print('  ', end='')
                else:
                    print('. ', end='')
                oszlop += 1
            print()
            sor += 1
        print(f'\n{proba} próbálkozásból elsüllyesztetted a hajót!')
        break
    else:
        tippek.append(felh_tipp2)
        print('\nNem talált. Próbáld meg mégegyszer!')
        proba += 1
