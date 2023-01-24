import random

print('3. Feladat')
print('\nA program generáljon 10 darab véletlenszámot [0;50] intervallumon, de csak a 4-gyel oszthatóakat rögzítse egy listában.\nA végén jelenítse meg a listát a képernyőn, és írja ki azt is, hány elemből áll a lista.')

counter = 1
numbers = []

while counter <= 10:
    number = random.randint(0, 50)
    if number % 4 == 0:
        numbers.append(number)
    counter += 1

print(f'\nA néggyel osztható számok listája: {numbers}, összesen {len(numbers)} db.')