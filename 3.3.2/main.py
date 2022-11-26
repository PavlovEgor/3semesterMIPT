import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os


"""

"""

files = os.listdir(r'C:\Users\User\Documents\3 семестр\ЭлеМагЛабы\3.3.2')


def line(x, a):
    return a * x


def get_massive(fileName, flag):
    file = open(fileName)
    m = file.readlines()
    n = len(m[0].split())
    G = [[] for _ in range(n)]
    f = 0
    for s in m:
        d = s.split()
        if d == []:
            f = 1
            continue
        if f == 0 or flag == 'I':
            for i in range(n):
                G[i].append(float(d[i]))
        elif flag == 'B':
            for i in range(n):
                G[i].append(float(d[i]) * 1000)

    file.close()
    if flag == 'I':
        return np.array(G[0])

    if flag == 'B':
        return (np.array(G[1]))

k = []
def correction_curve(fileName):
    I = np.array(get_massive(r'C:\Users\User\Documents\3 семестр\ЭлеМагЛабы\3.3.2\{}'.format(fileName), 'B'))
    U = np.array(get_massive(r'C:\Users\User\Documents\3 семестр\ЭлеМагЛабы\3.3.2\{}'.format(fileName), 'I'))
    x = U[16:] ** (3 / 2)
    y = I[16:]
    plt.errorbar(x, y, xerr=(0.1 * (3/2) * (U[16:] ** 0.5)), yerr=0, fmt='o', c='tab:red', markersize=1)
    param, param_cov = curve_fit(line, x, y)
    ax = np.linspace(0, max(list(x)), 10)
    plt.plot(ax, line(ax, param[0]), label=r'$I = {}$, k = {}'.format(fileName[:-4], round(param[0], 3)))
    k.append(param[0])



print(files)
for name in files:
    if name[-1] != 't':
        continue
    correction_curve(name)
    print(name)

plt.xlabel(r"$U^{3/2}$")
plt.ylabel(r'Сила тока, мкА')
plt.title('Вольт-амперная характеристика')
plt.grid(True)
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.legend()
plt.show()

ra = 9.5
eps0 = 8.85 * 1e-12
l = 9
a1 = 9 * ra * (k[3] * 1e-6)
a2 = 8 * np.pi * eps0 * l
a3 = (a1 / a2)**2
print(0.5 * a3 * 1e-11 * 0.16, 0.5 * a3 * 1e-11)




