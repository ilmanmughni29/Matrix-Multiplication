# Program perkalian matriks dengan numpy

import numpy as np

# syarat perkalian matriks:
# jumlah kolom di matriks 1 harus sama dengan jumlah baris di matriks 2
a = np.array ([[12, 5, 7], 
               [2, 9, 4]])
b = np.array ([[14, 9], 
               [9, 7],
               [2, 6]])

print('multiplication of two matrices is:\n')
print(np.dot(a,b))
