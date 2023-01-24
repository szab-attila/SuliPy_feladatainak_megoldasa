print('3. Feladat')
print('\nÍrj egy programot, amely kiírja a páratlan számokat csökkenő sorrendben 1 és 10 között!\n')

szamlalo = 10

while szamlalo > 0:
    if szamlalo % 2 != 0:
        print(szamlalo)
    szamlalo -= 1