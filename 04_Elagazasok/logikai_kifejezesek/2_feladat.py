print('2. Feladat')
print('\nKészíts egy programot, amely a felhasználótól két külön kérdésben megkérdezi,\nhogy az ikrek (Henrik és Hanna) jönnek-e ma kosrazni! Például így: Jön Henrik ma kosarazni? (igen/nem). \nA program írja ki, hogy melyik állítás igaz az alábbiak közül:\n- egyikük sem jön kosarazni,\n- mind a ketten jönnek kosarazni,\n- csak az egyikük jön kosarazni.')

henrik = input('\nJön Henrik ma kosarazni? (igen/nem) ')
hanna = input('Jön Hanna ma kosarazni? (igen/nem) ')

if henrik == 'nem' and hanna == 'nem':
    print('\nEgyikük sem jön kosarazni.')
elif henrik == 'igen' and hanna == 'igen':
    print('\nMindketten jönnek kosarazni.')
elif henrik == 'igen' and hanna == 'nem' or henrik == 'nem' and hanna == 'igen':
    print('\nCsak az egyikük jön kosarazni.')
else:
    print('\nA megadott válasz egyik kritériumnak sem felel meg.')