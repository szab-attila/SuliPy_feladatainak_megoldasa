import random
print('1. Feladat')
print('\nKészíts egy programot, amely [1;10] intervallumon generál 5 darab véletlen egész számot és ezeket tárolja el '
      'egy listában!\nA program számolja össze, és képernyőre írja ki a listában tárolt páros számok számát, '
      'valamint a lista elemeit!')


szamlalo = 0
szamok = []
while szamlalo < 5:
    szam = random.randint(1,10)
    szamok.append(szam)
    szamlalo += 1

darab = 0
for szam in szamok:
    if szam % 2 == 0:
        darab += 1

print(f'\nA lista elemei: {szamok}.\nA listában lévő páros számok száma: {darab} db.')
