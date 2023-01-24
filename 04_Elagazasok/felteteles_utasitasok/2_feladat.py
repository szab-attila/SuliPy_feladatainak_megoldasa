print('2. Feladat')
print('\nKészíts egy programot, ami bekér egy számot a felhasználótól,\nmajd kiírja, hogy a megadott szám páros-e vagy páratlan!')


szam = int(input('\nAdj meg egy számot: '))

if szam % 2 == 0:
    print('\nA megadott szám páros!')
else:
    print('\nA megadott szám páratlan!')