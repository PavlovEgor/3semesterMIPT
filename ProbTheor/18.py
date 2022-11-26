import scipy.special
from scipy.stats import norm
import numpy as np

p = 1 / 500
q = 1 - p
N = 50


def C(k, n=N):
    return scipy.special.comb(n, k)


def pq(i):
    return p**(i) * q**(N - i)


def F(x):
    return norm(loc=0, scale=1).cdf(x)


def P(m):
    lam = N * p
    return (lam ** m ) * np.exp(-lam) / scipy.special.factorial(m, exact=True)


x = 1 - C(50, 0) * pq(0) - C(1) * pq(1) - C(2) * pq(2)
print('Bin: ', x * 1e4, ' *10^-4')

x = 1 - P(0) - P(1) - P(2)
print('Pois: ', x * 1e4, ' *10^-4')


x = (3 - N * p) / ((N * p * q) ** 0.5)
prob = 1 - F(x)
print('Gauss: ', prob * 1e4, ' *10^-4')
