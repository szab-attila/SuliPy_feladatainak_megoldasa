import random

print('1.2 Feladat')
print('\nMódosítsd úgy a fenti programot, hogy a program csak a páros számokat adja össze!')


szamlalo = 1
lista = []

print()
while szamlalo <= 5:
    szam = random.randint(1, 10)
    lista.append(szam)
    szamlalo += 1

osszeg = 0

for szam in lista:
    if szam % 2 == 0:
        osszeg += szam

print(f'A lista elemei: {lista}, összegük: {osszeg}.')