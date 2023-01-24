print('Extra feladat')
print('\nKészíts egy programot, amely kiszámítja a felhasználó által megadott szám faktoriálisát!\nA program '
      'természetesen csak értelmezhető számokat fogadjon el bemenetként, és helyesen értelmezze 0 és 1 faktoriálisát '
      'is!')

szam = int(input('\nAdd meg a számot, aminek szeretnéd kiszámolni a faktoriálisát: '))
faktorial = 1

if szam == 0 or szam == 1:
    print('1')
else:
    for i in range(1, szam+1):
        faktorial = faktorial * i
    print(faktorial)


