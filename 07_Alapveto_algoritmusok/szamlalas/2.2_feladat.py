print('2.2 Feladat')
print('\nA program számolja össze, hogy hány darab "E" vagy "e" betűt tartalmazó szó van az adott listában (amely a '
      '"Próbáld ki!" gombra kattintva elérhető)!\nA képernyőre írja is ki a feltételnek megfelelő szavakat!')

szavak = ['Elemér', 'Emma', 'ajtó', 'róka', 'egér']
keresett_szavak = []

darab = 0
for szo in szavak:
    formazott_szo = szo.upper()
    if 'E' in formazott_szo:
        keresett_szavak.append(szo)
        talalat = True
        darab += 1


print(f'\nA listában {darab} db "E" vagy "e" betűt tartalmazó szó van.\nEzek a szavak: {keresett_szavak}')