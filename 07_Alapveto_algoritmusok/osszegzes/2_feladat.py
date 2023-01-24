print('2. Feladat')
print('\nÍrj egy programot, amely a felhasználótól kér be egész számokat [-5;5] intervallumban. A bekérés akkor fejeződjön be,\namikor a felhasználó intervallumon kívüli értéket ad meg!\nA program írja ki a megadott intervallumba eső számokat és az összegüket!')

szamok = []

print('')
while True:
    szam = int(input('Adj meg számokat [-5;5] intervallumon: '))
    if szam < -5 or szam > 5:
        break
    szamok.append(szam)

osszeg = 0

for szam in szamok:
    osszeg += szam

print(f'\nA megadott számok listája: {szamok}, összegük: {osszeg}.')
