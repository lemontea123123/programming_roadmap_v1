"""
Docstring for Exercise A3
3.	API key & environment variable (konsep)
•	Pelajari konsep: apa itu API key, kenapa tidak boleh ditulis langsung di code yang dishare.apxml+1
•	Latihan: set 1 environment variable dummy, misal MY_API_KEY=abc123, lalu di Python baca dengan os.getenv("MY_API_KEY") dan print.
"""


import os

print(os.getenv("MY_API_KEY"))