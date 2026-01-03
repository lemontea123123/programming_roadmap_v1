"""
Docstring for Exercise C.1
Integrasi ke project catatan (wajib)
Anggap kamu sudah punya “app catatan” sederhana (bisa CLI dulu, nanti bisa ke web/Flask di Level 4–5 roadmap).zenvanriel+1
7.	Versi CLI – Tombol “Ringkas”
•	Kalau belum ada, bikin dulu app catatan very simple di terminal:
o	List notes = [].
o	Menu:
	
1.	Tambah catatan (judul + isi)
	
2.	Lihat semua catatan
	
3.	Keluar
•	Tambah fitur baru:
o	3. Ringkas catatan:
	Tampilkan daftar catatan dengan nomor.
	Minta user pilih nomor catatan.
	Ambil isi catatan → kirim ke call_ai() dengan prompt ringkasan.
	Tampilkan ringkasan di terminal (boleh simpan ke field summary kalau mau).
"""

from v2Tools.menu_controller import *
from v2Tools.multi_line_input import *
from v2Tools.AI_LLM_TEXT import *


main_menu = [
    "Tambah Catatan",
    "Lihat Semua Catatan",
    "Keluar"
]

sub_menu_1 = [
    "Iya",
    "Tidak"
]


list_catatan=[]


main_loop = True

while main_loop:
    user_input = display_menu(pilihan_menu=main_menu)

    if(user_input == 1):
        #Tambah Catatan
        catatan_obj = {
            "title":"",
            "content":"",
            "summary":""
        }
        print("Input Judul:")
        catatan_obj["title"] = input()
        catatan_obj["content"] = multi_line_input(dialog="Input Isi:",batas_kata=200)
        list_catatan.append(catatan_obj)
        print("Berhasil Di Tambah!\n")

    elif(user_input==2):
        list_judul_catatan= []
        #Lihat Semua Catatan
        for index , catatan in enumerate(list_catatan):
            list_judul_catatan.append(catatan["title"])
        
        list_pilihan = [*list_judul_catatan,"Exit"]
        #Pilih dari catatan
        user_input = display_menu(dialog="\nPilih Salah Satu Catatan",pilihan_menu = list_pilihan)

        nomor_exit = len(list_pilihan)

        if(user_input != nomor_exit):
            #Masuk lagi ke menu mini catatan
            index_catatan = user_input -1 
            catatan = list_catatan[index_catatan]
            title = catatan["title"]
            content = catatan["content"]
            ringkasan = catatan["summary"]

            print("\nJudul Catatan:")
            print(title)
            print("Konten Catatan:")
            print(content)

            if(ringkasan==""):
                user_input = display_menu(dialog="Apakah mau coba terapkan ringkasan A.I. di konten catatan?",pilihan_menu=sub_menu_1)
                if(user_input == 1):
                    #Iya
                    hasil_ringkasan = ringkasan_bahasa_ai(content)
                    print("\nHasil Ringkasan")
                    print(hasil_ringkasan)
                    user_loading()

                    #sekarang tanyain jika mau simpan ringkasan
                    user_input = display_menu(dialog="Apakah mau simpan ringkasan?",pilihan_menu=sub_menu_1)
                    if(user_input == 1):
                        #Iya
                        catatan["summary"] = hasil_ringkasan
            else:
                #Jika sudh ada ringkasan yg tersimpan
                print("Konten Ringkasan:")
                print(ringkasan)
                user_loading()


    elif(user_input == 3):
        main_loop=False