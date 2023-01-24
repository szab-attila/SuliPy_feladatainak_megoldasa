import random
print('6. Feladat')
print('\nÍrj egy programot, amely [1;12] intervallumon állít elő 20 darab véletlenszámot! \nA képernyőre kizárólag csak a 3-mal oszthatóakat írja ki, és a végén informálja a felhasználót arról is, hány darab ilyen szám volt.')

szamlalo = 1
szamok = []
harommal_oszthato = []

while szamlalo <= 20:
    veletlen_szam = random.randint(1, 12)
    szamok.append(veletlen_szam)
    szamlalo += 1

for szam in szamok:
    if szam % 3 == 0:
        harommal_oszthato.append(szam)

print()
print(szamok)
print(f'\nA hárommal osztható számok: {harommal_oszthato}, összesen {len(harommal_oszthato)} db.')