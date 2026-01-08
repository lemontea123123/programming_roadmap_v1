"""
Docstring for Tools.Menu Selection User Prompt

Ini program yang mewajibkan user untuk menginput nomor sesuai dengan pilihan


"""


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

def user_loading(dialog="Press Anything To Continue..."):
    print(dialog)
    input()

def input_nomor(dialog="Input Nomor Yang Benar:",choices = []):
    print(dialog)
    loop = True
    user_input = None
    while loop:   
        try:
            user_input = int(input())

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

def display_menu(dialog="\nMain Menu: ",pilihan_menu=["TEST,TEST"]):
    """
    pilihan_menu = [
        "Tambah orang ke antrian",
        "Layani orang berikutnya (mengeluarkan dari antrian)",
        "Lihat antrian saat ini",
        "Keluar"
    ]
    """

    if len(pilihan_menu)<1:
        print("Tidak Ada Pilihan Untuk Menu!!")
        return -1

    pilihan_nomor = list(range(1,len(pilihan_menu)+1))

    print(dialog)         
    for i , pesan in enumerate(pilihan_menu):
        print(i+1,". ",pesan)

    user_input = input_nomor(dialog="Pilih No. Menu:", choices = pilihan_nomor )

    return user_input


