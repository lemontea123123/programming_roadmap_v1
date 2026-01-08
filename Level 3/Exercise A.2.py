"""
Docstring for v1.Level 3.Exercise A.2
2.	Seleksi kolom dan baris
•	Ambil hanya kolom tertentu (misal tanggal, produk, jumlah, harga).wikipedia
•	Filter baris dengan kondisi sederhana, misal: hanya penjualan di atas nominal tertentu atau produk tertentu saja.wikipedia
"""

import pandas as pd

#Dataframe utama
df = pd.read_csv("v1\Level 3\data_penjualan.csv")

#Filter
mask = df["harga"] > 10000
mask2 = df["nama_barang"]=="Buku"
mask3 = df["harga"] > 20000

#print(df[mask3])

#tambah kolom baru

df["total penjualan"] = df["harga"]*df["jumlah"]

#Filter
mask4 = df["total penjualan"] > 100000

#print(df[mask4])

#Filter Kombinasi
mask5 = df["jumlah"]>= 3
mask6 = mask2 & mask5

#print(df[mask6])

#Filter Kombinasi
mask7 = df["nama_barang"]=="Pulpen"
mask8 = mask7 | mask2

print(df[mask8])

