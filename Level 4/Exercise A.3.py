"""
Docstring for v1.Level 4.Exercise A.3
3.	JSON dasar
o	Baca contoh JSON sederhana: objek dengan key-value (misal {"title": "Catatan 1", "done": false}).geeksforgeeks+1
o	Latihan di Python: buat dict, lalu ubah jadi JSON string dengan json.dumps() dan sebaliknya json.loads().
"""

import json

note = {
    "title": "Belajar JSON",
    "done": True,
    "length_minutes": 30
}

note_json = json.dumps(note ,indent=4)

print("Note Object")
print("Python dict: ",note)
print("JSON form: ",note_json)

json_str = '{"title": "Catatan 1", "content": "Belajar JSON dasar.", "done": false, "priority": 1}'

dict_1 = json.loads(json_str)

print("Catatan Object")
print("JSON string: ",json_str)
print("Python Dict: ",dict_1)
