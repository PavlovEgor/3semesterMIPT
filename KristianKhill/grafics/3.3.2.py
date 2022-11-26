import matplotlib.pyplot as plt
import numpy as np
import math


"""Потенциал Ленарда-Джонса"""
A = 1.024e-23
B = 1.582e-26
x = (2 * B / A) ** (1 / 6) #minpoint ->0.38
y = (B / (x**12)) - (A / (x**6))
rg = 0.06
s = np.linspace(x - rg, x + rg + 0.4, 10)
sy = 0*s
r = np.linspace(x - rg, x + rg + 0.4, 1001)
r_2 = np.linspace(x - rg + 0.0414, x + rg+ 0.4, 1001)
U = (B / (r**12)) - (A / (r**6))
F = (B * 12 / (r_2**13)) - (6 * A / (r_2**7))
print(x, y)

line1 = plt.plot(r, U, label=r'$U(r) = \frac{B}{r^{12}} - \frac{A}{r^{6}}$', color='0.')
plt.ylabel('Потенциал Ленарда-Джонса')
plt.xlabel('Расстояние между атомами, нм')

plt.twinx()
line2 = plt.plot(r_2, F, label=r'$F(r) = \frac{12B}{r^{13}} - \frac{6A}{r^{7}}$', color='r')
plt.ylabel('Сила Ленарда-Джонса')
#plt.legend()

lines = line1 + line2
labels = []
for line in lines:
 labels.append(line.get_label())

plt.legend(lines , labels)
plt.grid()

plt.show()
