import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os
import numpy as np


def get_file_names(files_address):
    all_files_names = os.listdir(files_address)
    txt_files_names = []
    for name in all_files_names:
        if ".txt" in name:
            if os.path.getsize(files_address + r'\\' + name):
                txt_files_names.append(name)
    return txt_files_names


def approx_curve(x, y):
    param, param_cov = curve_fit(theoretical_curve, x, y)
    ax = np.linspace(0, max(x), 3)
    plt.plot(ax, theoretical_curve(ax, param[0]), label=r'')
    print(param)


def theoretical_curve(x, a):
    return a * x


def get_massive(file_name):
    file = open(file_name)  # открываем файл
    lines = file.readlines()[4:] # читаем, начиная с нужной строки

    date = [np.array(lines[0].split()).astype(np.float64)]

    for line in lines:
        values = np.array(line.split()).astype(np.float64)
        if not len(values):
            break
        date = np.append(date, [values], axis=0)

    file.close()

    return np.transpose(date)  # матрица: строки и столбцы как в транспонированном файле


def curve(x, y):  # paint of Date
    # global tau
    # plt.errorbar(x, y, xerr=0.1, yerr=0.2, fmt='o', c='tab:red', markersize=1)
    plt.plot(x, y, 'o', c='tab:orange')
    plt.xlim(left=0)
    plt.ylim(bottom=0)
    plt.ylabel(r'Отношение средней гармоники к боковой')
    plt.xlabel(r'Глубина модуляции $m$')
    plt.title('Зависимость спектра модулированного \n сигнала от глубины модуляции, k = 0.506')
    # plt.title('Спектр импульсных сигналов \n $\\nu_0 = 1 \\;$ кГц,$ \\tau = {} $ мкс'.format(tau * 1e3))
    # plt.legend()
    plt.grid(True)


files_address = r'C:\Users\User\Documents\3 семестр\ЭлеМагЛабы\3.6.1'  # address of txt files
files = get_file_names(files_address)

A_max = get_massive(files_address + r'\\' + files[0])[3]
A_min = get_massive(files_address + r'\\' + files[0])[4]
osc_max = get_massive(files_address + r'\\' + files[0])[1]
osc_min = get_massive(files_address + r'\\' + files[0])[2]

x = (A_max - A_min) / (A_max + A_min)
y = osc_min / osc_max
curve(x, y)
approx_curve(x, y)
plt.show()
