"""
Docstring for exercise_b5

5. Remove duplicates
Fokus: beda cara di unsorted vs sorted.geeksforgeeks+1
•	Versi unsorted:
o	Fungsi remove_duplicates_unsorted(nums):
	Pakai set untuk menyimpan angka yang sudah pernah muncul.
	Loop list, hanya tambahkan angka ke hasil kalau belum ada di set.
o	Return list baru tanpa duplikat.
•	Versi sorted:
o	Fungsi remove_duplicates_sorted(nums):
	Asumsikan list sudah terurut.
	Jalan dengan satu loop dan pointer “tulis” (mirip solusi klasik).
	Modifikasi list di tempat, lalu return list yang sudah dipotong.geeksforgeeks
"""


"""
Fokus: beda cara di unsorted vs sorted.geeksforgeeks+1
•	Versi unsorted:
o	Fungsi remove_duplicates_unsorted(nums):
	Pakai set untuk menyimpan angka yang sudah pernah muncul.
	Loop list, hanya tambahkan angka ke hasil kalau belum ada di set.
o	Return list baru tanpa duplikat.
"""

sample_list_1 = [3, 3, 2, 1, 2, 4, 3]

def remove_duplicates_unsorted(nums):
    set_1 = set()
    new_list = []

    for num in nums:
        if num not in set_1:
            new_list.append(num)

        set_1.add(num)

    return new_list


#print(remove_duplicates_unsorted(sample_list_1))



"""
•	Versi sorted:
o	Fungsi remove_duplicates_sorted(nums):
	Asumsikan list sudah terurut.
	Jalan dengan satu loop dan pointer “tulis” (mirip solusi klasik).
	Modifikasi list di tempat, lalu return list yang sudah dipotong.geeksforgeeks
"""
sample_list_2 = [1,1,2,2,3,3,3,5]

def remove_duplicates_sorted(nums):
    nums_length = len(nums)
    last_unique_num = None
    write_index = 0

    for i in range(nums_length):
        current_num = nums[i]
        
        if(current_num != last_unique_num):
            last_unique_num = current_num
            nums[write_index] = last_unique_num

            write_index += 1
    
    return nums[:write_index:1]
    

print(remove_duplicates_sorted(sample_list_2))
        

