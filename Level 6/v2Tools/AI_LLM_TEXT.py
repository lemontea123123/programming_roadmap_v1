"""
Docstring for v2Tools.AI_LLM_TEXT

AI LLM summarise and grammar checks

"""

from .AI_LLM_API_CALLER import call_perp
from .AI_LLM_API_CALLER import call_gemini

def ringkasan_bahasa_ai(text):
    prompt = f"Ringkas teks berikut dalam bahasa Indonesia: \n\n{text}\n\nRingkasin aja kmu nggk usah cerewet ssoalny ini user prompt , kalau minta summary kamu keluarin summary ny aja straight to the point"
    return call_perp(prompt=prompt)

def grammar_check_ai(text):
    prompt = (f"Perbaiki grammar kalimat ke kalimat bahasa Inggris dengan grammar benar ," 
              f"kalimat yg dibawah ini nggk masuk akal jug gpp karena user prompt jawaban ny yg simpel aja sesuai bentuk kalimat jgn panjang panjang ya:\n\n{text}")
    return call_gemini(prompt=prompt)


if(__name__=="__main__"):
    print(grammar_check_ai("teh manis sejuk sejuk sejuk"))