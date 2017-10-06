# Realizando Filtro / Seleção em um DataFrame

import pandas as pd

# Importando os dados
copacabana = pd.read_csv('C:\\Users\\Felipe\\Documents\\statics-py\
\Reference\\pandas\\DataFrames\\copacabana.csv', delimiter=';')

# Carregando as colunas do dataset (O pandas transforma em dataset ao importar)
# print(copacabana.columns)

# Realizando a descrição de uma coluna específica
# print(copacabana['Quartos'].describe())

# Retornando apenas os quartos maiores que 5
# copacabana['Quartos'] > 5

# Busca utilizando o loc
maior = copacabana.loc[copacabana['Quartos'] == 6]

# Buscando valor que esteja entre 3 e 5
medio = copacabana.loc[copacabana['Quartos'] > 3 ]