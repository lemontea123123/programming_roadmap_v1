"""
Docstring for v1.Level 3.Exercise A.3

3.	Pembersihan data dasar
•	Cek apakah ada nilai kosong (NaN) di dataset.wikipedia
•	Latihan:
o	Menghapus baris yang banyak NaN.
o	Mengisi nilai kosong dengan nilai default (misal 0 atau “Tidak diketahui”).wikipedia
"""

import pandas as pd

df = pd.read_csv("v1\Level 3\data_penjualan1.csv")

#Finds which rows excluding id and tanggal columns , which cells DOES NOT NaN
mask1 = df[["jumlah"]].notna().any(axis=1)


#which rows from both column nama_barang dan harga DOES NOT NaN bersamaan!!!
mask2 = df[["nama_barang","harga"]].notna().any(axis=1)

mask_final = (mask1 & mask2)

print(type(mask1))
print(type(mask2))

new_data_frame = df[mask_final]


#Only Tanggal dan Nama_barang columns allowed to have NaN values
# in these columns NaN will be filled with 0

new_data_frame = new_data_frame.fillna(0)

#Filter
print(new_data_frame)



