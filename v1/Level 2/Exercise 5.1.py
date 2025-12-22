"""
Docstring for Exercise 5.1
o	Program yang menerima list angka dan mengembalikan list baru berisi hanya angka genap.
"""

angka_list = [7, 10, 13, 20, 25, 30, 41]
angka_list_baru = []

for angka in angka_list:
    if angka % 2 == 0:
        angka_list_baru.append(angka)

print("END")