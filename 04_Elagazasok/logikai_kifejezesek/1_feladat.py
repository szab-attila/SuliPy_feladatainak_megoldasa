print('1. Feladat')
print('Készíts egy programot, amely a felhasználótól bekér egy egész számot, majd megvizsgálja, hogy a megadott szám\n- pozitív páros vagy\n- negatív páratlan.\nAz eredményről tájékoztatja a felhasználót.')

szam = int(input('\nAdj meg egy egész számot: '))

if szam % 2 == 0 and szam > 0:
    print('\nA megadott szám pozitív páros szám.')
elif szam % 2 != 0 and szam < 0:
    print('\nA megadott szám negatív páratlan szám.')
else:
    print('\nA megadott szám egyik kritériumnak sem felel meg.')