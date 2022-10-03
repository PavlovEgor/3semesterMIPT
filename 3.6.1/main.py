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
    # ax = np.linspace(0, max(list(x)), 10)
    plt.plot(x, theoretical_curve(x, param[0]), label=r'')


def theoretical_curve(x):
    a = 1.2
    return a * abs((np.sin(np.pi * tau * (x - nu_0)) / (np.pi * (x - nu_0))) - (np.sin(np.pi * tau * (x + nu_0)) / (np.pi * (x + nu_0))))


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
    global tau
    # plt.errorbar(x, y, xerr=0.1, yerr=0.2, fmt='o', c='tab:red', markersize=1)
    plt.plot(x, y, '-o', c='tab:red', markersize=1, label='сигнал')
    # approx_curve(x, y)
    plt.xlim(left=-5e-1)
    plt.ylim(bottom=0)
    plt.plot(x, theoretical_curve(x),  label=r'формула (6)')
    plt.ylabel('Произведение A*B, B')
    plt.xlabel('Частота, kГц')
    plt.title('Спектр цугов \n $\\nu_0 = {} \\;$ кГц,$ \\tau = {} $ мкс, $f = {} \\;$ кГц'.format(nu_0, tau * 1e3, f))
    plt.legend()
    # plt.grid(True)


files_address = r'C:\Users\User\Documents\3 семестр\ЭлеМагЛабы\3.6.1\EgorKate\IIIA8B19data2KHZ'  # address of txt files
tau = 100 * 1e-3
nu_0 = 30
f = 2
files = get_file_names(files_address)


x = get_massive(files_address + r'\\' + files[0])[0]
y = get_massive(files_address + r'\\' + files[0])[1]

for file in files[1::]:
    x += get_massive(files_address + r'\\' + file)[0]
    y += get_massive(files_address + r'\\' + file)[1]

curve(x / len(files), y / len(files))


plt.show()


