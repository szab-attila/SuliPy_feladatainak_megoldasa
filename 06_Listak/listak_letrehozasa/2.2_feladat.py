print('2.2 Feladat')
print('\nAlakítsd át úgy az előző porgramot, hogy az ne csak kis, \nhanem a nagy "A" betűvel kezdődő szavakat is elfogadja.')

szavak = []

while True:
    print('\nA kilépéshez nyomj ENTER-t!')
    szo = input('Adj meg "a" betűvel kezdődő szavakat: ')
    if szo == '':
        print('\nViszlát!')
        break
    if szo[0] == 'a' or szo[0] == 'A':
        print('')
        szavak.append(szo)
        print(szavak)
    else:
        print('\nA program csak "a" betűvel kezdődő szavakat tárol el.')