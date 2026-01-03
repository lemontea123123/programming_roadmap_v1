"""
Docstring for v2Tools.AI_LLM_TEXT

AI LLM summarise and grammar checks

"""

from AI_LLM_API_CALLER import *

def ringkasan_bahasa_ai(text):
    prompt = f"Ringkas teks berikut dalam bahasa Indonesia:\n\n{text}\n"
    return call_gemini(prompt=prompt)

def grammar_check_ai(text):
    prompt = f"Perbaiki grammar kalimat bahasa Inggris berikut, lalu tampilkan versi yang sudah benar:\n\n{text}"
    return call_gemini(prompt=prompt)