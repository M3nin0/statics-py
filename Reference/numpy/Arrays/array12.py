# Obtendo elementos do array através de indexação booleana

import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6]])

# Imprimindo certos tipos de valores

# Imprimir apenas os maiores que 3
print(arr[arr > 3])

# Imprimindo todos os valores maiores que 1
print(arr[arr > 1])

# Verificando se as expressões retornadas
idx = (arr > 2)
print(idx)