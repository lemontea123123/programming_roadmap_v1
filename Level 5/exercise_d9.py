"""
Docstring for Exercise D9
D. Latihan file I/O + AI (wajib)
9.	Script – Baca file teks → ringkas ke file lain
•	Buat file input.txt berisi teks bebas.
•	Buat script ringkas_file.py yang:
o	Membaca isi input.txt.
o	Mengirim ke API dengan prompt ringkasan.
o	Menyimpan hasil ringkasan ke summary.txt.machinelearningmastery+1
•	Tambahan: kalau input.txt kosong, tampilkan pesan error yang jelas dan jangan kirim request.
"""

import os
from v2Tools.AI_LLM_TEXT import *

def summarise_file(input_file_name,output_file_name):
    """
    Docstring for summarise_file
    Fungsi ini membuka text file sesuai input_file_name yg di dalam direktori folder Notes , yg di dalam direktori sekarang
    membuat text file output yg isinya summary input_file_name dan dikasi nama output_file_name , 
    di simpan di dalam folder Notes_summary , yg di dalam direktori sekarang
    
    :param input_file_name: nama file input yang harus ada
    :param output_file_name: nama file output sesuai kebutuhan user

    returns : None
    """
    CURRENT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
    NOTES_DIR_PATH = os.path.join(CURRENT_DIR_PATH,"Notes")
    NOTES_SUMMARY_DIR_PATH = os.path.join(CURRENT_DIR_PATH,"Notes Summary")

    input_txt_path = os.path.join(NOTES_DIR_PATH,input_file_name)
    output_txt_path = os.path.join(NOTES_SUMMARY_DIR_PATH,output_file_name)

    #Check if input txt exists
    if(not os.path.isfile(input_txt_path)):
        raise FileNotFoundError("File ini tidak ditemukan di folder Notes !")

    input_file = open(input_txt_path , "r",encoding="UTF-8")
    content = input_file.read().strip()
    input_file.close()

    if(len(content)==0):
        raise ValueError("Konten File Kosong! ")
    else:
        print("Merangkum ",input_file_name)
        ringkasan = ringkasan_bahasa_ai(content).strip()
        

    output_file = open(output_txt_path,"w",encoding="UTF-8")
    output_file.write(ringkasan)
    output_file.close()
    print("Selesai")


summarise_file("input.txt","output.txt")



