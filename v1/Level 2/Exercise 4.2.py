"""
Docstring for Exercise 4.2
4.	Simple sort (bubble / selection)
o	Implementasi selection sort sendiri untuk mengurutkan list angka.
"""

list_angka = [12, 5, 9, 1, 18, 7, 3, 15, 2, 10]
panjang_list = len(list_angka)

angka_min = None
index_min = None

for i1 in range(panjang_list):
    times = panjang_list - i1
    for i2 in range(times):
        i2 = i2 + i1
        angka_sekarang = list_angka[i2]

        if angka_min == None or angka_sekarang < angka_min:
            angka_min = angka_sekarang
            index_min = i2
    
    if angka_min != None:
        temp = list_angka[i1]
        list_angka[i1] = list_angka[index_min]
        list_angka[index_min] = temp

    angka_min = None
    index_min = None

print(list_angka)




