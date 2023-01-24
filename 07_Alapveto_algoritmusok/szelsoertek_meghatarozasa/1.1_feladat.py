print('1.1 Feladat')
print('\nKészíts egy programot, amely a felhasználótól számokat kér be mindaddig, amíg az csupán ENTER-t nem üt!\nA '
      'számokat tárolja el a program egy listában! Az adatbekérés befejezte után írja ki a program a lista elemeit, '
      'a legkisebb és a legnagyobb számot!')

szamok = []
print()
while True:
    szam = input('Adj meg számokat: ')
    if szam == '':
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
