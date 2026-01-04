"""
Docstring for Exercise B.4
4.	Script 1 – Text generation sederhana
•	Buat fungsi call_ai(prompt: str) -> str yang:
o	Mengirim POST ke endpoint dummy (misal https://api.example-llm.com/v1/chat/completions atau yang kamu pakai beneran nanti).
o	Mengirim headers Authorization: Bearer <API_KEY> dan Content-Type: application/json.
o	Mengirim JSON body sederhana: { "model": "nama-model", "messages": [{"role": "user", "content": prompt}] }.apxml+1
•	Untuk sekarang, kalau belum punya API asli, cukup tulis struktur kodenya dan comment bagian endpoint/key (fokus ke bentuk request).


"""

import os
import requests
import json

url = "https://api.perplexity.ai/chat/completions"

perplexity_key = os.getenv("PERPLEXITY_KEY")
gemini_key = os.getenv("GEMINI_API_KEY")

def call_gemini(prompt):
    url = (
        "https://generativelanguage.googleapis.com/v1beta/"
        "models/gemini-2.5-flash-lite:generateContent"
        f"?key={gemini_key}"
    )

    headers={
        "Content-Type":"application/json"
    }

    content={
        "contents":[
            {
                "parts":[
                    {
                    "text":prompt
                    }
                ]
            }
        ]
    }

    respond = requests.post(url,headers=headers,json=content)
    response_text = respond.json()["candidates"][0]["content"]["parts"][0]["text"]

    return response_text



def call_perp(prompt):

    header = {
        "Authorization":f"Bearer {perplexity_key}",
        "Content-Type":"application/json"
    }

    body = {
        "model":"sonar-pro",
        "messages": [
            {
                "role":"user",
                "content":prompt
            }
        ]
    }

    respond = requests.post(url,headers=header,json=body)

    #print(respond.status_code)
    #print(respond.reason)

    response_text = respond.json()["choices"][0]["message"]["content"]

    #print(response_text)
    #Extract Text
    return response_text


if(__name__=="__main__"):
    call_gemini("Namakan saya top 10 nba players sekarang")





