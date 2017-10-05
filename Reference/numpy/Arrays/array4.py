# Inserindo elementos em um array

import numpy as np

arr = np.array([1, 2, 3])
print(arr.ndim)

# Inserindo elementos dentro do array
# np.insert(arr, 1 , 10)

a = np.array([[1, 2], [3, 4]])
print(a.ndim)

'''
[1, 2]
[3, 4]

Vertical (axis = 0)
[4, 6]

Horizontal (axis = 1)
[3, 7]
'''

# Soma vertical
print(a.sum(axis=0))

# Soma horizontal
print(a.sum(axis=1))

# Inserindo um elemento dentro do array no eixo 0
# np.insert(a, 1, 5, axis = 1)

# Inserindo um elemento dentro do array no eixo 1
np.insert(a, 1, [5, 2], axis = 0)