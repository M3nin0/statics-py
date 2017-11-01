import numpy as np
import matplotlib.pyplot as plt

class Unipy():
    def um1801(self):
        x1 = np.linspace(0,2 * np.pi, 60) # Maior quantidade de dados
        x2 = np.linspace(0,2 * np.pi, 6)
        plt.plot(x1, np.sin(x1), x2, np.sin(x2))
