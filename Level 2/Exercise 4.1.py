"""
Docstring for Exercise 4.1
    4.	Simple sort (bubble / selection)
o	Implementasi bubble sort sendiri untuk mengurutkan list angka dari kecil ke besar.
"""

"""
List hampir terurut
Contoh: [1, 2, 3, 4, 6, 5, 7, 8] (cuma sedikit yang salah posisi).

List acak
Contoh: [7, 2, 9, 4, 1, 8, 3, 6].

"""

angka_list = [12, 5, 9, 1, 18, 7, 3, 15, 2, 10, 6, 14, 8, 4, 11, 13, 20, 19, 17, 16]

angka_list2 = [1, 2, 3, 4, 6, 5, 7, 8]
angka_list3 = [7, 2, 9, 4, 1, 8, 3, 6]

def bubble_sort(angka_list):
    total_swaps = 0
    list_length = len(angka_list)
    if list_length > 1:
        for i1 in range(list_length-1):
            times = list_length - i1 - 1
            for i in range(times):
                current_angka = angka_list[i]
                next_angka = angka_list[i+1]

                if current_angka > next_angka:
                    total_swaps = total_swaps + 1
                    angka_list[i+1] = current_angka
                    angka_list[i] = next_angka

    print("Total swaps : ",total_swaps)
    return angka_list

print(bubble_sort(angka_list))
print(bubble_sort(angka_list2))
print(bubble_sort(angka_list3))
