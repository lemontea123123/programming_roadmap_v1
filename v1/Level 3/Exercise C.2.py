"""
Docstring for v1.Level 3.Exercise C.2
Versi Python + SQL (opsional tapi bagus):
•	Script Python yang:
o	Koneksi ke SQLite.
o	Jalanin query, dan print hasilnya rapi ke terminal.wikipedia

o	Lihat 10 transaksi terbaru.
o	Lihat total penjualan per kategori.
o	Lihat produk dengan penjualan terbanyak.wikipedia

"""

import os
import sqlite3
import pandas as pd

print(os.getcwd())

db_path = "C:\SQLite\databases\latihan.db"

conn = sqlite3.connect(db_path)

query = " SELECT penjualan.tanggal , stok.produk , penjualan.jumlah , stok.harga , (penjualan.jumlah * stok.harga) AS total_penjualan " \
            "FROM penjualan INNER JOIN stok ON penjualan.produk_id = stok.id " \
            "   ORDER BY tanggal DESC , penjualan.id DESC LIMIT 10;"

query2 = " SELECT stok.kategori , sum(penjualan.jumlah) , sum(penjualan.jumlah * stok.harga) AS total_penjualan " \
            "FROM penjualan INNER JOIN stok ON penjualan.produk_id = stok.id GROUP BY stok.kategori  " \
                "ORDER BY total_penjualan DESC ;"

query3 = " SELECT stok.produk , sum(penjualan.jumlah) , sum(penjualan.jumlah * stok.harga) AS total_penjualan " \
            "FROM penjualan INNER JOIN stok ON penjualan.produk_id = stok.id GROUP BY stok.produk " \
                "ORDER BY total_penjualan DESC LIMIT 1;"

df1 = pd.read_sql_query(
    query,
    conn
)

df2 = pd.read_sql_query(
    query2,
    conn
)

df3 = pd.read_sql_query(
    query3,
    conn
)

print("10 Transaksi Terakhir")
print(df1)

print("\nKategori Penjualan")
print(df2)

print("\nProduk Paling Laku")
print(df3)