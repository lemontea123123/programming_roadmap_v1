"""
Docstring for Exercise 3.1
3.	Algoritma linear search & counting sederhana
o	Linear search: fungsi cari_indeks(lista, target) yang mengembalikan indeks pertama target atau -1 jika tidak ada.
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
]

def linear_search(list_nama,cari):
    
    for index,nama in list(enumerate(list_nama,0)):
        if nama==cari:
            return index
        
    return -1

linear_search(list_nama_orang,"Joko")