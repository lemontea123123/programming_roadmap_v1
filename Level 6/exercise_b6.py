"""
Docstring for exercise_b6
. Hitung frekuensi elemen
Ini menguatkan konsep dict / hash map.hackerrank+1
•	Buat fungsi count_char_frequency(s):
o	Input string, output dict karakter -> jumlah.
o	Abaikan spasi, jadikan semua huruf lower case.
•	Buat fungsi count_number_frequency(nums):
o	Input list angka, output dict angka -> jumlah.
•	Tambahan: dari dict frekuensi, cari:
o	Karakter/angka yang paling sering muncul.
o	Karakter/angka yang paling jarang muncul (kalau ada lebih dari satu, ambil yang pertama muncul di input).interviewcoder
"""

sample_string_1 = "Hello World"

def count_char_frequency(s):
    s_2 = s.lower()
    new_dict = {}

    for char in s_2:
        flag1 = char == " "

        flag_true = not flag1

        if(flag_true):
            if char in new_dict:
                new_dict[char] += 1
            else:
                new_dict[char] = 1
        
    
    return new_dict

"""
•	Buat fungsi count_number_frequency(nums):
o	Input list angka, output dict angka -> jumlah.
"""

sample_nums_1 = [1, 2, 2, 3, 3, 3]

def count_number_frequency(nums):
    new_dict = {}
    for num in nums:
        if num in new_dict:
            new_dict[num] += 1
        else:
            new_dict[num] = 1


"""
•	Tambahan: dari dict frekuensi, cari:
o	Karakter/angka yang paling sering muncul.
o	Karakter/angka yang paling jarang muncul (kalau ada lebih dari satu, ambil yang pertama muncul di input).interviewcoder
"""

#Fungsi buat cek karakter/angka yang paling sering muncul

dict_1 = count_char_frequency("Hello Woorld!")


def dict_string_count_find_most(dict_param):
    dict_values = dict_param.values()
    max_count = 0

    for count in dict_values:
        if max_count <= count:
            max_count = count
    
    max_count_keys_list = []

    for key,value in dict_param.items():
        if(value == max_count):
            max_count_keys_list.append(key)

    return_tuple = (max_count , max_count_keys_list)
    return return_tuple

def dict_string_count_find_least(dict_param):
    dict_values = dict_param.values()
    min_count = None

    for count in dict_values:
        if min_count == None or min_count >= count:
            min_count = count
    
    max_count_keys_list = []

    for key,value in dict_param.items():
        if(value == min_count):
            max_count_keys_list.append(key)

    return_tuple = (min_count , max_count_keys_list)
    return return_tuple



dict_string_count_find_least(dict_1)




        





