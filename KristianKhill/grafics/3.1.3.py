import matplotlib.pyplot as plt
import numpy as np
import math


'''Распределения Гаусса'''
sigma = np.linspace(1, 2, 3)
lines = ['--', ':', '-.']
x = np.linspace(-10, 10, 1001)
y = []
A = 1 / ((2 * math.pi) ** 0.5)
for i in range(len(sigma)):
    y.append((A / sigma[i]) * np.exp((-1) * x**2 / (2 * (sigma[i] ** 2))))

for i in range(len(sigma)):
    plt.plot(x, y[i], label=r'$\sigma = {}$'.format(sigma[i]), linestyle=r'{}'.format(lines[i]))

plt.legend()
plt.show()
