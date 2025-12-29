"""
Docstring for v1.Level 3.Exercise E.2
2. Membuat array cepat
•	Latihan fungsi pembuat array: np.zeros(), np.ones(), np.full(), np.arange(), np.linspace().datacamp+1
•	Buat “grid” angka, misalnya matriks 3×3 berisi 1–9, lalu reshape dengan arr.reshape().
"""
import numpy as np

# A list of zeroes
print(np.zeros(10))

# A list of ones
print(np.ones(10))

#A list of n
print(np.full(5,1))

# A range from a to b with steps
print(np.arange(1,10,2))

# A range from a to b with specified amounts of levels in between
print(np.linspace(1,10,20))

# A 3x3 Matrix of range from 1 to 9
print(np.reshape(np.arange(1,10),(3,3),order="C"))



