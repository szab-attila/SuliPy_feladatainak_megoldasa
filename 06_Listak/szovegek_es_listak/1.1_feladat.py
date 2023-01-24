print('1.1 Feladat')
print('\nKészíts egy programot, amely a felhasználó által megadott mondatról a mondatvégi jel alapján eldönti milyen fajtájú!\n(kijelentő, kérdő, felkiáltó / felszólító / óhatjtó)')

mondat = input('\nÍrj be egy mondatot aminek a végén van mondatvégi írásjel: ')

if mondat[-1] == '.':
    print(f'\n{mondat} --> Ez egy kijelentő mondat.')
elif mondat[-1] == '?':
    print(f'\n{mondat} --> Ez egy kérdő mondat.')
elif mondat[-1] == '!':
    print(f'\n{mondat} --> Ez egy felkiáltó / felszólító / óhatjtó mondat.')

    

    

