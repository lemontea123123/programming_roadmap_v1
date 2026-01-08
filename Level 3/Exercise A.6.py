"""
Docstring for v1.Level 3.Exercise A.6

6.	Groupby dasar
•	Hitung total penjualan per produk.wikipedia
•	Hitung total penjualan per bulan atau per kategori (kalau dataset punya kolom kategori).wikipedia

"""


import pandas as pd

df = pd.read_csv("v1/Level 3/data_penjualan.csv")

df['total_penjualan'] = df['jumlah']*df['harga']

df['tanggal'] = pd.to_datetime(df['tanggal'])

df['day'] = df['tanggal'].dt.day



group_produk = df.groupby("produk")
df2 = group_produk[["total_penjualan","jumlah"]].sum()

group_produk2 = df.groupby("day")
df3 = group_produk2[["total_penjualan","jumlah"]].sum()

print(df2)
print(df3)
print(df3['total_penjualan'].describe())