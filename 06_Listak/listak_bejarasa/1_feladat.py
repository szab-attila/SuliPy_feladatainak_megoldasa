print('1. Feladat')
print('Készíts egy programot, amely [1; 40] intervallumon kiírja a 3-mal osztható számokat!')

print()
for szam in range(1, 40):
    if szam % 3 == 0:
        print(szam, end=', ')
