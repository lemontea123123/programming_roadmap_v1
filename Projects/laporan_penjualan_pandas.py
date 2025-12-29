"""
C. Mini project utama (wajib)
1. Mini Project – Laporan Penjualan dengan Pandas
Target: dari satu file CSV, kamu bisa bikin ringkasan.
Minimal fitur:
•	Baca file penjualan.csv.wikipedia
•	Tampilkan:
o	Total penjualan keseluruhan.
o	Top 5 produk berdasarkan total penjualan.
o	Penjualan per bulan dalam bentuk tabel kecil.wikipedia
•	Opsional: simpan ringkasan ke file baru ringkasan_penjualan.csv.wikipedia
"""

import os
import pandas as pd

df1 = pd.read_csv("Projects/csv_penjualan/data_penjualan.csv")
df1["tanggal"] = pd.to_datetime(df1["tanggal"])
df1["total_penjualan"] = df1["jumlah"] * df1["harga"]
df1["bulan"] = df1["tanggal"].dt.month


total_total_penjualan = df1["total_penjualan"].sum()

print("Total Penjualan Keseluruhan:")
print(total_total_penjualan)

group_object1 = df1.groupby("produk")
df2 = group_object1[["jumlah","total_penjualan"]].sum()
df2_sorted = df2.sort_values(by="total_penjualan",ascending=False).reset_index()
print(df2_sorted)

group_object2 = df1.groupby("bulan")
df3 = group_object2[["jumlah","total_penjualan"]].sum().sort_values(by="bulan",ascending=True).reset_index()
print(df3)

df2_sorted.to_csv("Projects/Ringkasan Penjualan/ringkasa_penjualan_per_produk.csv",index=False)
df3.to_csv("Projects/Ringkasan Penjualan/ringkasa_penjualan_per_bulan.csv",index=False)





