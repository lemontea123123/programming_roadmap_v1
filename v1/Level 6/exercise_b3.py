"""
Docstring for exercise_b3
B. Latihan pola soal dasar (wajib)
3. Two Sum versi mudah
Kerjakan dalam beberapa tahap supaya polanya kebentuk.algo+1
•	Versi 1 (brute force):
o	Tulis fungsi two_sum_bruteforce(nums, target) yang:
	Cek semua pasangan indeks (i, j) dengan dua loop.
	Kalau nums[i] + nums[j] == target, return pasangan indeks tersebut.
o	Tes dengan beberapa contoh list dan target (misal [2,7,11,15], target=9).
•	Versi 2 (pakai dict / hash map):
o	Tulis fungsi two_sum_hash(nums, target):
	Loop sekali lewat list.
	Simpan angka yang sudah lewat ke dict: angka -> indeks.
	Untuk tiap angka sekarang, cek apakah target - angka sudah ada di dict.
o	Print juga berapa banyak iterasi yang dilakukan untuk membandingkan dengan brute force (pakai counter sederhana).interviewcoder
"""

#Versi 1 Brute Force
list_angka = [3, 7, 1, 9, 2, 6, 0, 8, 4, 5]

def two_sum_brute(list_angka,target):
    total_iterasi = 0
    result_tuple = None

    for i1 , angka_1 in enumerate(list_angka,0):
        current_angka = angka_1
        for i2 ,angka_2 in enumerate(list_angka):
            total_iterasi += 1
            print("total_iterasi = ",total_iterasi)

            if(i1 == i2):
                continue
            
            if((angka_1 + angka_2) == target):
                result_tuple = (i1,i2)
                return result_tuple
            
            

    return False

#Versi 2 (Pakai Dict/Hash Map)
def two_sum_hash(list_angka,target):
    total_iterasi = 0
    new_dict = {}
    #kombinasi_valid = []

    for i1 , angka in enumerate(list_angka):
        total_iterasi += 1
        print("total_iterasi = ",total_iterasi)
        try:
            #Jika angka sudah pernah di indeks
            new_dict[angka].append(i1)
        except KeyError:
            #Jika angka belum pernah di indeks
            new_dict[angka] = [i1]
        
        angka_dicari = target - angka
        list_i_angka_dicari = []

        try:
            #Jika angka_dicari sudh pernah di indeks
            list_i_angka_dicari = new_dict[angka_dicari]
        except KeyError:
            #Jika angka_dicari belum pernah di indeks
            continue

        #Dari list indeks cariin yg bukan indeks ini
        # i2 merupakan indeks dari indeks list dari angka_dicari
        for i2 in list_i_angka_dicari:
            total_iterasi += 1
            print("total_iterasi = ",total_iterasi)
            if(i2!=i1):
                #Ketemu indeks angka dicari!
                return (i1,i2)
                #kombinasi_valid.append((i1,i2))

    #return kombinasi_valid

print(two_sum_brute(list_angka=list_angka,target=17))
print(two_sum_hash(list_angka=list_angka,target=17))