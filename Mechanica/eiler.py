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

        return np.array([p, q, r])

    def axis(self):
        kx = -np.sin(self.psi) * np.sin(self.teta)
        ky = np.cos(self.psi) * np.sin(self.teta)
        kz = np.cos(self.teta)
        return Quaternion(0, kx, ky, kz)


class MomentOfInertia:

    def __init__(self, A, B, C, D=0, E=0, F=0):
        self.tenz = np.array([[A, -E, -D], [-E, B, -F], [-D, -F, C]])
        self.diag = np.array([A, B, C])
        self.A = A
        self.B = B
        self.C = C


class Plane: # плоскость

    def __init__(self, n): # определяется нормалью проходит через начало координат
        self.n = n

    def circle(self, m=5, r=0.5): # m точек на окружности радиуса r
        n = self.n
        axis, q = Quaternion(), Quaternion()
        axis.get_arg_and_vec((2 * np.pi) / (m * 2), n)
        a = np.array([n[1], -n[0], 0])  # какй-то вектор лежащий в плоскости
        a = r * (a / np.linalg.norm(a))
        q.vec = a
        X, Y, Z = [a[0]], [a[1]], [a[2]]

        for _ in range(m):
            q = q.rot(axis)
            v = q.vec
            X.append(v[0])
            Y.append(v[1])
            Z.append(v[2])

        return [X, Y, Z]


class Movement():

    R = 0.5
    l = ((3 ** 0.5) / 2) * R
    g = 9.8
    m = 1

    A = ((m * (R ** 2)) / 4) + (m * (l ** 2))
    C = ((m * (R ** 2)) / 2)
    dt = 1 / 16

    psi0 = phi0 = psidot0 = tetadot0 = 0
    teta0 = np.pi / 6
    phidot0 = 4 * ((g / R) ** 2)

    alfa = (A / (C * phidot0))
    beta = 2 * A * m * g * l / ((C * phidot0) ** 2)

    def __init__(self, psi=0, phi=0, teta=0):
        self.teta = teta

    def increment(self):


        dteta = (((np.cos(teta0) - np.cos(self.teta)) *
                 (beta * (np.sin(self.teta) ** 2) - (np.cos(teta0) - np.cos(self.teta))) /
                 (np.sin(self.teta) ** 2)) ** 0.5) * dt

        self.teta += dteta

    def psidot(self):
        x = ((g / R) ** 0.5) * ((2 - (3 ** 0.5) * np.cos(self.teta) + 2 * (np.sin(self.teta) ** 2)) /
                                (np.sin(self.teta) ** 2))
        return  x

    def phidot(self):
        x = ((g / R) ** 0.5) * (((3 ** 0.5)   - 2 * np.cos(self.teta) ) /
                                (np.sin(self.teta) ** 2))
        return x







# p = Plane(np.array([1, 1, 1]))
# cir = p.circle()


fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)

# ax.scatter(cir[0], cir[1], cir[2])
# print(cir)
plt.show()


def one_vec_aninate():
    global k


    k = k.rot(q)

    line.set_data([0, ex.i], [0, ex.j])
    line.set_3d_properties([0, ex.k])




count = 0

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

greekSystem = EulerAngles()  # подвижный базис в углах Эйлера
k = greekSystem.axis() # ось симметрии тела (О дзета)
z = Quaternion(0, 0, 0, 1)

line, = ax.plot([0, ex.i], [0, ex.j], [0, ex.k], c='tab:red', label="x'")


ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.plot([0], [0], [0], 'o', c='tab:red')

args = np.array([np.pi / 6, np.pi / 4, np.pi / 6])

n = 50
interval, nframes = 0.1, n * len(args)

anim2 = animation.FuncAnimation(fig, one_vec_aninate, frames=nframes, interval=interval, repeat=False)
plt.legend()
plt.show()

