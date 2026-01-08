"""
Docstring for v1.Level 3.Exercise E.1
    E. Latihan NumPy dasar (opsional tapi direkomendasikan)
1. Dasar array NumPy
•	Install dan import: import numpy as np, lalu buat beberapa array dengan np.array() dari list Python (1D dan 2D).numpy
•	Cek atribut penting: darray.shape, ndarray.ndim, ndarray.dtype, dan ndarray.size.numpy

"""

import numpy as np

test_list = [1,2,4]
test_list2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

np_arr = np.array(test_list2)

#Attribute Shape
print(np_arr.shape)

#Attribute Dimension
print(np_arr.ndim)

#Attribute data type
print(np_arr.dtype)

#Attribue numpy array size
print(np_arr.size)
