"""
D. Mini “project algoritma” kecil (wajib)
8. “Statistik simpel” dari list
Project ini menggabungkan beberapa operasi array + frekuensi.
•	Program minta user input list angka (boleh input satu string lalu di-split).
•	Hitung dan tampilkan:
o	Jumlah elemen, nilai minimum, maksimum, rata rata.
o	List angka tanpa duplikat (urutkan).
o	Frekuensi tiap angka (pakai dict).geeksforgeeks
•	Tambahan:
o	Tampilkan angka yang paling sering dan paling jarang muncul.
"""

from v2Tools.multi_line_input import *

loop = True 





def unique_list(list_param):
    last_unique = None
    pointer_i = 0

    for i in range(len(list_param)):
        current_number = list_param[i]

        if(current_number!=last_unique):
            last_unique = current_number
            list_param[pointer_i] = last_unique
            pointer_i += 1
    
    return_value =  list_param[:pointer_i]
    return return_value



def sortir(list_param,ascending=True):
    #Implement bubble sort
    panjang = len(list_param)

    result_list = list_param[:]

    for i1 in range(panjang):
        times = panjang - i1 - 1    
        for i2 in range(times):
            current_i = i2
            next_i = i2 + 1

            current_ele = result_list[current_i]
            next_ele = result_list[next_i]

            flag_switch = False

            if(ascending):
                flag_switch = current_ele > next_ele
            else:
                flag_switch = current_ele <= next_ele
            
            if(flag_switch):
                
                result_list[current_i] = next_ele
                result_list[next_i] = current_ele

    return result_list


def jumlah_ele(list_param):
    jumlah_ele = 0
    counter = 0

    for ele in list_param:
        counter+= 1

    return counter

def cari_min(list_param):
    min_value = None

    for num in list_param:
        if(min_value == None or min_value > num):
            min_value = num
    return min_value

def cari_max(list_param):
    max_value = None

    for num in list_param:
        if(max_value == None or max_value < num):
            max_value = num
    return max_value

def cari_rata(list_param):
    rata_value = 0
    total_value = 0
    length = jumlah_ele(list_param)

    for ele in list_param:
        total_value += ele

    rata_value = total_value / length

    return rata_value

def histogram(list_param):
    new_dict = {}

    for ele in list_param:
        if ele in new_dict:
            new_dict[ele] += 1
        else:
            new_dict[ele] = 1
    
    return new_dict
        
def histogram_min(dict_param):

    dict_values = dict_param.values()

    nilai_min_values = cari_min(dict_values)

    new_tuple = None

    #list key yg mengandung value tersebut
    list_key = []

    for key , value in dict_param.items():
        if(value == nilai_min_values):
            list_key.append(key)

    
    new_tuple = (nilai_min_values , list_key)
    return new_tuple

def histogram_max(dict_param):
    dict_values = dict_param.values()

    nilai_max_values = cari_max(dict_values)

    new_tuple = None

    #list key yg mengandung value tersebut
    list_key = []

    for key , value in dict_param.items():
        if(value == nilai_max_values):
            list_key.append(key)

    
    new_tuple = (nilai_max_values , list_key)
    return new_tuple


"""
•	Hitung dan tampilkan:
o	Jumlah elemen, nilai minimum, maksimum, rata rata.
o	List angka tanpa duplikat (urutkan).
o	Frekuensi tiap angka (pakai dict).geeksforgeeks
•	Tambahan:
o	Tampilkan angka yang paling sering dan paling jarang muncul.
"""



while(loop):
    user_input = multi_line_input(dialog="Input List Angka : ",batas_kata=50)

    new_string = ""
    #Only list in spaces allowed
    for character in user_input:
        flag_1 = False
        flag_2 = False
        flag_3 = False

        try:
            int(character)
            flag_1 = True
        except ValueError:
            flag_1 = False


        if(character==" "):
            flag_2 = True
        else:
            flag_2 = False

        if(character=="-"):
            flag_3 = True
        else:
            flag_3 = False

        if(flag_1 or flag_2 or flag_3):
            new_string += character
        else:
            new_string += " "


        
    new_string = new_string.split()
    numbers_list = []

    for string_ele in new_string:
        try:
            numbers_list.append(int(string_ele))
        except ValueError:
            print("Error Found \"",string_ele,"\" !")


    #print(numbers_list)
    length = jumlah_ele(numbers_list)
    nilai_min = cari_min(numbers_list)
    nilai_max = cari_max(numbers_list)
    nilai_rata = cari_rata(numbers_list)

    print("Jumlah Ele : ",length)
    print("Nilai Min : ",nilai_min)
    print("Nilai Max : ",nilai_max)
    print("Nilai Rata : ",nilai_rata)

    #o	List angka tanpa duplikat (urutkan).
    list_unique = unique_list(sortir(numbers_list))
    print("Di List secara Unik: ",list_unique)

    #o	Frekuensi tiap angka (pakai dict).geeksforgeeks
    histogram_list = histogram(numbers_list)

    for key, value in histogram_list.items():
        print(key," = > ",value)

    #o	Tampilkan angka yang paling sering dan paling jarang muncul.
    histo_max = histogram_max(histogram_list)
    histo_min = histogram_min(histogram_list)

    print()
    print( "".join(str(histo_max[1])) , "\nangka angka ini muncul: ",histo_max[0]," kali , paling banyak kali")
    print()
    print( "".join(str(histo_min[1])) , "\nangka angka ini muncul: ",histo_min[0]," kali , paling sedikit kali")

    print("\n")



    




