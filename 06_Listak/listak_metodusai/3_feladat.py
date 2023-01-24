print('3. Feladat')
print('\nÍrj egy programot, amely a felhasználótól betűket kér be mindaddig, amíg az nem ad meg szót, csupán egy ENTER-t üt!')
print('\nA program vizsgálja meg a megadott betűt, és tárolja el egy listában, ha az még nem szerepel benne\n(a felhasználó korábban még nem adta meg)! A program NE különböztesse meg a kis- és nagybetűket egymástól,\nde olyan formában tárolja el a betűket mindig, ahogy a felhasználó megadta.')
print('\nHa a megadott betű már szerepel a listában írja ki, a képernyőre, hogy "Ezt a betűt már rögzítettem."!')
print('\nMinden egyes adatbekérés után írja ki a már rögzített betűket ábécé sorrendben (elöl a nagybetűk, utána a kisbetűk ábécé sorrendben)!')


characters = []

print()
while True:
    character = input('\nGive me letters: ')
    print()
    if character == '':
        print('Bye bye!')
        break
    elif character not in characters:
        characters.append(character)
    elif character in characters:
        print('Ezt a betűt már rögzítettem.\n')
    #print(characters)
    characters.sort()
    for item in characters:
        print(item, end=' ')

    
        