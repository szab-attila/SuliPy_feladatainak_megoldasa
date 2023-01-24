print('1.2 Feladat')
print('\nAlakítsuk át az előbbi programot úgy, hogy a program arról adjon tájékoztatást,\nhogy pontosan hányszor szerepel a felhasználó által megadott szín a listában!\nHa a megadott szín nincs még tárolva, továbbra is a "A megadott szín nem szerepel a listában." szöveg jelenjen meg!')

palette = ['kék', 'piros', 'fehér', 'fekete', 'zöld', 'sárga', 'barna', 'piros', 'fehér', 'szürke']

user_color = input('\nAdj meg egy színt: ')
counter = 0

if user_color not in palette:
    print('A megadott szín nem szerepel a listában.')
else:
    for color in palette:
        if color == user_color:
            counter += 1
    print(f'A megadott szín {counter} alkalommal szerepel a listában.')

print('\nA lista színei:')
for colors in palette:
    print(colors, end=', ')
