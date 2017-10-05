# Concatenando arrays
import numpy as np

'''
Sintaxe

np.concatenate((array_a, array_b), axis = eixo)
'''

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
c = np.concatenate((a, b), axis = 0)
print(c)

a = np.array([[3, 2], [8, 9]])
b = np.array([[1, 6]])
c = np.concatenate((a, b.T), axis = 1)
print(c)

# b.T -> Transposta, assim consigo concatenar matrizes com linhas e colunas diferentes.