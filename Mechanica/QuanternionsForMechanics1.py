import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


"""
Класс квантернионов для задания вращения тела в пространстве 
Павлов Егор 07.10.2022
"""


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


def aninate():
    global args, darg
    global ex, ey, ez
    global count, n

    vecs = np.array([ex.vec, ey.vec, ez.vec])

    if count // n == len(args):
        darg = 0
        vec = vecs[-1]
    else:
        darg = args[count // n] / n
        vec = vecs[count // n]

    q = Quaternion()
    q.get_arg_and_vec(darg, vec)

    ex = ex.rot(q)
    ey = ey.rot(q)
    ez = ez.rot(q)

    line1.set_data([0, ex.i], [0, ex.j])
    line1.set_3d_properties([0, ex.k])
    line2.set_data([0, ey.i], [0, ey.j])
    line2.set_3d_properties([0, ey.k])
    line3.set_data([0, ez.i], [0, ez.j])
    line3.set_3d_properties([0, ez.k])

    count += 1


def one_vec_aninate():
    global ex, ey, ez
    arg = 1.2094292028881888
    vec = [0.6546536707079771, 0.3779644730092272, 0.6546536707079771]
    darg = arg / n
    q = Quaternion()
    q.get_arg_and_vec(darg, vec)

    ex = ex.rot(q)
    ey = ey.rot(q)
    ez = ez.rot(q)

    line1.set_data([0, ex.i], [0, ex.j])
    line1.set_3d_properties([0, ex.k])
    line2.set_data([0, ey.i], [0, ey.j])
    line2.set_3d_properties([0, ey.k])
    line3.set_data([0, ez.i], [0, ez.j])
    line3.set_3d_properties([0, ez.k])


ex = Quaternion(0, 1, 0, 0)  # стандартный базис
ey = Quaternion(0, 0, 1, 0)  # вместо него можно взять любой набор векторов
ez = Quaternion(0, 0, 0, 1)  # так как набором векторов можно задать тело, то можно вращать его

count = 0

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

line1, = ax.plot([0, ex.i], [0, ex.j], [0, ex.k], c='tab:red', label="x'")
line2, = ax.plot([0, ey.i], [0, ey.j], [0, ey.k], c='tab:green', label="y'")
line3, = ax.plot([0, ez.i], [0, ez.j], [0, ez.k], c='tab:orange', label="z'")

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

anim1 = animation.FuncAnimation(fig, aninate, frames=nframes, interval=interval, repeat=False)
plt.legend()
plt.show()

ex = Quaternion(0, 1, 0, 0)  # стандартный базис
ey = Quaternion(0, 0, 1, 0)  # вместо него можно взять любой набор векторов
ez = Quaternion(0, 0, 0, 1)  # так как набором векторов можно задать тело, то можно вращать его

count = 0

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

line1, = ax.plot([0, ex.i], [0, ex.j], [0, ex.k], c='tab:red', label="x'")
line2, = ax.plot([0, ey.i], [0, ey.j], [0, ey.k], c='tab:green', label="y'")
line3, = ax.plot([0, ez.i], [0, ez.j], [0, ez.k], c='tab:orange', label="z'")

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.plot([0], [0], [0], 'o', c='tab:red')
ax.quiver([0], [0], [0], [0.6546536707079771], [0.3779644730092272], [0.6546536707079771])


n = 100
interval, nframes = 0.1, n

anim2 = animation.FuncAnimation(fig, one_vec_aninate, frames=nframes, interval=interval, repeat=False)

plt.legend()
plt.show()
