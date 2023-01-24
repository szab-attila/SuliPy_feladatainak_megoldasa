print('1.3 Feladat')
print('\nAlakítsd át úgy az előbbi programot, hogy a legkisebb és legnagyobb páros számot határozza meg!')

szamok = []
print()
while True:
    szam = input('Adj meg számokat: ')
    if szam == 'x' or szam == 'X':
        break

    szam = int(szam)
    szamok.append(szam)

    szam_min = szamok[0]
    szam_max = szamok[0]
    for szam in szamok:
        if szam < szam_min and szam % 2 == 0:
            szam_min = szam
        if szam > szam_max and szam % 2 == 0:
            szam_max = szam

print(f'\nA lista elemei: {szamok}.\nA legkisebb páros szám: {szam_min}, a legnagyobb páros szám: {szam_max}.')

