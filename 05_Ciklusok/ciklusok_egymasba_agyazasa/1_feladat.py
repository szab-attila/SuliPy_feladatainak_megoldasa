print('1. Feladat - Pocak')
print('\nKészíts egy programot, amely a felhasználótól bekér egy páros számot, \nmajd ennek megfelelően rajzol ki a '
      'képernyőre egy pocak szerű alakzatot az alábbiak szerint!\n')

bekert_szam = int(input('Írj be egy páros számot: '))
print()

sor = 1
while sor <= bekert_szam / 2:
    oszlop = 1
    while oszlop <= sor:
        print('0 ', end='')
        oszlop += 1
    print()
    sor += 1
    
while sor >= 1:
    oszlop = 1
    while oszlop < sor:
        print('0 ', end='')
        oszlop += 1
    print()
    sor -= 1
    