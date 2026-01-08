"""
Docstring for v1.Level 3.Exercise E.3
3. Indexing & slicing
•	Ambil elemen tunggal, satu baris, satu kolom, dan sub array (misal baris 0–1, kolom 1–2).numpy+1
•	Latihan boolean indexing: ambil hanya elemen yang lebih besar dari nilai tertentu, dan ganti elemen yang 
        kurang dari 0 menjadi 0.geeksforgeeks+1
"""

import numpy as np

range_1 = np.arange(1,13)
grid_1 = range_1.reshape((3,4))


print(grid_1)

#Ambil satu baris
row_2 = grid_1[1]

#Ambil satu kolom
col_2 = grid_1[:,1]

#Sub Array
sub_array = []
sub_array.append(grid_1[0:2,:])
sub_array.append(grid_1[:,1:3])

#Boolean Indexing
mask_1 = grid_1 > 3
grid_1[mask_1] = 0

print(grid_1[mask_1])
print(grid_1)
