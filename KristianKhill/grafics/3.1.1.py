import matplotlib.pyplot as plt
import numpy as np
import math
'''Строит два неограниченных графика'''

x = np.linspace(-20, 20, 1001)
y_1 = np.log(1 / np.cos(x) ** 2)
y_2 = np.log(1 / np.sin(x) ** 2)
plt.plot(x, y_1, label=r'$\ln(1 / \cos^2(x))$', )
plt.plot(x, y_2, label=r'$\ln(1 / \sin^2(x))$')
plt.legend()
plt.show()