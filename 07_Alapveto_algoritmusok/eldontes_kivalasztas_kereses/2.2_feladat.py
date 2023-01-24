print('2.2 Feladat')
print('\nA program tároljon el egy szót egy változóban. A felhasználó adjon meg egy betűt, amiről a program döntse '
      'el,\nhogy előfordul-e a szóban! Az eredményről tájékoztassa a felhasználót, és írja ki a tárolt szót is!')

word = 'anyagtakarékosság'
letter = input('\nAdd meg a keresett betűt: ')

match = False
index = 0

while index < len(word):
    if word[index] == letter:
        match = True
    index += 1

print(f'\nA szó: {word}')
if match:
    print('A keresett betű benne van a szóban.')
else:
    print('A keresett betű nincs benne a szóban.')



