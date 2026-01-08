"""
Docstring for Exercise 1.3
o	Buat set berisi beberapa angka dengan duplikat di list asal, lalu tunjukkan 
bahwa set menghilangkan duplikat (print sebelum dan sesudah).
"""


list_test = list(range(1,10))


list_test.append(2)
list_test.append(4)
list_test.append(5)
list_test.append(5)

set1 = set(list_test)

print(list_test)
print(set1)