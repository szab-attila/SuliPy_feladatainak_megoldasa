print('1.2 Feladat')
print('\nAlakítsd át úgy az előbbi programot, hogy az "X" vagy "x" megadása eredményezze az adatbekérés végét!')

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
        if szam < szam_min:
            szam_min = szam
        if szam > szam_max:
            szam_max = szam

print(f'\nA lista elemei: {szamok}.\nA legkisebb szám: {szam_min}, a legnagyobb szám: {szam_max}.')
