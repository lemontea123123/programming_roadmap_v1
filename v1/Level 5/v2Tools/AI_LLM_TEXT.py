"""
Docstring for v2Tools.AI_LLM_TEXT

AI LLM summarise and grammar checks

"""

from AI_LLM_API_CALLER import *

def ringkasan_bahasa_ai(text):
    prompt = f"Ringkas teks berikut dalam bahasa Indonesia: ringkasin yg simpel aja nggk masuk akal juga gpp! yg penting ada hasil!\n\n{text}\n"
    return call_perp(prompt=prompt)

def grammar_check_ai(text):
    prompt = f"Perbaiki grammar kalimat bahasa Inggris berikut, lalu tampilkan versi yang sudah benar:\n\n{text}"
    return call_gemini(prompt=prompt)