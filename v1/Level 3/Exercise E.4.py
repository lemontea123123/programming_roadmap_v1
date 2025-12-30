"""
Docstring for v1.Level 3.Exercise E.4
4. Operasi vektor & statistik
•	Latihan operasi element wise: +, -, *, /, **, np.add, np.multiply di dua array dengan ukuran sama.resagratia+1
•	Hitung np.sum, np.mean, np.max, np.min, np.std di seluruh array dan per axis (axis=0 dan axis=1).wesmckinney+1
"""

import numpy as np

test_list = [1,2,3]
test_list2 = [4,5,6]
test_matrix3 = np.arange(1,13).reshape(4,3)

np_arr = np.array(test_list)
np_arr2 = np.array(test_list2)

#Operations + = * / **
print("+ : ",np_arr+np_arr2)
print("- : ",np_arr-np_arr2)
print("* : ",np_arr*np_arr2)
print("/ : ",np_arr/np_arr2)
print("** : ",np_arr**np_arr2)

#Operations np.add np.multiply
print("Add :",np.add(np_arr , np_arr2))
print("Multiply :",np.multiply(np_arr , np_arr2))

print("\nMatrix:\n",test_matrix3)

#Kalkulasi Matrix
#Sum Axis 0 & Axis 1
print("Sum")
print("All:\n",np.sum(test_matrix3))
print("Axis: 0\n",np.sum(test_matrix3,axis = 0))
print("Axis: 1\n",np.sum(test_matrix3,axis = 1))

print("\nMatrix:\n",test_matrix3)
#Mean Axis 0 & Axis 1
print("Mean")
print("All:\n",np.mean(test_matrix3))
print("Axis: 0\n",np.mean(test_matrix3,axis = 0))
print("Axis: 1\n",np.mean(test_matrix3,axis = 1))

print("\nMatrix:\n",test_matrix3)
#Max Axis 0 & Axis 1
print("Max")
print("All:\n",np.max(test_matrix3))
print("Axis: 0\n",np.max(test_matrix3,axis = 0))
print("Axis: 1\n",np.max(test_matrix3,axis = 1))

print("\nMatrix:\n",test_matrix3)
#Min Axis 0 & Axis 1
print("Min")
print("All:\n",np.min(test_matrix3))
print("Axis: 0\n",np.min(test_matrix3,axis = 0))
print("Axis: 1\n",np.min(test_matrix3,axis = 1))

print("\nMatrix:\n",test_matrix3)
#Std Axis 0 & Axis 1
print("Std")
print("All:\n",np.std(test_matrix3))
print("Axis: 0\n",np.std(test_matrix3,axis = 0))
print("Axis: 1\n",np.std(test_matrix3,axis = 1))
