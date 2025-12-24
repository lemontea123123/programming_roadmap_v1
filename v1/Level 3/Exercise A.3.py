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

#Finds which rows excluding id and tanggal columns , which cells doesnt contain NaN
data_frame_nan_mask = df[["jumlah","harga"]].isna()
#Reduce to a series mask , which row contain NaN is identified , True is inverted to False
single_series_mask = data_frame_nan_mask.any(axis=1) == False

new_data_frame = df[single_series_mask]

#Only Tanggal dan Nama_barang columns allowed to have NaN values
# in these columns NaN will be filled with 0

new_data_frame = new_data_frame.fillna(0)

#Filter
print(new_data_frame)



