print('2.2 Feladat')
print('\nAz előző programot alakítsuk most úgy át, hogy a listaelemek leképezése az értelemezési tartomány\nnemnegatív elemire korlátozódjon!')

lista = [szam for szam in range(-3, 5) if szam >= 0]

print(lista)