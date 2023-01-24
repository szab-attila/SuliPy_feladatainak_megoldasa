print('1.2 Feladat')
print('\nFejleszd tovább úgy az előző programot, hogy a 3. név megadása után tájékoztassa a program a felhasználót, hogy már nincs lehetősége újabb adat bevitelére, írja ki az addig megadott neveket, és lépjen ki.\n')

nevek = []

while True:
    nev = input('Adj meg egy nevet: ')
    nevek.append(nev)
    formazott = [x for x in nevek]
    if nev == '':
        print(f'\nA nevek: {formazott}\nViszlát!')
        break
    elif len(nevek) > 2:
        print(f'\nNincs több lehetőség újabb adat bevitelére.\nA nevek: {formazott}\nViszlát!')
        print(f'')
        break 
    


    
