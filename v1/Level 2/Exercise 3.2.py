"""
o	Counting:
	Hitung berapa banyak kemunculan angka tertentu di list (tanpa count() dulu).
	Hitung berapa banyak huruf vokal dalam sebuah string
a, i, u, e, o


"""

list_nama_orang = [
    "Andi",
    "Budi",
    "Cici",
    "Deni",
    "Eka",
    "Fani",
    "Gita",
    "Hadi",
    "Intan",
    "Joko",
    "Fani"
]

def hitung(list_nama_orang,nama_cari):
    count = 0
    for nama in list_nama_orang:
        if nama == nama_cari:
            count = count + 1

    return count

hitungan=hitung(list_nama_orang,"Fani")

seri_vokal=["a", "i", "u", "e", "o"]

def hitung_vokal(string_test):
    string_lowered = string_test.lower()
    panjang = len(string_test)

    total_count = 0

    for index in list(range(panjang)):
        huruf = string_lowered[index]
        
        if huruf in seri_vokal:
            total_count = total_count + 1


    return total_count

hitungan = hitung_vokal("Belajar Python itu seru dan menantang, tapi kalau sabar hasilnya kerasa banget.")

print("End")