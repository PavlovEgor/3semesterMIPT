import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-1, 1, 1000)
y = np.exp(5*x)

fig, ax = plt.subplots()
ax.set_yscale('log')
ax.plot(x, y, color='tab:red', ls=':')
plt.show()