print('3. Feladat')
print('\nKészíts egy programot, amely a felhasználó által megadott egész számról eldönti, hogy\n- csak 3-mal osztható,\n- csak 4-gyel osztható,\n- 3-mal és 4-gyel is osztható,\n- sem 3-mal, sem 4-gyel nem osztható!')


szam = int(input('\nAdj meg egy egész számot: '))

if szam % 12 == 0:
    print('\nEz a szám osztható hárommal és néggyel is.')
elif szam % 4 == 0:
    print('\nEz a szám osztható néggyel.')
elif szam % 3 == 0:
    print('\nEz a szám osztható hárommal.')
else:
    print('\nEz a szám nem osztható hárommal és néggyel sem.')