import random

print('1.1 Feladat')
print('\nKészíts egy programot, amely [1;10] intervallumon generál 5 darab véletlen egész számot, és ezeket tárolja el egy listában!\nA program adja össze a lista elemeit, írja ki a képernyőre az összegüket és a lista elemeit!')

szamlalo = 1
lista = []

print()
while szamlalo <= 5:
    szam = random.randint(1, 10)
    lista.append(szam)
    szamlalo += 1

osszeg = 0

for szam in lista:
    osszeg += szam

print(f'A lista elemei: {lista}, összegük: {osszeg}.')
