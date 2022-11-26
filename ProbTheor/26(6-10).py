import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def s(X):
    n = len(X)
    Y = X - np.mean(X)
    l = Y.dot(Y)
    return l / (n - 1)


def F(X):  # эмпирическое распределение
    n = len(X)
    return np.array(list(range(0, n))) / n


norm_numb_0_1_159 = np.array( [0.464, 0.137, 2.455, -0.323, -0.068, 0.296, -0.288, 1.298, 0.06, -2.256, -0.531, -0.194, 0.543, -1.558, 0.187,
    -1.19, 1.486, -0.354, -0.634, 0.697, 0.926, 1.375, 0.785, -0.963, 1.022, -0.472, 1.279, 3.521, 0.571, -1.851,
    0.194, 1.192, 1.394, -0.555, 0.046, 0.321, 2.945, 1.974, -0.259, 0.412, 0.906, -0.513, -0.525, 0.595, 0.881,
    0.934, 1.579, 0.161, 1.179, -1.055, 0.007, 0.769, 0.971, 0.712, 1.09, -0.631, -1.501, -0.488, -0.162, -0.136,
    1.033, 0.203, 0.448, 0.74, -0.69, 0.756, -1.618, -0.345, -0.511, -2.051, -0.457, -0.218, 1.372, 0.225, 0.378,
    0.761, 0.181, -0.738, 0.06, -1.53, -0.482, 1.678, -0.057, -1.229, -0.486, 0.856, -0.491, -1.983, -1.376, -1.15,
    1.356, -0.561, -0.256, -0.212, 0.219, 0.779, -1.01, 0.598, -0.918, 1.598, 0.085, 0.415, -0.169, 0.313, 0.005,
    -0.899, 0.012, -0.725, 1.147, -0.121, 1.096, 0.181, 1.393, -1.163, -0.911, 1.231, -0.199, -0.246, 1.239, -4.361,
    -0.261, 1.237, 1.046, -0.508, -1.63, -0.146, -0.392, -0.105, -0.357, -1.384, 0.36, -0.992, -0.116, -1.698, -2.832,
    1.339, 1.827, -0.959, 0.424, 0.969, -1.141, -1.041, 0.362, 1.041, 0.535, 0.731, 1.377, 0.983, -1.33, 1.62, -1.04,
    0.279, -2.056, 0.717, -0.873, -1.096, -1.396, 1.047, 0.089] ) # C1 c.312 len = 159

norm_numb_05_1_159 = norm_numb_0_1_159 + 0.5
norm_numb_05_1_50 = norm_numb_05_1_159[0:50]
norm_numb_05_1_100 = norm_numb_05_1_159[0:100]
norm_numb_05_1_150 = norm_numb_05_1_159[0:150]

variation_series_05_1_50 = np.array(sorted(norm_numb_05_1_50))  # сортировка в вариоционный ряд
variation_series_05_1_100 = np.array(sorted(norm_numb_05_1_100))
variation_series_05_1_150 = np.array(sorted(norm_numb_05_1_150))

print('50:', variation_series_05_1_50, '\n',
      '100:', variation_series_05_1_100, '\n',
      '150:', variation_series_05_1_150)

arange_05_1_50 = np.mean(variation_series_05_1_50)  # среднее
arange_05_1_100 = np.mean(variation_series_05_1_100)
arange_05_1_150 = np.mean(variation_series_05_1_150)

print('50:', arange_05_1_50, '100:', arange_05_1_100, '150:', arange_05_1_150)
# 50: 0.8645200000000002 100: 0.6372899999999999 150: 0.5734066666666666

s_05_1_50 = s(variation_series_05_1_50)
s_05_1_100 = s(variation_series_05_1_100)
s_05_1_150 = s(variation_series_05_1_150)

print('50:', s_05_1_50, '100:', s_05_1_100, '150:', s_05_1_150)
# 50: 1.2803936424489795 100: 1.113296612020202 150: 1.211420712706935

plt.plot(variation_series_05_1_50, F(variation_series_05_1_50), label='50')
plt.plot(variation_series_05_1_100, F(variation_series_05_1_100), label='100')
plt.plot(variation_series_05_1_150, F(variation_series_05_1_150), label='150')
plt.plot(variation_series_05_1_150, norm(loc=0.5, scale=1).cdf(variation_series_05_1_150), label='N(0.5, 1)')
plt.title('Эмпирические функции распределения для разных n')
plt.grid(True)
plt.legend()
plt.show()

plt.hist(variation_series_05_1_50, label='50', density=True, histtype='stepfilled', alpha=0.5)
plt.hist(variation_series_05_1_100, label='100', density=True, histtype='stepfilled', alpha=0.5)
plt.hist(variation_series_05_1_150, label='150', density=True, histtype='stepfilled', alpha=0.5)
plt.plot(variation_series_05_1_150 + 0.5, norm.pdf(variation_series_05_1_150), label='N(0.5, 1)')
# plt.xlim(-0.5, 0.5)
plt.title('Плотность распределений для разных n')
plt.grid(True)
plt.legend()
plt.show()
