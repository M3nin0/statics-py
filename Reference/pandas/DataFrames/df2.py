import pandas as pd

# Criando um DataFrame com colunas nomeadas
# Isso é feito porque no exemplo df1.py, muitas adições numéricas sem saber
# o que eram cada uma foi utilizada

df = pd.DataFrame([['fchollet/keras', 11302], ['openai/universe', 4350], 
['pandas-dev/pandas', 8168]], columns = ['repository', 'stars'])

# Exibindo a estrutura do df
# print(df)

# Pegando elemento específico
# print(df['repository'][0])

# Calculando a média dos valores presentes na coluna 'starts'
# print('Media')
# print(df['stars'].mean())

# Calculando a mediana
# print('Mediana')
# print(df['stars'].median())

# Recuperando uma linha especifica
df.iloc[1]

# Perceba que o iloc retorna um dicionario, assim é possível recuperar elementos da linha
df.iloc[1]['stars']