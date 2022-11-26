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



file_address = r'C:/Users/User/Documents/3 семестр/ЭлеМагЛабы/3.3.6/palc_2.txt' # address of txt files

U_0 = 0.667
B = get_massive(file_address)[0]
B_2 = (B * B) / 1e4
U = get_massive(file_address)[1]
Y = (U - np.array([U_0]*len(U))) / U_0
print(list(B_2), '\n', list(Y))

B_2_disk = [0.009721959999999998, 0.009721959999999998, 0.31472100000000003, 1.136356, 2.274064, 3.7403560000000007, 5.8081, 8.0089, 11.6281, 13.7641, 14.7456]
Y_disk = [-0.0027322404371584725, -0.0027322404371584725, 0.09289617486338807, 0.3469945355191257, 0.6762295081967215, 1.0806010928961747, 1.6284153005464481, 2.162568306010929, 3.0081967213114753, 3.487704918032787, 3.6502732240437155]

B_2_palc_1 = [0.008028160000000001, 0.008028160000000001, 0.23232400000000003, 0.9960039999999999, 2.4837759999999998, 3.888784, 5.8081, 7.9524, 11.6964, 13.69, 14.44]
Y_palc_1 = [0.0, 0.0, 0.03225806451612889, 0.12756598240469202, 0.2771260997067448, 0.3958944281524925, 0.541055718475073, 0.6832844574780056, 0.8900293255131962, 0.9912023460410557, 1.030791788856305]

B_2_palc_2 = [0.009702249999999999, 0.009702249999999999, 0.34574399999999994, 1.2633760000000003, 2.4995609999999995, 4.3264, 6.7081, 8.7616, 12.1104, 13.7641, 14.5161]
Y_palc_2 = [0.001499250374812595, 0.001499250374812595, 0.01799100449775114, 0.05547226386806585, 0.10344827586206888, 0.16191904047976008, 0.2248875562218889, 0.27136431784107934, 0.3448275862068965, 0.3703148425787106, 0.3823088455772114]

plt.plot(B_2_disk, Y_disk, 'o', c='tab:red', label='диск Корбино')
plt.plot(B_2_palc_1, Y_palc_1, 's', c='tab:orange', label='пластина в положении №1')
plt.plot(B_2_palc_2, Y_palc_2, '^', c='tab:green', label='пластина в положении №2')
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.ylabel('Отклонение от начального напряжения \n на образце, отн. ед')
plt.xlabel(r'Квадрат индукции в катушке $B^2$, мТл$^2 \cdot 10^{4}$')
plt.title('Зависимость напряжения на образцах \n от поля электромагнита')
plt.legend()
plt.grid(which='minor', linestyle=':', color='0.9')
plt.grid(which='major', linestyle='-', color='0.8', linewidth=0.3)
plt.show()

x = abs(np.array(Y_disk) / np.array(B_2_disk))
print(np.std(x), x)