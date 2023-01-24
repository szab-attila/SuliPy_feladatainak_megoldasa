print('2. Feladat')
print('\nKészíts egy programot, amely a felhasználótól szavakat kér be, amíg az csupán ENTER-t nem üt!\nA szavakat '
      'tárolja el a program egy listában! Az adatbekérés befejezte után írja ki a program a lista elemeit, '
      'a legrövidebb és a leghosszabb szót!')

szavak = []

print()
while True:
    szo = input('Adj meg szavakat: ')
    if szo == '':
        break
    szavak.append(szo)

    legrovidebb = szavak[0]
    leghosszabb = szavak[0]

    for szo in szavak:
        if len(szo) < len(legrovidebb):
            legrovidebb = szo
        if len(szo) > len(leghosszabb):
            leghosszabb = szo

print(f'\nA lista elemei: {szavak}.\nA legrövidebb szó: "{legrovidebb}", a leghosszabb szó: "{leghosszabb}".')
