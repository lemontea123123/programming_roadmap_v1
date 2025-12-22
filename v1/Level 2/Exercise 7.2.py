"""
Docstring for v1.Level 2.Exercise 7.2

o	Diberi list angka, buat list baru berisi kuadrat dari angka yang ganjil saja

"""

sampel_data1 = [10, 11, 12, 13, 14, 15]
kuadrat_ganjil = []

for data in sampel_data1:
    if data % 2 ==1:
        kuadrat_ganjil.append(data*data)