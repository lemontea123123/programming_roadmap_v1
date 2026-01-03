"""
Docstring for Exercise B.6
6.	Script 3 – Koreksi grammar (Bahasa Inggris)
•	Buat script grammar_check.py yang:
o	Minta kalimat Inggris dari user.
o	Prompt: "Perbaiki grammar kalimat bahasa Inggris berikut, lalu tampilkan versi yang sudah benar:\n\n<kalimat>".
o	Panggil call_ai() dan print versi yang diperbaiki.
•	Opsional: tampilkan juga kalimat asli dan yang sudah diperbaiki dalam format rapi.
"""

from v2Tools.multi_line_input import *
from AI_LLM_API_CALLER import call_gemini

user_input = multi_line_input(dialog="Ketik Dalam Bahasa Inggris",batas_kata=50)

def grammar_check_ai(text):
    prompt = f"Perbaiki grammar kalimat bahasa Inggris berikut, lalu tampilkan versi yang sudah benar:\n\n{text}"
    return call_gemini(prompt=prompt)

