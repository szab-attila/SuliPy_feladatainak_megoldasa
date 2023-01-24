print('2.1 Feladat')
print('\nAz adott lista (amely a '"Próbáld ki!"' gombra kattintva elérhető) elemei közül \na program kiírja a "t" és "T" betűkkel kezdődőeket!')

szavak = ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python']

print()
for szo in szavak:
    if szo[0] == 't' or szo[0] == 'T':
        print(szo, end=', ')