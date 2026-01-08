"""
o	Implementasi stack sederhana:
	Operasi: push, pop, lihat_atas, cek_kosong.
	Simulasi: tumpukan piring; tambahkan dan ambil piring beberapa kali, print isi stack setiap perubahan.
First In Last Out
"""

user_list = ["piring1" , "piring2" , "piring3" , "piring4"]

def push(list , item):
    list.append(item)

def pop(list):
    length = len(list)
    last_index = length - 1

    if last_index >= 0 :
        list.pop(last_index)

push(user_list,"piring10")

pop(user_list)

print("End")