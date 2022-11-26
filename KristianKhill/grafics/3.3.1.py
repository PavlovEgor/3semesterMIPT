import matplotlib.pyplot as plt
import numpy as np
import math

"""Спирали в полярных координатах"""

def SpiraArchimed(a=0, b=2):
    theta = np.linspace(0, 8 * np.pi, 1000)
    r = a + b * theta
    plt.polar(theta, r, linestyle='--', color='0.', label=r'$r = a + b\theta$, a = {}, b = {}'.format(a, b))
    plt.title('Архимедова спираль')


def SpiraMirabilis(a=1.1684223846194647258528389332448):
    theta = np.linspace(0, 8 * np.pi, 1000)
    r = a**theta
    plt.polar(theta, r, linestyle='--', color='r', label=r'$r = c^\theta, c = {}$'.format(round(a, 2)))
    plt.title('Чудесная спираль')

SpiraArchimed()
SpiraMirabilis()
plt.legend(fontsize=12., loc=8)
plt.show()