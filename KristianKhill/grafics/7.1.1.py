import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(num='Population density', #название
                 #figsize=(4.5, 2.), # Кортеж размеров рисунка (width, height) – к сожалению, только в дюймах
                 #facecolor='red', # Цвет фона рисунка
                 #dpi=100., # Разрешение рисунка в точках на дюйм. Не трогать
                 edgecolor='red') # Цвет границ рисунка. что-то не работает
ax = fig.add_subplot()


x = np.linspace(-2, 2, 10)
line_cosh, = ax.plot(x, np.cosh(x), c=(0.3, 1., 0.), marker='v',
                     markerfacecolor=(0., 0.5, 0.5),
                     markeredgecolor=(1., 0., 0.))

line_quad, = ax.plot(x, 1 + x**2 / 2, c='tab:purple', marker='^')

ax.set_xlim(left=-2, right=2) # Установлены границы оси x: от -1 до 2. Можно записать картежем (-1, 2)
ax.set_ylim(bottom=1, top=4) # ymin=1: график будет "отсечен" по нижней границе bottom. Если top < bottom, то график переворачивается
line_quad.set_dashes([2, 4, 8, 4, 2, 4]) # Шаблон точка-штрих-точка.
#ax.yaxis.grid(True)
#ax.grid(True)
ax.xaxis.grid(True , which='minor', c='b')
plt.show()