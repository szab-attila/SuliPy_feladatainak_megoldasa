print('3. Feladat - X')
print('\nKészíts egy programot, amely egymásba ágyazott ciklusok segítségével rajzolja ki egy 7 x 7-es mezőben az alábbi alakzatot\n')

sor = 1

while sor <= 7:
    oszlop = 1
    while oszlop <= 7:
        #print(f'{sor}:{oszlop} ', end='')
        #print(f'{sor + oszlop} ', end='')
        if sor == oszlop or sor + oszlop == 8:
            print(f'O ', end='')
        else:
            print('. ', end='')
        oszlop += 1
    print('')
    sor += 1
