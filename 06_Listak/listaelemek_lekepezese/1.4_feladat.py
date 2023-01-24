print('1.4 Feladat')
print('\nKészíts egy programot, amely sztringeket tartalmazó listaelemek leképezését valósítja meg.\nA leképezéshez a sztringek metódusait ezen az oldalon bemutató listából válassz egyet!\nA program írja ki az eredeti és a generált listát is a képernyőre!')

old_list = ['portion', 'tribute','donor','shape','hip']
new_list = [word.capitalize() for word in old_list]


print()
print(old_list)
print(new_list)