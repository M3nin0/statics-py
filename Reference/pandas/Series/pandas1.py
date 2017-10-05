import pandas as pd

# Criando uma serie de numeros
# A série é um dado de uma única dimensão
s = pd.Series([1, 4, 6, 5, 7, 10, 6])

# Exibindo o valor e seus indices
# Perceba que a manipulação dos dados é feita de forma igual as listas
print(s)

# Recuperando uma pequena descrição que os dados dentro da serie pode apresentar
print(s.describe())

# Verificando se algum valor está duplicado
print(s.duplicated())

# Adicionando mais series a uma serie
# No exemplo visto abaixo os indices não são sobrescrito, assim há dois indices 0, por exemplo
s2 = pd.Series([11, 5, 8])
s.append(s2)
