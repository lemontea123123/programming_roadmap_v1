"""
Docstring for exercise_a2
. Big O sekilas (tanpa matematika ribet)
Tujuan: bisa “nebak” kira kira kompleksitas dari kode sederhana.
•	Tulis 3 contoh fungsi kecil di Python:
o	Fungsi yang hanya print satu nilai (tanpa loop) → catat di komentar: “Ini kira kira O(1) karena cuma satu operasi utama.”dev
o	Fungsi yang loop 1 kali lewat list dan print tiap elemen → komentar: “O(n) karena waktu tergantung jumlah elemen list.”dev
o	Fungsi yang punya dua loop bersarang (for di dalam for) untuk print semua pasangan (i, j) → komentar: “O(n²) karena setiap elemen dipasangkan dengan semua elemen lain.”geeksforgeeks
•	Baca potongan kode sederhana (misal loop yang setiap iterasi memotong list jadi setengah pakai indeks) dan tulis di komentar: “Kira kira ini O(log n) karena ukuran masalah berkurang setengah tiap langkah.”linkedin

"""

# O(1)
def say_hello(string):
    print(string)

# O(n)
def spell_string(string):
    for char in string:
        print(char)

def sort_string(string_param,ascending=True):
    string_arr = list(string_param.lower())

    #Implement bubble sort
    string_length = len(string_arr)
    for i1 in range(string_length):
        times = string_length -i1-1
        for i2 in range(times):
            current_index = i2
            next_index = i2+1

            current_letter = string_arr[current_index]
            next_letter = string_arr[next_index]

            greater_than_flag = current_letter > next_letter

            if(ascending):
                switch = greater_than_flag
            else:
                switch = not greater_than_flag
            
            if(switch):
                temp_letter = current_letter
                string_arr[current_index] = next_letter
                string_arr[next_index] = temp_letter
    
    return "".join(string_arr)

def binary_search(string_param , char_target):
    string_list = list(string_param)
    list_length = len(string_list)

    if(list_length == 0):
        raise ValueError("string_param length is 0 !")

    if(list_length == 1):
        #Immediately compare then return
        return string_list[0] == char_target
    
    left_index = 0
    right_index = list_length - 1
    

    while(True):
        range_1 = right_index - left_index
        mid_index = int( ((range_1 / 2) + left_index ) )

        if(string_list[mid_index] == char_target):
            return mid_index

        if(string_list[mid_index] > char_target):
            right_index = mid_index - 1
        else:
            left_index = mid_index + 1
        


sample_data = "lemonteaabcxyz"
sorted_data = sort_string(sample_data)

print(binary_search(sorted_data,"l"))