"""
o	Implementasi queue sederhana:
	Operasi: enqueue, dequeue, lihat_depan, cek_kosong.
	Simulasi: antrian loket; tambahkan nama orang ke antrian, keluarkan satu per satu.
"""

user_list = [
    (1,"Raymond"),
    (2,"Test1"),
    (3,"Test3"),
    (4,"Test4"),
    (5,"Test5")
]

def cek_kosong(user_list):
    return len(user_list)==0

def next_number(user_list):
    if cek_kosong(user_list) == False :
        last_ele = user_list[len(user_list)-1][0]
    else:
        last_ele = 0

    return last_ele+1

    
def enqueue(user_list , nama):
    next_no = next_number(user_list)
    new_ele = (next_no,nama)

    user_list.append(new_ele)

def dequeue(user_list):
    if cek_kosong(user_list)==False:
        user_list.pop(0)


enqueue(user_list , "Raymond2")
user_list=[]
enqueue(user_list,"Lemon")
dequeue(user_list)
print("test")

