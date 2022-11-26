import matplotlib.pyplot as plt
import numpy as np


"""Семенную шапку подсолнечника"""
fi = (1 + 5**0.5)/2
N = np.linspace(1, 1000, 1000)
r = N ** 0.5
theta = 2 * np.pi * N / fi

plt.polar(theta, r, 'o', color='0.')
plt.title('Упаковка шапки подсолнечника')
plt.show()