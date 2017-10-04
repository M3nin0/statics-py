# Repetindo elementos de um array

import numpy as np

arr = np.array([[1, 2], [3, 4]])

'''
Sintaxe
np.repeat(array, quantidade de vezes que será repetido)
'''

np.repeat(arr, 2)

# Repetindo em eixo específico (0)
np.repeat(arr, 2, axis = 0)

# Repetindo em eixo específico (1)
np.repeat(arr, 2, axis = 1)