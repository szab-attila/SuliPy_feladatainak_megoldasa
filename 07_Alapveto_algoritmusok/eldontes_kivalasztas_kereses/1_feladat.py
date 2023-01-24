import random

print('1. Feladat')
print('\nÍrj egy programot, amely 5 darab véletlenszámot generál [1;7] intervallumon, és ezeket eltárolja egy listában.\nKérjen be a felhasználótól egy számot, és vizsgálja meg, hogy ez előfordul-e a listában!\nAz eredményről tájékoztassa a felhasználót, és írja ki a lista elemeit a képernyőre!')

counter = 1
numbers = []

while counter <= 5:
    n = random.randint(1, 8)
    numbers.append(n)
    counter += 1

user_n = int(input('\nAdj meg egy számot: '))

index = 0
talalat = False

while index <= len(numbers):
    if numbers[index-1] == user_n:
        talalat = True
    index += 1

if talalat:
    print('\nA megadott szám benne van a listában.')
else:
    print('\nA megadott szám nincs a listában.')


print(f'A lista elemei: {numbers}')













# is_included = 0
#
# for i in numbers:
#     if i == user_n:
#         is_included += 1
#
# if is_included > 0:
#     print('\nA megadott szám benne van a listában.')
# else:
#     print('\nA megadott szám nincs a listában.')

# print(f'A lista elemei: {numbers}')

#EZT HOLNAP UJRA KELL CSINALNOM!!!
