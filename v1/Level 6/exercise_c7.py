"""
Docstring for exercise_c7
C. Latihan gabungan pola LeetCode Easy (wajib)
7. Soal pola array & string
Pilih 4–6 soal yang mirip LeetCode Easy, tapi bisa kamu definisikan sendiri dulu (tanpa buka LeetCode).geeksforgeeks+1
•	Contoh soal yang bisa kamu buat dan kerjakan:
o	Diberi list angka, cari:
1.	Nilai maksimum dan minimum.
2.	Indeks pertama angka tertentu.
3.	Diberi string, cek apakah palindrome (abaikan spasi dan kapital).
4.	Geser semua nol ke akhir list sambil menjaga urutan angka lain.
5.	Gabungkan dua list terurut menjadi satu list terurut.
•	Untuk tiap soal:
o	Tulis dulu penjelasan dengan bahasamu sendiri (di komentar).
o	Tulis solusi brute force (kalau ada).
o	Kalau sudah paham, coba perbaiki ke versi yang lebih efisien (misal dari dua loop jadi satu loop, atau dari list ke dict/set).
interviewcoder
"""

#1.	Nilai maksimum dan minimum.
nums_1 = [3, 7, 2, 9, 4]

def max(numbers):
    max_value = None
    for num in nums_1 :
        if(max_value==None or max_value <= num):
            max_value = num
    
    return max_value

def min(numbers):
    min_value = None
    for num in nums_1 :
        if(min_value==None or min_value >= num):
            min_value = num
    
    return min_value

min(nums_1)

#2.	Indeks pertama angka tertentu.
def search(numbers , target):
    for index, num in enumerate(numbers):
        if(num==target):
            return index
    
    return None

#3.	Diberi string, cek apakah palindrome (abaikan spasi dan kapital).

def is_palindrome_first(string_param):
    
    list_string = list(string_param.lower())
    new_list_string = []

    for letter in list_string:
        if(letter == " "):
            continue
        new_list_string.append(letter)

    new_string = "".join(new_list_string)

    #2 pointers algo
    left = 0
    right = len(new_string) - 1
    
    while(right>left):
        left_letter = new_string[left]
        right_letter = new_string[right]

        if(left_letter!=right_letter):
            return False

        left+= 1
        right-=1

    return True

def is_palindrome_second(string_param):
    list_string = list(string_param.lower())
    new_list_string = []
    list_string_2 = []

    for letter in list_string:
        if(letter == " "):
            continue
        new_list_string.append(letter)
        list_string_2.append(letter)

    new_string = "".join(new_list_string)

    #Brute Force??
    #Reverse second list
    list_string_2 = list_string_2[::-1]

    half_length = len(new_list_string)/2

    for i in range(int(half_length)):
        if(new_list_string[i]!=list_string_2[i]):
            return False

    return True

is_palindrome_second("never odd or even")

#4.	Geser semua nol ke akhir list sambil menjaga urutan angka lain.
nums_2 = [4, 0, 5, 0, 0, 7, 8]

def geser_nol_first(nums_param):
    pointer = 0
    
    for index in range(len(nums_2)):
        number = nums_param[index]

        if number != 0:
            #Switch
            temp_num = nums_param[pointer]
            nums_param[pointer] = nums_param[index]
            nums_param[index] = temp_num

            pointer += 1
    
    return nums_param
    
def geser_nol_second(nums_param):
    new_list = []
    zero_counter =0

    for num in nums_param:
        if(num != 0):
            new_list.append(num)
        else:
            zero_counter += 1
    
    for index in range(zero_counter):
        new_list.append(0)

    

    return new_list


#print(geser_nol_second([4, 0, 5, 0, 0, 7, 8]))

#5.	Gabungkan dua list terurut menjadi satu list terurut.
list_a1 = [1, 3, 5, 7]

list_a2 = [2, 4, 6, 8]
# Hasil: [1, 2, 3, 4, 5, 6, 7, 8]





#Ini hanya bisa proses 2 list yg masing2 sudh di sortir dgn benar
def gabung_list_one(list_param_1 , list_param_2):
    i1_length = len(list_param_1)
    i2_length = len(list_param_2)
    total_length = i1_length + i2_length
    
    new_list = []
    
    i1_current = None
    i2_current = None

    i1 = 0
    i2 = 0

    for i in range(total_length):

        #Cek if out of index , if not assign , if yes flag
        i1_out_of_index = i1>=i1_length
        i2_out_of_index = i2>=i2_length
        either_out_of_index = i1_out_of_index or i2_out_of_index

        #penentu jika milih dari elemen berikut list 1 atau list 2 
        choose_i1_current = False
        

        #if each not out of index then assign
        if(not i1_out_of_index):
            i1_current = list_param_1[i1]
        
        if(not i2_out_of_index):
            i2_current = list_param_2[i2]

        if(not either_out_of_index):
            choose_i1_current = i1_current < i2_current
        elif(i1_out_of_index):
            choose_i1_current = False
        elif(i2_out_of_index):
            choose_i1_current = True

        if(choose_i1_current):
            new_list.append(i1_current)
            i1 += 1
        else:
            new_list.append(i2_current)
            i2 += 1

    return new_list

def gabung_list_two(list_param_1,list_param_2):
    new_list = list_param_1 

    for ele in list_param_2:
        new_list.append(ele)
    
    #Implement bubble sorting
    for i1 in range(len(new_list)):
        times = len(new_list) - 1 - i1
        for i2 in range(times):
            current_ele_i = i2
            next_ele_i = i2 + 1

            current_ele = new_list[current_ele_i]
            next_ele = new_list[next_ele_i]

            if(current_ele>next_ele):
                temp = next_ele
                new_list[next_ele_i] = current_ele
                new_list[current_ele_i] = temp
    
    return new_list


#Fungsi Rekursif 
def gabung_list_main(list_param_1):
    length = len(list_param_1)
    half = length/2
    half = int(half)  

    first_start_i = 0
    first_end_i = half
    second_start_i = half
    second_end_i = length

    first_split = list_param_1[first_start_i:first_end_i]
    second_split = list_param_1[second_start_i:second_end_i]  

    #Base Case
    if(length <= 2):
        result_list = gabung_list_one(first_split,second_split)
        return result_list
    else:
        first_split_sorted = gabung_list_main(first_split)
        second_split_sorted = gabung_list_main(second_split)

        return gabung_list_one(first_split_sorted,second_split_sorted)
    



print(gabung_list_main([64, 34, 25, 12, 22, 11, 90]))








            