import matplotlib.pyplot as plt
import numpy as np
import math


'''Спираль Гаусса (херня)'''
class vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def sum(self, v2):
        return vector(self.x + v2.x, self.y + v2.y)


    def rott(self):
        return vector(self.y, -self.x)


num = vector(7, 23)
direct = vector(1, 0)
AllPoints = []
SimplPoints = []
F = {2, 3, 5, 7, 521, 11, 523, 13, 17, 19, 23, 29, 541, 31, 547, 37, 41, 43, 557, 47, 563, 53, 569, 59, 571, 61, 577, 67, 71, 73, 587, 79, 593, 83, 599, 89, 601, 607, 97, 101, 613, 103, 617, 107, 619, 109, 113, 631, 127, 641, 131, 643, 647, 137, 139, 653, 659, 149, 661, 151, 157, 673, 163, 677, 167, 683, 173, 179, 691, 181, 701, 191, 193, 197, 709, 199, 719, 211, 727, 733, 223, 227, 739, 229, 743, 233, 239, 751, 241, 757, 761, 251, 257, 769, 773, 263, 269, 271, 787, 277, 281, 283, 797, 293, 809, 811, 307, 821, 311, 823, 313, 827, 317, 829, 839, 331, 337, 853, 857, 347, 859, 349, 863, 353, 359, 877, 367, 881, 883, 373, 887, 379, 383, 389, 907, 397, 911, 401, 919, 409, 929, 419, 421, 937, 941, 431, 433, 947, 439, 953, 443, 449, 967, 457, 971, 461, 463, 977, 467, 983, 479, 991, 997, 487, 491, 499, 503, 509}
for i in range(100):
    if num.x == 0:
        if (num.y - 3) % 4 == 0 and num.y in F:
            direct = direct.rott()
            SimplPoints.append(num)
            num = num.sum(direct)
            AllPoints.append(num)
        else:
            num = num.sum(direct)
            AllPoints.append(num)
    elif num.y == 0:
        if (num.x - 3) % 4 == 0 and num.x in F:
            direct = direct.rott()
            SimplPoints.append(num)
            num = num.sum(direct)
            AllPoints.append(num)
        else:
            num = num.sum(direct)
            AllPoints.append(num)
    else:
        if num.x**2 + num.y**2 in F:
            direct = direct.rott()
            SimplPoints.append(num)
            num = num.sum(direct)

            AllPoints.append(num)
        else:
            num = num.sum(direct)
            AllPoints.append(num)
X, Y, sX, sY = [], [], [], []

for i in range(len(AllPoints)):
    X.append(AllPoints[i].x)
    Y.append(AllPoints[i].y)

for i in range(len(SimplPoints)):
    sX.append(SimplPoints[i].x)
    sY.append(SimplPoints[i].y)

print(AllPoints)
plt.plot(X, Y)
plt.plot(sX, sY, '*')
plt.show()