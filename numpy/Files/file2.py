# Tratando dados que faltam
import numpy as np

var1, var2, var3 = np.genfromtxt('C:\\Users\\Felipe\\Documents\\
statics-py\\numpy\\Files\\dados2.txt', skip_header=1, unpack=1, filling_values=999)