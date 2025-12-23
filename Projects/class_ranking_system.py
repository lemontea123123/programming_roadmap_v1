"""
Docstring for v1.Level 2.Exercise 9.1
9.	Project 2 – Sistem penilaian kelas
o	Input:
	Jumlah siswa.
	Untuk tiap siswa: nama dan nilai (0–100).
o	Simpan di list of dict, contoh: {"nama": "...", "nilai": 80}.
o	Hitung dan tampilkan:
	Rata rata nilai kelas.
	Nilai tertinggi & terendah + nama siswanya.
	Jumlah siswa lulus (>= 60) dan gagal.
"""

def hitung_rata(list_angka):
    panjang_list = len(list_angka)

    if panjang_list == 0:
        return 0
    
    total = 0

    for angka in list_angka:
        total = total + angka
    
    rata = total / panjang_list

    return rata


def user_loading():
    print("Press Anything To Continue...")
    input()


def input_nomor(dialog="Input Angka Yang Benar: "):
    print(dialog)
    loop = True
    user_input= None

    while loop:
        try :
            user_input = float(input())
            loop = False
        except ValueError:
            print("Tolong Input Angka Yang Benar!")

    return user_input


jumlah_siswa = int(input_nomor("Input Jumlah Siswa: "))
list_siswa = []


for i in range(jumlah_siswa):
    print("\nInput Nama Siswa Ke-",i+1)
    nama_siswa = input()
    nilai_siswa = input_nomor("Input Nilai Siswa")
    siswa = {}
    siswa["nama"] = nama_siswa
    siswa["nilai"] = nilai_siswa
    list_siswa.append(siswa)

#Ambil smua nilai sisa
nilai_list = []

for i in range(len(list_siswa)):
    siswa = list_siswa[i]
    nilai_siswa = siswa["nilai"]
    nilai_list.append(nilai_siswa)

rata_nilai = hitung_rata(nilai_list)

nilai_lulus = []
nilai_gagal = []

for nilai in nilai_list:
    if nilai >= 60:
        nilai_lulus.append(nilai)
    else:
        nilai_gagal.append(nilai)

print("Rata Nilai: ",rata_nilai)
print("Jumlah Murid Lulus: ",len(nilai_lulus))
print("Jumlah Murid Gagal: ",len(nilai_gagal))



#Syarat ny list siswa harus lebih dr 1 siswa dong
if len(list_siswa)>1:
    for i1 in range(len(list_siswa)):
        times = len(list_siswa) - i1 -1
        for i2 in range(times):
            current_index = i2
            next_index = i2+1

            current_siswa = list_siswa[current_index]
            next_siswa = list_siswa[next_index]

            current_siswa_nilai = current_siswa["nilai"]
            current_siswa_nama = current_siswa["nama"]

            next_siswa_nilai = next_siswa["nilai"]
            next_siswa_nama = next_siswa["nama"]

            #Flags
            flag_swap1 = current_siswa_nilai < next_siswa_nilai
            flag_tie = current_siswa_nilai == next_siswa_nilai
            flag_urutan = current_siswa_nama > next_siswa_nama
            flag_swap2 = flag_tie and flag_urutan

            if flag_swap1 or flag_swap2:
                list_siswa[current_index]=next_siswa
                list_siswa[next_index]=current_siswa
else:
    print("Nothing To Sort!")

#Print Rankings!!!
for index , siswa in enumerate(list_siswa):
    print(index+1,". ",siswa["nama"]," ",siswa["nilai"])
