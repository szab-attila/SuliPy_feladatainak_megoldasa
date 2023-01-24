print('2.1 Feladat')
print('\nA program számolja össze, hogy hány darab "A" vagy "a" betűvel kezdődő szó van az adott listában (amely a '
      '"Próbáld ki!" gombra kattintva elérhető)! \nA képernyőre írja is ki a feltételnek megfelelő szavakat!')

szavak = ['alma', 'barack', 'Attila', 'kávé', 'szekrény', 'asztal']
keresett_szavak = []

darab = 0
for szo in szavak:
    if szo[0] == 'A' or szo[0] == 'a':
        keresett_szavak.append(szo)
        darab += 1

print(f'\nA listában {darab} db "A" vagy "a" betűvel kezdődő szó van.\nEzek a szavak: {keresett_szavak}')



