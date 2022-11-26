import matplotlib.pyplot as plt
import numpy as np


'''Кинетика мономолекулярной реакции: A -> B + C'''
t = np.linspace(0, 0.015, 1001)
k_1, k_2 = 300, 100
A_0 = 2.0
A = A_0 * np.exp((-t) * (k_1 + k_2))
B = (k_1 / (k_1 + k_2)) * A_0 * (1 - np.exp((-t) * (k_1 + k_2)))
C = (k_2 / (k_1 + k_2)) * A_0 * (1 - np.exp((-t) * (k_1 + k_2)))

plt.plot(t, A, label=r'$[A]$',  linestyle='-', color='0.')
plt.plot(t, B, label=r'$[B]$',  linestyle='--', color='0.33')
plt.plot(t, C, label=r'$[C]$',  linestyle='--', color='0.67')
plt.title('Кинетика мономолекулярной реакции')
plt.xlabel('Время, $c$',  fontsize=12.)
plt.ylabel('Концентрация субстрата, $M$',  fontsize=12.)
plt.legend()
plt.show()