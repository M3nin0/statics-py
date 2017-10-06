# Filtro de dataset

import pandas as pd
import pydataset as pyds

# Carregando os dados
titanic = pyds.data('titanic')

# Verificando a quantidade de bytes que estão sendo usadas
titanic['class'].nbytes

# Medindo tempo
titanic['class'] == '3rd class'

# Transformando os dados em dados categóricos
# Abaixo transformo apenas a coluna class em category
titanic['class'] = titanic['class'].astype('category')
