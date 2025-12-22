"""
Docstring for v1.Level 2.Exercise 6.2
o	Program yang menghitung frekuensi setiap kata dalam kalimat pendek (dipisah spasi).
"""



sample1 = "   belajar python itu seru dan belajar git itu juga seru dan bermanfaat   "
sample1_list = sample1.strip().split()
dict_test={}


for kata in sample1_list:
    try:
        dict_test[kata] = dict_test[kata] + 1
    except KeyError:
        dict_test[kata] = 1

for kata , jumlah in dict_test.items():
    print(kata,": ",jumlah)

    


