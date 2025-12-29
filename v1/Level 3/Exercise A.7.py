"""
Docstring for v1.Level 3.Exercise A.7
7.	Plot sederhana
•	Buat grafik garis: penjualan per bulan.wikipedia
•	Buat grafik batang: total penjualan per produk.wikipedia
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("v1/Level 3/data_penjualan.csv").reset_index()

df["total_penjualan"] = df["harga"]*df["jumlah"]
df["tanggal"] = pd.to_datetime(df["tanggal"])
df["bulan"] = df["tanggal"].dt.month


group_bulan = df.groupby("bulan")
#Data Frame of grouped data based on Month sales
df2 = group_bulan["total_penjualan"].sum().reset_index()
df2["total_penjualan"] = df2["total_penjualan"]/1000000


group_produk = df.groupby("produk")
#Data Frame of grouped data based on Product sales
df3 = group_produk["total_penjualan"].sum().reset_index()
#IN MILLIONS
df3["total_penjualan"]=df3["total_penjualan"]/1000000



#print(df2[["bulan","total_penjualan"]])

plt.figure(figsize=(8, 4))
plt.plot(df2["bulan"],df2["total_penjualan"],marker="o")

plt.title("Total Penjualan Per Bulan")
plt.xlabel("Bulan")
plt.ylabel("Total Penjualan di Jutaan")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 4))
plt.bar(df3["produk"],df3["total_penjualan"])

plt.title("Total Penjualan Per Produk")
plt.xlabel("Produk")
plt.ylabel("Total Penjualan di Jutaan")
plt.tight_layout()
plt.show()

