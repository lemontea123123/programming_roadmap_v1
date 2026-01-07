"""
Docstring for exercise_b4
4. Reverse string / list
Tujuannya mengenal beberapa cara berpikir untuk masalah yang sama.getsdeready+1
•	Reverse list:
o	Versi 1: pakai slicing nums[::-1].
o	Versi 2: pakai loop for i in range(len(nums)-1, -1, -1) dan simpan ke list baru.
o	Versi 3: pakai two pointers (awal & akhir) lalu swap sampai bertemu di tengah.
•	Reverse string:
o	Versi 1: pakai slicing.
o	Versi 2: convert ke list karakter, reverse manual pakai two pointers, lalu gabung lagi ke string.
"""

nums2 = [10, 20, 30, 40, 50]

#Versi 1: pakai slicing nums[::-1].
def reverse_version_1(list_param):
    new_list = []

    new_list = list_param[::-1]

    return new_list

#Versi 2: pakai loop for i in range(len(nums)-1, -1, -1) dan simpan ke list baru.
def reverse_version_2(list_param):
    new_list = []

    for i in range(len(list_param)-1,-1,-1):
        current_ele = list_param[i]
        new_list.append(current_ele)
    return new_list


#Versi 3: pakai two pointers (awal & akhir) lalu swap sampai bertemu di tengah
def reverse_version_3(list_param):
    
    list_param_length = len(list_param)

    #Special cases where length is 0
    if(list_param_length == 0):
        return list_param

    left_index = 0
    right_index = list_param_length - 1

    while(right_index > left_index):

        #swap
        temp = list_param[left_index]
        list_param[left_index] = list_param[right_index]
        list_param[right_index] = temp

        left_index = left_index + 1
        right_index = right_index - 1
    
    return list_param

reverse_version_3(nums2)
        

#Reverse string:
#o	Versi 1: pakai slicing
sample_string = "12345"

def reverse_string_slicing(string_param):
    new_string = sample_string[::-1]
    return new_string

print(reverse_string_slicing(sample_string))


#Versi 2: convert ke list karakter, reverse manual pakai two pointers, lalu gabung lagi ke string.
def reverse_string_version_2(string_param):
    sample_list = list(string_param)

    reverse_version_3(sample_list)
    return "".join(sample_list)

result_value = reverse_string_version_2(sample_string)

print("test")
