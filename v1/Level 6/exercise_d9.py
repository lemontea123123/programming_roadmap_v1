"""
Docstring for exercise_d9
9. “Analisa teks” sederhana
Project ini menggabungkan string + dict.
•	Program minta user input paragraf pendek.
•	Tampilkan: 
o	Jumlah total karakter (tanpa spasi).
o	Jumlah kata (pisah dengan spasi).
o	5 kata yang paling sering muncul beserta jumlahnya.interviewcoder
•	Bonus:
o	Tampilkan juga apakah paragraf mengandung palindrome (kata yang kalau dibalik sama, contoh: “level”, “katak”).
"""

from v2Tools.multi_line_input import *

program_loop = True

def is_palindrome(string_param):
    #clear whitespace filter word
    whitespace_chars = [" ", "\t", "\n", "\r", "\x0b", "\x0c"]
    punctuation_chars = punctuation_chars = [
    "!", '"', "#", "$", "%", "&", "'", "(", ")", "*",
    "+", ",", "-", ".", "/", ":", ";", "<", "=", ">",
    "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|",
    "}", "~"
]
    filtered_string = ""
    

    for letter in string_param.lower():
        flag_1 = letter not in whitespace_chars
        flag_2 = letter not in punctuation_chars

        if(flag_1 and flag_2):
            filtered_string += letter

    length = len(filtered_string)

    left = 0
    right = length - 1

    while(left<right):
        left_char = filtered_string[left]
        right_char = filtered_string[right]

        if(left_char != right_char):
            return False
        
        left += 1
        right -= 1
    
    return True

def compare_ele(tup_1 , tup_2):
    #Mengambil 2 struktur data tup (angka_jumlah,kata_representatif) , dan sambil bandingkan in descending untuk program ini
    jumlah_1 = tup_1[0]
    jumlah_2 = tup_2[0]

    isi_1 = tup_1[1]
    isi_2 = tup_2[1]

    #Kalau Jumlah ini Descending
    if(jumlah_1>jumlah_2):
        return 1
    elif(jumlah_1<jumlah_2):
        return -1

    #Jika jumlah sama
    #Kalau Isi kata tetap harus ascending
    #Aku mau nya untuk logika ini tetap dahului yg hurufan sebelum jdi ascneding
    if(isi_1 < isi_2):
        return 1
    elif(isi_1 > isi_2):
        return -1

    return 0


def merge_main(list_param_1,list_param_2):
    #Asumsi 2 list itu sudh di sortir isinya , list ini mengandung tuple custom
    length = len(list_param_1) + len(list_param_2)
    i1 = 0
    i2 = 0

    new_list = []

    for i0 in range(length):
        ele_i1 = None
        ele_i2 = None

        i1_oob = i1>= len(list_param_1)
        i2_oob = i2>= len(list_param_2)
        compare_flag = (not i1_oob) and (not i2_oob)
        assign_i1 = False

        if(not i1_oob):
            ele_i1 = list_param_1[i1]

        if(not i2_oob):
            ele_i2 = list_param_2[i2]

        if(compare_flag):
            comparison = compare_ele(ele_i1 , ele_i2)
            assign_i1 = comparison > 0
        elif(i1_oob):
            assign_i1 = False    
        elif(i2_oob):
            assign_i1 = True
            
        
        if(assign_i1):
            new_list.append(ele_i1)
            i1 += 1
        else:
            new_list.append(ele_i2)
            i2 += 1

    return new_list
    
def merge_sort(list_param_1):
    length = len(list_param_1)
    half = int(length / 2)

    first_half = list_param_1[0:half]
    second_half = list_param_1[half:length]

    if length <= 2:
        #Base Case
        return_value = merge_main(first_half,second_half)
    else:
        first_half_sorted = merge_sort(first_half)
        second_half_sorted = merge_sort(second_half)
        return_value = merge_main(first_half_sorted,second_half_sorted)
        

    return return_value

def histo_kata(list_param_1):
    new_dict = {}

    for kata in list_param_1:
        if kata in new_dict :
            new_dict[kata] += 1
        else:
            new_dict[kata] = 1

    return new_dict


while(program_loop):
    user_input = multi_line_input("Input Paragraf Pendek",batas_kata=1000)
    filtered_input = ""

    punctuation_chars = [
        "!", '"', "#", "$", "%", "&", "'", "(", ")", "*",
        "+", ",", "-", ".", "/", ":", ";", "<", "=", ">",
        "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|",
        "}", "~"
    ]

    for huruf in user_input:
        if huruf not in punctuation_chars:
            filtered_input += huruf

    
    list_kata = filtered_input.lower().split()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    kata_no_whitespace = "".join(list_kata)

    print("Jumlah Huruf Tanpa Whitespace: ",len(kata_no_whitespace))
    print("Jumlah Kata: ",len(list_kata))

    #o	5 kata yang paling sering muncul beserta jumlahnya.interviewcoder
    histo_input = histo_kata(list_kata)
    histo_details = []

    for key , value in histo_input.items():
        new_tup = (value , key)
        histo_details.append(new_tup)

    histo_details_sorted = merge_sort(histo_details)
    
    histo_details_sorted_top_5 = histo_details_sorted[0:5]

    #Print
    for index , detail in enumerate(histo_details_sorted_top_5):
        detail_jumlah = detail[0]
        detail_kata = detail[1]

        print(index+1 , ". ",detail_kata," => ",detail_jumlah)

    #•	Bonus:
    #o	Tampilkan juga apakah paragraf mengandung palindrome (kata yang kalau dibalik sama, contoh: “level”, “katak”).
    palindrome_set = set()
    for kata in list_kata :
        if(is_palindrome(kata)):
            palindrome_set.add(kata)
    
    print("Berikut kata kata palindrome yang ditemukan :")
    print(palindrome_set)
    
    print("\n\n")






    
    