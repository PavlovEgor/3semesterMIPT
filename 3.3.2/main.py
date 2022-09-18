import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os


"""

"""

files = os.listdir(r'C:\Users\User\Documents\3 семестр\ЭлеМагЛабы\3.3.2')


def line(x, a, b):
    return a * (x) + b


def get_massive(fileName, flag):
    file = open(fileName)
    m = file.readlines()
    n = len(m[0].split())
    G = [[] for _ in range(n)]
    mist = []
    f = 0
    for s in m:
        d = s.split()
        print(d)
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


def correction_curve():
    I = np.array(get_massive(r'C:\Users\User\Documents\3 семестр\ЭлеМагЛабы\3.3.2\1.58A.txt', 'B'))
    U = np.array(get_massive(r'C:\Users\User\Documents\3 семестр\ЭлеМагЛабы\3.3.2\1.58A.txt', 'I'))
    #plt.errorbar(x, y, xerr= (5 / 1006), yerr=yerr, label=r'R = 100 Ом', fmt='o', c='tab:red', markersize=0)
    #plt.errorbar(IR0, BR0, xerr=5 / 1006, yerr=BR02, label=r'R = 0 Ом', fmt='o', c='black', markersize=0)
    x = U ** (3 / 2)
    y = I
    plt.errorbar(x, y, xerr=(0.1 / abs(U)), yerr=0, label=r'R = 100 Ом', fmt='o', c='tab:red', markersize=1)
    param, param_cov = curve_fit(line, x[16:], y[16:])
    ax = np.linspace(min(list(x)), max(list(x)), 10)
    plt.plot(ax, line(ax, param[0], param[1]), label=r'интерполяция')
    #plt.plot(ax, ax, '--', label=r'теория')
    #print(param[0])
    plt.grid(True)
    # plt.xlim(left=0)
    # plt.ylim(bottom=0)
    plt.xlabel(r"Логарифм напряжения, $\ln{U}$")
    plt.ylabel(r'Логарифм силы тока, $\ln{I}$')
    plt.title('Вольт-амперная характеристика, $I_n = 1.58 A$')
    plt.text(-0.5, 7, '$k = {}$, по напряжению\n с {} В по {} В'.format(round(param[0], 3), U[16], U[-1]), fontsize=15)
    # print(param[0])



correction_curve()
plt.show()
