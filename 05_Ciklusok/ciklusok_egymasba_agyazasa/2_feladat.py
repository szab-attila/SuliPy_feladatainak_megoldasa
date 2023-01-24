print('2. Feladat - \\')
print('\nKészíts egy programot, amely egymásba ágyazott ciklusok segítségével rajzolja ki egy 5 x 5-ös mezőben az alábbi alakzatot!\n')

sor = 1
while sor <= 5:
    oszlop = 1
    while oszlop <= 5:
        #print(f'({sor}:{oszlop}) ', end='')
        if oszlop == sor:
            print('O ', end='')
        else:
            print('. ', end='') 
        oszlop += 1
    print('')
    sor += 1