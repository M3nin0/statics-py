import numpy as np

# Criando as listas de pontos
joao_pts = [20, 30, 40, 15]
pedro_pts = [100, 24, 48, 23]
maria_pts = [92, 22, 34, 12]
marcos_pts = [12, 34, 12, 43]

# Criando um array com os valores
pontos = np.array([joao_pts, pedro_pts, maria_pts, marcos_pts])

# Criando um array com valores de 0 até 19
my_data = np.arange(0, 20)
print(my_data)

# Transformando o array acima em uma matriz
# Para isso utilize a função reshape(arr, (x, y))
mat1 = np.reshape(my_data, (5, 4))
print(mat1)