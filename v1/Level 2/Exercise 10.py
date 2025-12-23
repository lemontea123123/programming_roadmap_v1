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
pilihan_menu = [
    "Tambah orang ke antrian",
    "Layani orang berikutnya (mengeluarkan dari antrian)",
    "Lihat antrian saat ini",
    "Keluar"
]

def input_nomor(dialog="Input Nomor Yang Benar:",choices = []):
    print(dialog)
    loop = True
    user_input = None
    while loop:   
        try:
            user_input = float(input())

            flag0 = len(choices) > 0
            flag1 = user_input in choices
            flag2 = flag0 and flag1

            #if not in choices but choices length is 0
            flag3 = not(flag0) 

            if flag2 or flag3:
                loop = False
                continue
            
            print("Mohon Input Pilihan No. Yang Benar")

        except ValueError:
            print("Mohon Input Format Nomor Yang Benar")

    return user_input
     


user_input = input_nomor(dialog="Pilih No. Menu:", choices = [1,2,3,4] )