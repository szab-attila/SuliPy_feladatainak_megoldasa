print('1.3 Feladat')
print('\nAz előbbi programot módosítsd úgy, hogy csak a 3 betűnél hosszabb szavak kerülnek átalakítva a másik listába!')

old_list = ['apple', 'table', 'cat', 'dog']
new_list = [words.upper() for words in old_list if len(words) > 3]

#for words in old_list:
    #if len(words) > 3:
        #formated_words = words.upper()
        #new_list.append(formated_words)
    #else:
        #new_list.append(words)

print()
print(old_list)
print(new_list)