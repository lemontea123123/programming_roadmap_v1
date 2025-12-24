"""
Docstring for v1.Level 3.Exercise A.4

4.	Kolom baru dan transformasi
•	Buat kolom baru total_penjualan = jumlah * harga.wikipedia
•	Ubah format kolom tanggal (string → datetime), lalu ekstrak bulan atau tahun ke kolom baru.wikipedia
    Buatin Kolom Baru yang buat menghitung bonus karyawan sesuai dengan target Penjualan
"""

import pandas as pd

df = pd.read_csv("v1/Level 3/data_penjualan.csv")

df["total_penjualan"] = df["jumlah"] * df["harga"]
df["tanggal"]=pd.to_datetime(df["tanggal"])
df["bulan"]=df["tanggal"].dt.month
df["tahun"]=df["tanggal"].dt.year

#diskon 10% untuk pembelian diatas 100000
df["bonus"]=0

df.loc[df["total_penjualan"]>=50000,"bonus"]=10
df.loc[df["total_penjualan"]>=100000,"bonus"]=20
df.loc[df["total_penjualan"]>=200000,"bonus"]=35

df["bonus_karyawan"]= 0
df.loc[df["bonus"]>0,"bonus_karyawan"] = df["total_penjualan"]*(df["bonus"]/100)


print(df.info())
print(df)