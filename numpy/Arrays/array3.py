import numpy as np

# Arrays do numpy trabalham com referência
# Para fazer cópia utilize o .copy()

# Fatiando em um array
arr = np.array([[10, 20], [30, 40]])
arr2 = arr[:]
arr2[0] = 333

print('Primeiro array')
print(arr[:])

print('Segundo array')
print(arr2[:])

# Para isso não ocorrer utilize o copy()
c = a.copy()
print(c)