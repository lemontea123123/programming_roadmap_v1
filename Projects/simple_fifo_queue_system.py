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

from v2Tools.menu_controller import main  as menu_controller_main 
from v2Tools.menu_controller import user_loading 

"""
Pilihan Menu
1.	Tambah orang ke antrian
2.	Layani orang berikutnya (mengeluarkan dari antrian)
3.	Lihat antrian saat ini
4.	Keluar
"""

"""
Data structure FIRST IN FIRST OUT
-DENGAN LIST
-INTERAKSI DGN FUNGSI PUSH POP CUSTOM UTK IMPLEMENTASI FIRST IN FIRST OUT

antrian objek dictionary yg kunci , no. antrian , nama
"""

def cek_kosong():
    return len(list_antrian) < 1

def cek_no_terakhir():
    if cek_kosong():
        return 0
    
    index_terakhir = len(list_antrian)-1
    entri_terakhir = list_antrian[index_terakhir]
    return entri_terakhir["nomor"]


def buat_entri(nama):
    nomor_antrian = cek_no_terakhir() + 1

    return {
        "nomor":nomor_antrian,
        "nama":nama
    }

def tambah_orang(nama):
    entri = buat_entri(nama)
    list_antrian.append(entri)
    print("\nBerhasil Menambah ",nama," Ke Antrian No-",entri["nomor"])


list_antrian = [
    {"nomor": 1, "nama": "Andi"},
    {"nomor": 2, "nama": "Budi"},
    {"nomor": 3, "nama": "Cici"},
    {"nomor": 4, "nama": "Dina"},
    {"nomor": 5, "nama": "Eko"}
]


nomor_antrian_terakhir = 5

pilihan_menu = [
    "Tambah orang ke antrian",
    "Layani orang berikutnya (mengeluarkan dari antrian)",
    "Lihat antrian saat ini",
    "Keluar"
]


loop = True
while loop :
    pilihan_user = menu_controller_main(pilihan_menu = pilihan_menu)
    if pilihan_user == 1:
        print("\nInput Nama:")
        user_input_nama = input()

        tambah_orang(user_input_nama)
        user_loading()
        
    if pilihan_user == 2:
        if cek_kosong():
            print("\nAntrian Sekarang Lagi Kosong")
            user_loading("Balik Ke Main Menu")
        else:
            entri_sekarang = list_antrian.pop(0)
            print("\nSedang Melayani:\nNo: ",entri_sekarang["nomor"],"\nNama: ",entri_sekarang["nama"])

            dialog = "Konfirmasi Pelayanan Telah Selesai Untuk Balik Ke Main Menu"
            user_loading(dialog)
            user_loading(dialog)
            user_loading(dialog)

    if pilihan_user ==3:
        if cek_kosong():
            print("\nAntrian Sekarang Lagi Kosong")
            user_loading("Balik Ke Main Menu")
        else:
            print("\nList Antrian: ")
            for entri in list_antrian:
                nama_entri = entri["nama"]
                nomor_entri = entri["nomor"]

                print(nomor_entri,". ",nama_entri)
            user_loading()

    if pilihan_user ==4:
        loop=False





