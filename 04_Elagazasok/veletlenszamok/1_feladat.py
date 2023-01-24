import random

print('1. Feladat')
print('\nKészíts egy rövid programot, amely 1 és 3 között generál véletlenszámot,\nmajd összehasonlítja ezt a felhasználó által megadott, szintén ebbe a tartományba eső számmal!\nAz összehasonlítás eredményéről tájékoztassa a felhasználót!')

gep_szama = random.randint(1, 3)
szam = int(input('\nAdj meg egy számot 1 és 3 között: '))


if szam < 1 or szam > 3:
    print('Nem a megadott intervallumon belül adtad meg a számot.')
elif gep_szama == szam:
    print('A két szám megegyezik.')
else:
    print(f'A gép száma: {gep_szama}.\nSajnos nem egyezik az általad megadott számmal.')

