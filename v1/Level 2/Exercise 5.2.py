"""
Docstring for Exercise 5.2
o	Program yang menerima string kalimat dan:
	Mengubah semua ke huruf kecil.
	Menghapus spasi di awal/akhir.
	Menghitung jumlah kata (pakai split()).

"""
kalimat2 = "   Hari ini   saya makan NASI goreng  "
kalimat2 = kalimat2.lower()

kalimat_strip = kalimat2.strip()
kata_list = kalimat_strip.split()

jumlah_kata = len(kata_list)
hasil = " ".join(kata_list)


print("END")
