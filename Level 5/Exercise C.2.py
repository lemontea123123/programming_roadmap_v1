"""
Docstring for Exercise C.2
8.	Versi CLI – Tombol “Cek grammar”
•	Tambah menu:
o	4. Cek grammar catatan (anggap catatan bahasa Inggris).
•	Flow:
o	Pilih catatan.
o	Kirim isi ke API dengan prompt grammar correction.
o	Tampilkan versi yang sudah diperbaiki di bawahnya.
"""

from v2Tools.menu_controller import *
from v2Tools.multi_line_input import *
from v2Tools.AI_LLM_TEXT import grammar_check_ai


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
                "ai_check":False
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

        #Jika User memilih catatan
        if(user_input != nomor_exit):
            #Masuk lagi ke menu mini catatan
            index_catatan = user_input -1 
            catatan = list_catatan[index_catatan]
            title = catatan["title"]
            content = catatan["content"]
            check = catatan["ai_check"]

            print("\nJudul Catatan:")
            print(title)
            print("Konten Catatan:")
            print(content)
            user_loading()

            if (not check):
                user_input = display_menu(dialog="Apakah mau coba terapkan grammar check A.I. di konten catatan?",pilihan_menu=sub_menu_1)
                #Jika user memilih untuk coba buatin ringkasan
                if(user_input == 1):
                    #Iya
                    hasil_cek = grammar_check_ai(content)
                    print("\nHasil Grammar Check")
                    print(hasil_cek)
                    user_loading()

                    #sekarang tanyain jika mau simpan ringkasan
                    user_input = display_menu(dialog="Apakah mau simpan hasil?",pilihan_menu=sub_menu_1)
                        
                    #Jika user setuju untuk simpanin ringkasan
                    if(user_input == 1):
                        #Iya
                        catatan["content"] = hasil_cek
                        catatan["ai_check"] = True
                
            
                        
            

    elif(user_input == 3):
        main_loop=False