import pandas as pd

# Trabalhando com indices
# Indices: É uma forma de mapear os dados, para um valor único

# Declarando o DataFrame
df = pd.DataFrame(
    [
        ['PE', 'Pernambuco', 'Recife'], ['RJ', 'Rio de Janeiro', 'Rio de Janeiro'],
        ['PB', 'Paraíba', 'João Pessoa'], ['SP', 'São Paulo', 'São Paulo'],
        ['MG', 'Minas Gerais', 'Belo Horizonte'], ['CE', 'Ceará', 'Fortaleza'],
        ['AC', 'Acre', 'Rio Branco'], ['MA', 'Maranhão', 'São Luís'], ['RN', 'Rio Grande do Norte', 'Natal'],
        ['PR', 'Paraná', 'Curitiba'], ['RS', 'Rio Grande do Sul', 'Porto Alegre']
    ], columns=['Sigla', 'Nome', 'Capital']
)

# Exibindo todas as siglas
# print(df['Sigla'])

# Exibindo a quantidade de index
# print(df.index)

# Recuperando o índice 0 com iloc
# print(df.iloc[:3])

# Alterando o index padrão do DataFrame (Numérico)
# df.index = pd.Index([1, 2, 3, 4, 5, 6, 7 ,8, 9 , 10, 11])

# print('Novo indice')
# print(df)

# Colocando a sigla como um indice do df
df.index = df['Sigla']

# print('Novo indice')
# print(df)

# print(df.loc['PE'])

# Excluido a coluna Sigla, já que ela passou a ser o índice
del df['Sigla']
print(df)