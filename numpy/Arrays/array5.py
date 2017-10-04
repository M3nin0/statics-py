import numpy as np

arr = np.array([1, 2, 3])

# Anexando elementos ao final do array
arr = np.append(arr, [[4, 5, 6]])

# Anexando a um eixo específico (axis = 0)
arr = np.append(arr, [[7, 8, 9]])

print(arr)