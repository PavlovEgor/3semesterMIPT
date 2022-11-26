import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation



class Quaternion:

    def __init__(self, a=0, b=1, c=0, d=0):  # a + bi + cj + dk
        self.real = a
        self.i = b
        self.j = c
        self.k = d
        self.vec = np.array([b, c, d])  # мнимая часть
        self.norm = (a ** 2 + b ** 2 + c ** 2 + d ** 2)  # норма
        self.mod = (self.norm ** 0.5)  # модуль
        self.arg = np.arccos(a / self.mod)  # угол

    def sum(self, q):  # сложение квантернионов
        a = self.real + q.real
        b = self.i + q.i
        c = self.j + q.j
        d = self.k + q.k
        return Quaternion(a, b, c, d)

    def mult(self, q):  # h * q порядок важен
        h = self
        a = h.real * q.real - h.vec.dot(q.vec)
        v = h.real * q.vec + q.real * h.vec + np.cross(h.vec, q.vec)
        return Quaternion(a, *v)

    def conj(self):  # сопряженный
        return Quaternion(self.real, *(-self.vec))

    def rot(self, q):  # вращение относительно вектора на угол
        qh = (q.mult(self))
        _q = q.conj()
        qh_q = qh.mult(_q)
        return qh_q

    def get_arg_and_vec(self, arg, vec=np.array([1, 0, 0])):  # составить квантернион по углу и вектору
        vec = vec / (np.linalg.norm(vec))
        vec *= np.sin(arg)
        a = np.cos(arg)
        self.arg = arg
        self.real = a
        self.vec = vec
        self.i = vec[0]
        self.j = vec[1]
        self.k = vec[2]


class EulerAngles:

    def __init__(self, psi=0, phi=0, teta=0, psidot=0, phidot=0, tetadot=0):
        self.psi = psi
        self.phi = phi
        self.teta = teta
        self.psidot = psidot
        self.phidot = phidot
        self.tetadot = tetadot

    def omega(self):
        p = self.psidot * np.sin(self.teta) * np.sin(self.phi) + self.tetadot * np.cos(self.phi)
        q = self.psidot * np.sin(self.teta) * np.cos(self.phi) - self.tetadot * np.sin(self.phi)
        r = self.phidot + self.psidot * np.cos(self.teta)


class MomentOfInertia:

    def __init__(self, A, B, C, D=0, E=0, F=0):
        self.tenz = np.array([[A, -E, -D], [-E, B, -F], [-D, -F, C]])
        self.diag = np.array([A, B, C])

