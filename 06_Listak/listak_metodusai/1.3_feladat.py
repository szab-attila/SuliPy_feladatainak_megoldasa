print('1.3 Feladat')
print('\nEgészítsük ki az előbbi programot úgy, hogy a kiértékelést követően a felhasználó által\nmegadott szín kerüljön felvételre a listába, és csak ezután történjen meg a lista tartalmának kiírása!')

palette = ['kék', 'piros', 'fehér', 'fekete', 'zöld', 'sárga', 'barna', 'piros', 'fehér', 'szürke']

user_color = input('\nAdj meg egy színt: ')
counter = 0

if user_color not in palette:
    print('A megadott szín nem szerepel a listában.')
    palette.append(user_color)
else:
    palette.append(user_color)
    for color in palette:
        if color == user_color:
            counter += 1
    print(f'A megadott szín {counter} alkalommal szerepel a listában.')
    
print('\nA lista színei:')
for colors in palette:
    print(colors, end=', ')
