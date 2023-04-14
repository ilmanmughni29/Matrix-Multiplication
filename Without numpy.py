# Muhammad Ilman Mughni
# NPM: 2006537324
# Program perkalian matriks tanpa numpy

m = int(input('masukkan jumlah baris untuk matriks 1: '))
n = int(input('masukkan jumlah kolom untuk matriks 1: '))

matrix= [[0 for j in range(n)] for i in range(m)]

for i in range(0,m):
	for j in range(0,n):
		print('masukkan angka untuk baris', i+1, 'masukkan angka untuk kolom', j+1)
		matrix[i][j] = int(input())

print('Matriks 1: ')
print(matrix)

o = int(input('masukkan jumlah baris untuk matriks 2: '))
p = int(input('masukkan jumlah kolom untuk matriks 2: '))

matrix2 = [[0 for j in range(p)] for i in range(o)]

for i in range(0,o):
	for j in range(0,p):
		print('masukkan angka untuk baris', i+1, 'masukkan angka untuk kolom', j+1)
		matrix2[i][j] = int(input())

print('Matriks 2: ')
print (matrix2)

if o != n:
    print('jumlah kolom matriks 1 tidak sama dengan baris matriks 2')
          
if o == n:
	hasil = [[0 for j in range(p)] for i in range(m)]

	for i in range(len(matrix)):
		for j in range(len(matrix2[0])):
			for k in range(len(matrix2)):
				hasil[i][j] += matrix[i][k] * matrix2[k][j]
				
print ('\nhasilnya adalah:\n', hasil)
