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
    plt.errorbar(x, y, xerr=x*0.015, yerr=0.05, fmt='o', c='tab:red', markersize=1)
    plt.plot(x, y, 'o', c='tab:red')
    approx_curve(x, y)
    plt.xlim(left=0)
    plt.ylim(bottom=0)
    plt.ylabel('Отклонение от начального напряжения \n на образце, отн. ед')
    plt.xlabel(r'Квадрат индукции в катушке $B^2$, мТл$^2 \cdot 10^{4}$')
    plt.title('Зависимость напряжения на образце \n от поля электромагнита, k = 0.26')
    # plt.legend()
    plt.grid(True)



file_address = r'C:/Users/User/Documents/3 семестр/ЭлеМагЛабы/3.3.6/disk.txt' # address of txt files

U_0 = 0.732
B = get_massive(file_address)[0]
B_2 = (B * B) / 1e4
U = get_massive(file_address)[1]
Y = (U - np.array([U_0]*len(U))) / U_0

curve(B_2, Y)
plt.show()
