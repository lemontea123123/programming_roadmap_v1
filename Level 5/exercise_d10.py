"""
Docstring for Exercise D10
10.	Script – Batch ringkasan beberapa file
•	Buat folder notes/ berisi beberapa .txt (misal note1.txt, note2.txt …).
•	Script batch_summary.py:
o	Loop semua file .txt di folder.
o	Untuk setiap file, baca isi → kirim ke API → simpan di Notes Summary/nama_file.txt.
•	Tambahan: print progress, misal “Merangkum note1.txt… selesai”.

"""

from exercise_d9 import summarise_file
import os

ABS_PATH = os.path.abspath(__file__)
NOTES_DIR = os.path.join(os.path.dirname(ABS_PATH),"Notes")

list_notes = os.listdir(NOTES_DIR)



for notes_txt in list_notes:
    summarise_file(input_file_name=notes_txt,output_file_name=notes_txt)

#summarise_file("input1.txt","output.txt")