"""
Docstring for v1.Level 2.Exercise 10
10.	Project 3 – Antrian layanan (queue)
•	Program menu:
o	
1.	Tambah orang ke antrian
o	
2.	Layani orang berikutnya (mengeluarkan dari antrian)
o	
3.	Lihat antrian saat ini
o	
4.	Keluar
•	Data antrian disimpan di list (atau collections.deque kalau sudah kenal).
•	Pastikan ada pesan kalau antrian kosong saat ingin melayani.
"""

from Tools.menu_controller import main as menu_controller_main

pilihan_menu = [
    "Tambah orang ke antrian",
    "Layani orang berikutnya (mengeluarkan dari antrian)",
    "Lihat antrian saat ini",
    "Keluar"
]

pilihan_user = menu_controller_main(pilihan_menu)

print("test")



