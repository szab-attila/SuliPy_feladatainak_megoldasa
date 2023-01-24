print('5. Feladat')
print('\nÍrj egy programot, amely a felhasználótól páros számot kér be. \nAmennyiben a megadott szám páratlan, újra és újra megtörténik az adatbekérés mindaddig, \namíg végül páros számot nem ad meg a felhasználó.')

feltetel = True 
while feltetel:
    szam = int(input('\nAdj meg egy páros számot: '))
    if szam % 2 == 0:
        feltetel = False 
    



