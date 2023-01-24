import random

print('2. Feladat')
print('A program a pénzfeldobást modellezi.\nKérdezze meg a felhasználótól a választását (fej vagy írás), majd adjon tájékoztatást, hogy eltalálta-e!')

lista = ['fej', 'írás']
gep_dontese = random.choice(lista)

def fej_vagy_iras(dontes):
    if gep_dontese == dontes:
        print('Gratulálok, eltaláltad.')
    else:
        print('Sajnos nem találtad el.')

dontes = input('\nFej vagy írás? ')

fej_vagy_iras(dontes)