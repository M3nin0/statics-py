# Lendo arquivos com Numpy
import numpy as np

'''
Sintaxe
np.loadtxt('NOME DO ARQUIVO A SER LIDO', 
skiprows=quantas linhas irá pular para começar a ler os arquivos, 
unpack=Indica se as colunas devem ou não serem retornadas separadamente)
'''

var1, var2, var3 = np.loadtxt('C:\\Users\\Felipe\\Documents\\statics-py\\numpy\\Files\\dados.txt', skiprows=1,unpack=True)

print(var1)
print(var2)
print(var3)