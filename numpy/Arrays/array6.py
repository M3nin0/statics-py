import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6]])

# Deletando sub-arrays (Linhas)
arr = np.delete(arr, 1, 0)

# Deletando sub-arrays (Colunas)
np.delete(arr, 0, 1)

arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
arr2

# Deletando sub-arrays através de passos
# Neste exemplo: Passo 2

'''
Sintaxe
np.delete(array, np.s_[PASSOS], EIXO)
'''

arr2 = np.delete(arr2, np.s_[::2], 0)
arr2