# Plotando alguns gráficos
import numpy as np
import matplotlib.pyplot as plt

salario = np.array([100, 200, 300, 500, 400, 150])

# Paramêtros
# plt.plot(VALORES A SEREM FEITOS O PLOT, c='COR', ls='estilo da linha', marker='tipo marker', ms = tamanho do marker)

plt.plot(salario, 'r--', marker='s', ms=6)
plt.show()