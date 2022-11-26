import numpy as np
import matplotlib.pyplot as plt


countries = ['Brazil', 'Madagascar', 'S. Korea', 'United States', 'Ethiopia', 'Pakistan', 'China', 'Belize']

# Уровень рождаемости на 1000 населения.
birth_rate = [16.4, 33.5, 9.5, 14.2, 38.6, 30.2, 13.5, 23.0]

# Ожидаемая средняя продолжительность жизни при рождении, в г.
life_expectancy = [73.7, 64.3, 81.3, 78.8, 63.0, 66.4, 75.2, 73.7]

# Доход на душу населения, определенный в 2000 г. в долл. США.
GDP = np.array([4800, 240, 16700, 37700, 230, 670, 2640, 3490])


fig, ax = plt.subplots()

# Некоторые произвольно выбираемые цвета:
colors = range(len(countries))

ax.scatter(birth_rate, life_expectancy, c=colors , s=GDP/20)

ax.set_xlim(5, 45)
ax.set_ylim(60, 85)

ax.set_xlabel('Birth rate per 1000 population')
ax.set_ylabel('Life expectancy at birth (years)')


plt.show()