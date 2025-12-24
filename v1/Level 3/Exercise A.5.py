"""
Docstring for v1.Level 3.Exercise A.5

5.	Ringkasan/statistik sederhana
•	Hitung total penjualan keseluruhan, rata-rata penjualan per transaksi, nilai maksimum dan minimum.wikipedia
•	Gunakan describe() untuk melihat ringkasan statistik dan pahami artinya (mean, min, max, dll).wikipedia

"""

import pandas as pd 

df = pd.read_csv("v1/Level 3/data_penjualan.csv")
df["total_penjualan"] = df['jumlah'] * df['harga']


total = df["total_penjualan"].sum()
avg = df["total_penjualan"].mean()
maks = df["total_penjualan"].max()
min = df["total_penjualan"].min()

print(df.describe())

print("Total Penjualan: ",total)
print("Rata Penjualan: ",avg)
print("Maks Penjualan: ",maks)
print("Min Penjualan: ",min)