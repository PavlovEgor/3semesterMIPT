import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np


def approx_curve(x, y):
    param, param_cov = curve_fit(theoretical_curve, x, y)
    plt.plot(x, theoretical_curve(x, param[0]), label=r'аппроксимация')
    print(param[0])


def theoretical_curve(x, a):
    return a * x


def get_massive(file_name):
    file = open(file_name)  # открываем файл
    lines = file.readlines()[2:] # читаем, начиная с нужной строки

    date = [np.array(lines[0].split()).astype(np.float64)]

    for line in lines:
        values = np.array(line.split()).astype(np.float64)
        if not len(values):
            break
        date = np.append(date, [values], axis=0)

    file.close()

    return np.transpose(date)  # матрица: строки и столбцы как в транспонированном файле


def curve(x, y):  # paint of Date
    plt.errorbar(x, y, xerr=0.01, yerr=0.01, fmt='o', c='tab:red', markersize=1)
    plt.plot(x, y, 'o', c='tab:red')
    # approx_curve(x[:5:], y[:5:])
    # plt.xlim(left=0)
    # plt.ylim(top=0)
    plt.ylabel('Поток Ф, мВб')
    plt.xlabel('Ток I, A')
    plt.title('Зависимость потока через веберметр \n от сылы тока на источнике')
    # plt.legend()
    plt.grid(True)

# r'C:\Users\User\Documents\3 семестр\ЭлеМагЛабы\3.4.1\Wtoward.txt'


file_address = r'C:/Users/User/Documents/3 семестр/ЭлеМагЛабы/3.4.1/correctCurve.txt' # address of txt files

mu0 = 4 * np.pi * 1e-7
# d = 3.2
# L = 90 - 6.15
d = 0.81
S = np.pi * (d / 2) ** 2 * 1e-4
g = 9.78
SN = 72 * 1e-4

I = get_massive(file_address)[0]
F = get_massive(file_address)[1] - get_massive(file_address)[2]



curve(I, F)
plt.show()
