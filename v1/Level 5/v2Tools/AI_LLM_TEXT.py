"""
Docstring for v2Tools.AI_LLM_TEXT

AI LLM summarise and grammar checks

"""

from .AI_LLM_API_CALLER import call_perp
from .AI_LLM_API_CALLER import call_gemini

def ringkasan_bahasa_ai(text):
    prompt = f"Ringkas teks berikut dalam bahasa Indonesia: ringkasin yg simpel aja nggk masuk akal juga gpp! yg penting ada hasil!\n\n{text}\n"
    return call_gemini(prompt=prompt)

def grammar_check_ai(text):
    prompt = (f"Perbaiki grammar kalimat ke kalimat bahasa Inggris dengan grammar benar ," 
              f"kalimat yg dibawah ini nggk masuk akal jug gpp karena user prompt jawaban ny yg simpel aja sesuai bentuk kalimat jgn panjang panjang ya:\n\n{text}")
    return call_gemini(prompt=prompt)


if(__name__=="__main__"):
    print(grammar_check_ai("teh manis sejuk sejuk sejuk"))