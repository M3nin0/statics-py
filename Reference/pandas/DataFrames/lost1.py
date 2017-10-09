import pandas as pd
import numpy as np

# nan -> not a number

# Tratando o problema dos dados perdidos

dados = {
    'nomes': ['João', 'Maria', 'José', np.nan, 'Pedro', 'Judas', 'Tiago'],
    'sexo': ['M', 'F', 'M', 'np.nan', 'M', 'M', np.nan],
    'idade': [14, 13, np.nan, np.nan, 15, 13, 14],
    'nota': [4, 10, 7, np.nan, 8, 9, 7]
}

df = pd.DataFrame(dados)

# Criando um novo DataFrame e removendo seus nan
ndf = df.dropna()
# print(ndf)

# No caso acima removo todas as linhas que tem nan
# Mas não quero remover todas as linhas e sim aquelas em que todos os campos são nan
# Para isso deve-se usar:

# Abaixo especifico que as linhas excluidas serão aquelas que que tem todos os elementos nan 
df.dropna(how = 'all')

# Criando uma coluna nan
df['serie'] = np.nan
# print(df)

# Veja que no caso acima há uma coluna toda com valores nan e a forma normal do dropna
# não irá excluir a coluna, veja:
# print(df.dropna(how = 'all'))

# Para fazer isso é necessário específicar o axis, veja
# Lembrando axis = 0 -> Linha
#           axis = 1 -> Coluna

# print(df.dropna(how = 'all', axis = 1))

# Há ainda a possibilidade de colocar parâmetros para a exclusão
# Para isso será utilizado o thresh, neste parâmetro é possível específicar 
# Com quantos elementos perdidos a linha/coluna tem que conter para ser excluido
# Veja

# Abaixo toda linha que tiver três ou mais elementos perdidos será excluida
# print(df.dropna(thresh=3))

# Mas nem sempre é necessário remover os elementos
# Veja, abaixo vou preencher os campos nan da coluna 'serie' que estão vazios
# print(df['serie'].fillna(8))

# Será preenchido com 8, caso queira que a modificação seja efetiva
# Use dentro do fillna o inplace = True

# df['serie'].fillna(8, inplace = True)

# print(df)

# Preenchendo o campo de idade com media
df['idade'].fillna(df['idade'].mean(), inplace = True)

# Retornando todos os valores que estão dentro da espressão lógica 

df[df['nomes'].notnull() & df['sexo'].notnull()]