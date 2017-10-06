# Utilizando dados importados do pydataset
import pandas as pd
import pydataset as data

# Visualizando a estrutura dos datasets importados
data.data()

# Importando os dados do titanic
titanic = data.data('titanic')

# Exibindo os 5 primeiros elementos do dataframe
titanic.head()

# Exibindo os 5 últimos elementos do dataframe
titanic.tail()

# Descrevendo o dataframe
titanic.describe()

# Calculando valores de uma coluna específica
titanic['class'].value_counts()