"""
Docstring for v1.Level 3.Exercise A.1

1.	Baca dan cek data dari CSV
•	Install dan import Pandas, lalu baca file CSV sederhana (misal data_penjualan.csv).wikipedia
•	Tampilkan 5 baris pertama, jumlah baris/kolom, dan tipe data tiap kolom.wikipedia


"""

import pandas as pd
import os


df = pd.read_csv("v1\Level 3\data_penjualan.csv")

df.dropna(axis="columns",how="all")
df["harga"]=df["harga"].astype("float64")

print(df.head())
print(df.shape)
print(df.info())
