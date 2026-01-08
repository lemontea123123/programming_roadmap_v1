"""
Docstring for exercise_a1
A. Latihan dasar konsep (wajib)
1. Review struktur data utama
Latihan ini tujuannya mengulang cara pakai list, string, dict, set dengan sengaja.
•	Buat list angka, lalu:
o	Tambah elemen baru di akhir.
o	Hapus elemen tertentu (misal angka 3).
o	Cari apakah angka tertentu ada di list (pakai in).
•	Buat string, lalu:
o	Ambil substring (misal 2 karakter pertama dan terakhir).
o	Ubah ke huruf besar/kecil.
o	Hitung berapa kali huruf tertentu muncul.
•	Buat dict frekuensi_huruf dari string pendek (misal "hello world"), isi manual, lalu print key dan valuenya satu per satu.
•	Buat set dari list dengan elemen duplikat (misal [1,2,2,3,3,3]) untuk menghilangkan duplikat, lalu bandingkan panjang list asli vs set.dev
"""

range_1 = list(range(1,10,1))
range_1.append(10)

range_1.remove(3)

print(range_1)
print(2 in range_1)


#String
string_sample = "Lemon Tea"
string_1 = string_sample[0:2] + string_sample[-2:]
string_1_lower = string_1.lower()
string_1_dict = {}

for character in string_1_lower:
    try:
        string_1_dict[character] = string_1_dict[character]+1
    except KeyError:
        string_1_dict[character] = 1

for entry in string_1_dict.items():
    letter = entry[0]
    times = entry[1]
    print(letter," => ",times)

list_sample_1 = [1,2,2,3,3,3]
set_sample_1 = set(list_sample_1)

print(set_sample_1)
print("list_sample_1 length => ",len(list_sample_1))
print("set_sample_1 length => ",len(set_sample_1))
        


