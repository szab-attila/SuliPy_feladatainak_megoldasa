import random

print('2. Feladat')
print('\nA program generáljon 10 darab véletlenszámot [1;3] intervallumon, ezeket tárolja egy listában,\na lista tartalmát írja ki a képernyőre! A felhasználónak legyen lehetősége megadni egy számot [1;3] intervallumon,\nés a program törölje ennek a számnak valamennyi előfordulását a listából, majd írja ki a módosított listát a képernyőre!')


numbers_list = []
counter = 1

print('')
while counter <= 10:
    rand_number = random.randint(1, 3)
    numbers_list.append(rand_number)
    counter += 1
    
print(numbers_list)

user_number = int(input('\nAdj meg egy számot 1 és 3 között: '))

numbers_list_copy = numbers_list.copy()
for number in numbers_list_copy:
    if number == user_number:
        while number in numbers_list_copy:
            numbers_list_copy.remove(number)

print(numbers_list_copy)








