"""
Docstring for v1.Level 2.Exercise 8.1
8.	Project 1 – Analisis teks sederhana
Buat program analisis teks di terminal:
o	Input: satu paragraf teks dari user.
o	Output:
	Jumlah karakter (tanpa spasi).
	Jumlah kata.
	5 kata yang paling sering muncul beserta jumlahnya.
o	Gunakan dict untuk menyimpan frekuensi kata.
"""

def filter_string(string_param , filter):
    hasil = ""
    for huruf in string_param:
        flag = huruf in filter
        if not flag:
            hasil += huruf

    return hasil


sample = "Belajar algoritma dan struktur data memang tidak selalu mudah. Kadang kita merasa pusing, bosan, atau bingung. Namun, dengan latihan rutin dan contoh soal yang cukup, algoritma dan struktur data akan terasa jauh lebih masuk akal."
sample1 = "satu dua satu dua satu"
sample3 = "Di dunia pemrograman, banyak orang memulai dengan rasa penasaran dan sedikit rasa takut. Seiring waktu, rasa takut itu perlahan berubah menjadi rasa percaya diri, terutama ketika mereka berhasil menyelesaikan masalah yang sebelumnya terasa mustahil. Latihan yang konsisten, eksperimen kecil, dan belajar dari kesalahan sendiri membuat perkembangan terasa nyata dari hari ke hari."
sample4 = "Dalam perjalanan belajar pemrograman, banyak orang merasa ragu di awal karena melihat contoh kode yang tampak rumit dan penuh istilah asing. Padahal, hampir semua programmer berpengalaman pernah berada di titik yang sama, yaitu tidak mengerti apa-apa dan sering melakukan kesalahan yang sama berulang kali. Perbedaannya adalah, mereka memutuskan untuk terus mencoba, bertanya ketika bingung, dan tidak menyerah hanya karena satu atau dua bug yang sulit ditemukan. Seiring waktu, konsep yang awalnya terasa membingungkan seperti variabel, fungsi, dan struktur data mulai terlihat lebih masuk akal. Latihan rutin, proyek kecil yang relevan dengan kehidupan sehari-hari, dan kebiasaan untuk membaca dokumentasi membuat kemampuan berpikir logis berkembang secara perlahan namun pasti. Pada akhirnya, pemrograman bukan hanya tentang menulis kode yang berjalan tanpa error, tetapi juga tentang membangun cara berpikir yang terstruktur, sabar dalam memecahkan masalah, dan berani bereksperimen dengan solusi baru yang mungkin belum pernah dicoba sebelumnya."



tanda_baca = [",", ".", "!", "?", ";", ":"]

#Filter tanda baca dari sampel!
hasil = filter_string(sample4 , tanda_baca)

hasil = hasil.lower()
hasil_kata_list = hasil.split()
hasil_tanpa_spasi = filter_string(hasil,[" "])

jumlah_karakter = len(hasil_tanpa_spasi)
jumlah_kata = len(hasil_kata_list)
dict_kata = {}

for kata in hasil_kata_list:
    try:
        dict_kata[kata] += 1
    except KeyError:
        dict_kata[kata] = 1

list_dict_kata = list(dict_kata.items())
for i1 in range(len(dict_kata)):
    times = len(dict_kata) - i1 -1
    for i2 in range(times):
        curr_index = i2
        next_index = i2 + 1

        curr_entri_tup = list_dict_kata[curr_index]
        next_entri_tup = list_dict_kata[next_index]
        
        curr_entri_kata = curr_entri_tup[0]
        curr_entri_jumlah = curr_entri_tup[1]

        next_entri_kata = next_entri_tup[0]
        next_entri_jumlah = next_entri_tup[1]

        #Banding Jumlah hanya dipindah maju kalau jumlah ny sedikit atau jika tie banding urutan kata ny setelah
        flag_swap = curr_entri_jumlah < next_entri_jumlah
        flag_tie = curr_entri_jumlah == next_entri_jumlah
        flag_urutan = curr_entri_kata > next_entri_kata
        flag_swap2 = flag_tie and flag_urutan
       
        # Jika jumlah ny sama maka banding urutan kata ny langsung
        if flag_swap or flag_swap2:
            list_dict_kata[curr_index] = next_entri_tup
            list_dict_kata[next_index] = curr_entri_tup



print("Jumlah Karakter :",jumlah_karakter)
print("Jumlah Kata :",jumlah_kata)

for i in range(5):
    try:
        entri = list_dict_kata[i] 
        kata = entri[0]
        jumlah = entri[1]
        print(i+1,". ",kata ," x",jumlah)
    except IndexError:
        break

print("test")

