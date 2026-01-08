"""
Docstring for Exercise B.5
5.	Script 2 – Ringkasan teks via API
•	Buat script ringkas_teks.py yang:
o	Minta input teks panjang dari user (bisa input() berulang atau paste di terminal).
o	Menyusun prompt: "Ringkas teks berikut dalam bahasa Indonesia:\n\n<teks user>".
o	Memanggil call_ai() dan menampilkan hasil ringkasan.
•	Tambahan kecil: kalau teks lebih dari N karakter (misal 500), print peringatan “Teks cukup panjang, ini hanya ringkasan singkat”.
"""


from AI_LLM_API_CALLER import call_gemini

def multi_line_input(dialog="Input Teks Panjang , Enter dua kali untuk akhiri",batas_kata=30):
    user_input = []
    line =""
    loop = True
    length = 0
    batas = batas_kata

    print(dialog)
    while loop:
        line = input()
        user_input.append(line)
        if(line==""):
            loop=False

        length = len(line)+length

        if(length>=batas):
            print("Teks sudah melebihi jumlah batas kata")
            break

    paragraph = "\n".join(user_input)
    return paragraph

paragraph = multi_line_input(dialog="Tulis Apapun" , batas_kata=30)

def ringkasan_ai(text):
    prompt = f"Ringkas teks berikut dalam bahasa Indonesia:\n\n{text}\n"
    return call_gemini(prompt=prompt)



