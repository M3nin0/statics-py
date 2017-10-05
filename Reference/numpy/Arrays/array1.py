import numpy as np

# Criando array
arr = np.array([10, 20, 30, 40])

# Criando array (N dimensões - Matriz)
mat = np.array([[1,2], [3, 4]])

# Acessando os elementos do array

## Linhas
#print(mat[0, :])

## Colunas
#print(mat[:, 0])

# Transpondo matriz

# print('Sem transpor')
# print(mat)

# print('Transpondo')
# print(mat.transpose())

# Operações com matrizes

m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])

# Soma
print(m1 + m2)

# Subtração
print(m1 - m2)

# Multiplicação 
print(m1 * m2)

# Índice do maior valor
m1.argmax()

# Índice do menor valor
m1.argmin()