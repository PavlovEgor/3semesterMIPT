import matplotlib.pyplot as plt


"""Риск смерти в Британии"""
age = [1, 5, 15, 25, 35, 45, 55, 65, 75, 85, 90]
women = [277, 5376, 10417, 4132, 2488, 1106, 421, 178, 65, 21, 7]
men = [177, 4386, 8333, 1908, 1215, 663, 279, 112, 42, 15, 6]

plt.plot(age, women, 'o', linestyle='--', color='0.5', label='women')
plt.plot(age, men, 'o', linestyle='-.', color='0.', label='men')
plt.legend(fontsize=20.)
plt.title('Риск смерти')
plt.xlabel('Возрастная группа',  fontsize=12.)
plt.ylabel(r'Риск $1 / N$',  fontsize=12.)
plt.show()