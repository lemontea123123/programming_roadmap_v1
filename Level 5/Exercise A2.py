"""
2.	Latihan requests dasar (Python)
•	Install dan test: pip install requests, lalu script sederhana GET ke https://httpbin.org/get dan print status_code + response.json().geeksforgeeks+1
•	Buat 2 script kecil:
o	Script 1: GET ke https://httpbin.org/get?nama=... dan print nilai parameter nama dari JSON.
o	Script 2: POST ke https://httpbin.org/post dengan JSON { "pesan": "halo" } dan print kembali datanya dari respons.

"""

import requests
import json

url = "https://httpbin.org/get"

response = requests.get(url)

params = {
    "nama":"Budi"
}

print("Status Code: ",response.status_code )
print("Response JSON:")
print(response.json())

response = requests.get(url,params = params)

data = response.json()

print(data)

print("URL yang dipanggil: " , data["url"] )
print("Args dari server: ",data["args"])
print("Nilai parameter 'name': ",data["args"]["nama"])

print("\n\n\n")
url = "https://httpbin.org/post"

payload = {
    "pesan":"halo"
}

response = requests.post(url,json=payload)

data = response.json()

print("Status Code: ",response.status_code)
print("JSON yg diterima server:")
print(data["json"])