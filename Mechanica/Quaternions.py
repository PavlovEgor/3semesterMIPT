import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation


class quaternion():

    def __init__(self, a=0, b=1, c=0, d=0): # a + bi + cj + dk
        self.real = a
        self.i = b
        self.j = c
        self.k = d
        self.vec = np.array([b, c, d])
        self.norm = (a**2 + b**2 + c**2 + d**2)
        self.mod = (self.norm**0.5)
        self.arg = np.arccos(a / (self.mod))

    def sum(self, q2):
        a = self.real + q2.real
        b = self.i + q2.i
        c = self.j + q2.j
        d = self.k + q2.k

        return quaternion(a, b, c, d)

    def mult(self, q): # h * q порядок важен
        h = self
        a = h.real * q.real - h.vec.dot(q.vec)
        v = h.real * q.vec + q.real * h.vec + np.cross(h.vec, q.vec)
        return quaternion(a, *v)

    def conj(self):
        return quaternion(self.real, *(-self.vec))

    def rot(self, q):
        qh = (q.mult(self))
        _q = q.conj()
        qh_q = qh.mult(_q)
        return qh_q

    def get_arg_and_vec(self, arg, vec=np.array([1, 0, 0])):
        vec = vec / (np.linalg.norm(vec))
        vec *= np.sin(arg)
        a = np.cos(arg)
        self.arg = arg
        self.real = a
        self.vec = vec
        self.i = vec[0]
        self.j = vec[1]
        self.k = vec[2]

# начальное состояние
ex = quaternion(0, 1, 0, 0)
ey = quaternion(0, 0, 1, 0)
ez = quaternion(0, 0, 0, 1)
q = quaternion()

# поворот на 60 градусов вокруг ОХ
q.get_arg_and_vec(np.pi / 6, ex.vec)

ex = ex.rot(q)
ey = ey.rot(q)
ez = ez.rot(q)

h = quaternion(q.real, *q.vec) # запоминаем в переменную

# поворот на 90 градусов вокруг новой ОY
q.get_arg_and_vec(np.pi/4, ey.vec)

ex = ex.rot(q)
ey = ey.rot(q)
ez = ez.rot(q)

h = q.mult(h)
# поворот на 60 градусов вокруг новой OZ
q.get_arg_and_vec(np.pi/6, ez.vec)

ex = ex.rot(q)
ey = ey.rot(q)
ez = ez.rot(q)
h = q.mult(h)

print(ex.vec, ey.vec, ez.vec) # полученный базис
# h = q3 * q2 * q1 - если умножим на него получим этот же поворот

ex = quaternion(0, 1, 0, 0)
ey = quaternion(0, 0, 1, 0)
ez = quaternion(0, 0, 0, 1)

ex = ex.rot(h)
ey = ey.rot(h)
ez = ez.rot(h)

print(ex.vec, ey.vec, ez.vec) # проверяе совпадение с предыдущим принтом

print(h.arg, h.vec /  (np.linalg.norm(h.vec))) # половинный угол поворота и направляющие косинусы оси
print(np.arccos((2 ** 0.5) / 4), (3/7)**0.5, (1/7)**0.5, (3/7)**0.5) # ответ из учебника