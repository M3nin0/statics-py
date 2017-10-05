import pandas as pd

# DataFrame é uma matriz, ou seja, é uma tabela que possui linhas e colunas
# O dataframe abaixo contém informações sobre alguns repositórios e suas estrelas
df = pd.DataFrame([['fchollet/keras', 11302], ['openai/universe', 4350], ['pandas-dev/pandas', 6168]])

# Exibindo as dimensões do DataFrame
df.shape

# Exibindo o DataFrame completo
df

# Exibindo DataFrames (Elemento específico)
print(df[0][0])
print(df[1][0])