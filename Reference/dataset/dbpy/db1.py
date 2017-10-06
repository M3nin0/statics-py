# Importando dados de DB's
from db import DB

'''
Sintaxe
DB(filename='caminho/nome_do_banco', dbtype='tipo_do_banco')
'''

# Carregando o banco
database = DB(filename='logs.sqlite3', dbtype='sqlite')

# Exibindo informações
database.tables

# Puzando os dados do db
log_df = database.tables.log