import matplotlib.pyplot as plt
import numpy as np
import math


'''Уравнение Михаэлиса–Ментен'''
V_max = 0.1
K_m = 0.04
S = np.linspace(0, 0.5, 1001)
y = V_max * S / (K_m + S)
plt.plot(S, y,  color='cyan', linestyle='--', linewidth=1., label=r'$\nu = \frac{V_{max} [S]}{K_m + [S]}$')
plt.title('Уравнение Михаэлиса–Ментен')
plt.xlabel('Концентрация субстрата $[S]$, $M$',  fontsize=12.)
plt.ylabel(r'Скорость реакции $\nu$, $M/c$',  fontsize=12.)
plt.legend(loc='center right', fontsize=20.)
plt.show()
