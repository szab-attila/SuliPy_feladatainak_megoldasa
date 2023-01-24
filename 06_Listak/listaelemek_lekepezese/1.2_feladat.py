print('1.2 Feladat')
print('\nKészíts egy programot, amely listaelemek leképezésével megvalósítja a következő funkciót:\negy szavakat tartalmazó lista elemeiből generál egy másik listát, amelyben az eredeti szavak csupa\nnagybetűs formában szerepelnek! A program írja ki az eredeti és a generált listát is a képernyőre!')

old_list = ['apple', 'table', 'cat', 'dog']
new_list = [words.upper() for words in old_list]

print()
print(old_list)
print(new_list)