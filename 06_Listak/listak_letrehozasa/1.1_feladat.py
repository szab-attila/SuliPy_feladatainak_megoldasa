print('1.1 Feladat')
print('\nKészíts egy programot, amely a felhasználótól keresztneveket kér be egészen addig, amíg az ENTER-t nem üt (nem ad meg újabb nevet a bekérésnél)! A program a bekért neveket írja ki a képernyőre!\n')


nevek = []

while True:
    nev = input('Adj meg egy nevet: ')
    if nev == '':
        break 
    nevek.append(nev)

print()
for nev in nevek:
    print(nev, end=' ')
    
print('\nViszlát!')

