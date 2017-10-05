# Dividindo arrays

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

'''
Sintaxe
np.array_split(array, quantidade de divisões)

'''

# Dividindo no eixo 0
np.array_split(arr, 2, axis = 0)

# Dividindo no eixo 1
np.array_split(arr, 2, axis = 1)

# É possivel atribuir os valores a várias variaveis
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

# Gerando lista de arrays
arrays = np.array_split(arr2, 2, axis = 0)

# Iterando a lista para recurperar os arrays
for array in arrays:
    print(array)