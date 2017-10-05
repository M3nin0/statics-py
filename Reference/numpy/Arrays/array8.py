# Repetindo array com tile
# tile permite repetir arrays em torno dos eixos

import numpy as np

arr = np.array([1, 2, 3])

'''
Sintaxe (Não utiliza axis)
np.tile(array, quantidade de repetições)
'''

np.tile(arr, 2)

arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

np.tile(arr2, 3)