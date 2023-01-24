print('3. Feladat')
print('\nKészíts egy programot! A gép "gondol" egy számra 1 és 5 között,\nvagyis egy változóban tárolj egy ilyen számot! Azután a program\nbekér egy számot a felhasználótól, majd kiírja, hogy ez a szám\negyenlő-e a gép által "gondolt" számmal, vagy annál kisebb, illetve nagyobb.')


gep_szama = 3
print('\nA gép gondolt egy számra 1 és 5 között. Találd ki! :)')

jatekos_szama = int(input('\nA te számod: '))

if jatekos_szama < gep_szama:
    print('\nA gép nagyobb számra gondolt.')
elif jatekos_szama > gep_szama:
    print('\nA gép kisebb számra gondolt.')
else:
    print('\nEltaláltad!\nGratulálok!')
