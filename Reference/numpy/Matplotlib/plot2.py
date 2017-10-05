import numpy as np
import matplotlib.pyplot as plt

salarios_joao = np.array([100, 200, 400, 300])
salarios_maria = np.array([500, 300, 500, 450])
salarios_ana = np.array([250, 150, 250, 225])

plt.plot(salarios_joao, 'r--', marker='s', ms=8, label='Salários João')
plt.plot(salarios_maria, 'b--', marker='^', ms=8, label='Salários Maria')
plt.plot(salarios_ana, 'b--', marker='o', ms=8, label='Salários Ana')

# Adicionando legenda
# plt.legend(loc = 'localização')
plt.legend(loc = 'upper left')

plt.show()