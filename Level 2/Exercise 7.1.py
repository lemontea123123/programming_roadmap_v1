"""
Docstring for v1.Level 2.Exercise 7.1
o	Diberi list nilai ujian (0–100), buat list:
	Nilai lulus (>= 60).
	Nilai gagal (< 60).
"""

list_nilai = [30, 55, 60, 75, 80, 45, 90]
nilai_lulus = []
nilai_gagal = []

for nilai in list_nilai:
    if nilai >= 60 :
        nilai_lulus.append(nilai)
    elif nilai < 60 :
        nilai_gagal.append(nilai)

print(nilai_lulus)
print(nilai_gagal)

