print('1.2 Feladat')
print('\nFejleszd tovább az első feladat programját úgy, hogy amennyiben a felhasználó\nnem a két lehetséges válasz (igen/nem) közül ad meg egyet, a gép kiírja: "Sajnos nem értem a válaszodat!"')

print('\nSzia!')

kerdes = input("Jó napod van ma (igen/nem)? ")

if kerdes == 'igen':
    print('\nSzuper! Maradjon is így! :)')
elif kerdes == 'nem':
    print('\nSajnálom! Remélem holnap már jobb lesz! :)')
else:
    print('Sajnos nem értem a válaszodat!')