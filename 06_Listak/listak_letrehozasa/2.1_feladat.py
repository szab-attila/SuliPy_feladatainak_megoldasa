print('2.1 Feladat')
print('\nKészíts egy programot, amely a felhasználótól kis "a" betűvel kezdődő szavakat kér be és ezeket tárolja. Ha a felhasználó nem "a" betűvel kezdődő szót ad meg, akkor azt hagyja figyelmen kívül és ne tárolja. \nA bekérés egészen addig folytatódjon, amíg a felhasználó ENTER-t nem üt (nem ad meg újabb nevet a bekérésnél)! A program a bekért neveket írja ki a képernyőre!')
print('A program tájékoztatássa a felhasználót a működéséről, és az elvárt adatokról!')

szavak = []

while True:
    print('\nA kilépéshez nyomj ENTER-t!')
    szo = input('Adj meg "a" betűvel kezdődő szavakat: ')
    if szo == '':
        print('\nViszlát!')
        break
    if szo[0] == 'a':
        print('')
        szavak.append(szo)
        print(szavak)
    else:
        print('\nA program csak "a" betűvel kezdődő szavakat tárol el.')
        

    
    
