import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np


def approx_curve(x, y):
    param, param_cov = curve_fit(theoretical_curve, x, y)
    plt.plot(x, theoretical_curve(x, param[0]), label=r'аппроксимация')
    print(param[0])


def theoretical_curve(x, a):
    return a * x


def curve():  # paint of Date
    plt.xlim(left=0)
    plt.ylim(bottom=0)
    plt.ylabel('Сила поля $F_M$, нH')
    plt.xlabel('$B_0^2 S / 2 \mu_0$, Н')
    plt.title('Функция силы магнитного поля $F_M$ \n от приложенного поля $B_0$ для графита')
    plt.text(1, 2700, '$\chi = 425 \pm 8 \; \cdot 10^{-6}$')
    plt.legend()
    plt.grid(True)


x2 = np.array([0.08009033203125009, 0.08009033203125009, 0.47856445312499996, 1.2814453125, 3.6311176757812493, 6.265001953125, 8.188000488281247, 10.489855957031244, 13.213283203124998, 14.716845703124998]
)
y2 = np.array([156.48, 156.48, 410.76, 762.8399999999999, 1467.0, 1897.32, 2180.94, 2542.7999999999997, 2836.2, 3227.3999999999996])


x1 = np.array([0.08009033203125009, 0.08009033203125009, 0.47856445312499996, 1.2814453125, 2.278125, 3.6311176757812493, 4.956345703125, 6.265001953125, 8.188000488281247, 10.489855957031244, 13.213283203124998, 14.716845703124998]
)
y1 = np.array([88.02, 88.02, 342.29999999999995, 674.8199999999999, 1017.1199999999999, 1408.32, 1691.9399999999998, 1897.32, 2278.74, 2640.6, 3178.5, 3413.22])


plt.errorbar(x1, y1, xerr=0.02 * x1, yerr=9.78, fmt='o', c='tab:red', markersize=1)
plt.plot(x1, y1, 's', c='tab:red', label='по увеличению')

plt.errorbar(x2, y2, xerr=0.02 * x2, yerr=9.78, fmt='o', c='tab:orange', markersize=1)
plt.plot(x2, y2, 'o', c='tab:orange', label='по уменьшению')

plt.plot(x1[:6:], theoretical_curve(x1[:6:], 425), label=r'аппроксимация')
curve()
plt.show()