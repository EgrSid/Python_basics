import numpy as np
import matplotlib.pyplot as plt
import time

'''# ДЕМОНСТРАЦИЯ ГРАДИЕНТНОГО СПУСКА

def f(x):
    return x ** 2 - 5 * x + 5


def df(x):
    return 2 * x - 5


N = 20  # количество итераций
xx = 0  # начальное значение
lmd = 0.1  # шаг сходимости

x_plt = np.arange(0, 5, 0.1)
f_plt = [f(x) for x in x_plt]

plt.ion()  # интерактивный режим
fig, ax = plt.subplots()
ax.grid(True)
ax.plot(x_plt, f_plt, c='black')
point = ax.scatter(xx, f(xx), c='red')

for i in range(N):
    xx = xx - lmd * df(xx)
    point.set_offsets([xx, f(xx)])

    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.1)

plt.ioff()
print(xx)
ax.scatter(xx, f(xx), c='green')
plt.show()'''

'''# ДЕМОНСТРАЦИЯ ЗАСТРЕВАНИЯ ГРАДИЕНТА В ЛОКАЛЬНОМ МИНИМУМЕ

def f(x):
    return np.sin(x) + x / 2


def df(x):
    """градиент"""
    return np.cos(x) + 0.5


N = 20  # количество итераций
xx = 2.5  # начальное значение
lmd = 0.9  # шаг сходимости

x_plt = np.arange(-5, 5, 0.1)
f_plt = [f(x) for x in x_plt]

plt.ion()  # интерактивный режим
fig, ax = plt.subplots()
ax.grid(True)
ax.plot(x_plt, f_plt, c='black')
point = ax.scatter(xx, f(xx), c='red')

n_min = 100
for i in range(N):
    lmd = 1 / min(i+1, n_min)
    xx = xx - lmd * np.sign(df(xx))  # np.sign(df(xx)) возвращает знак градиента
    point.set_offsets([xx, f(xx)])

    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.1)

plt.ioff()
print(xx)
ax.scatter(xx, f(xx), c='green')
plt.show()'''


def E(y, k, b):
    ff = np.array([k * x + b for x in range(N)])
    return np.dot((y - ff).T, (y - ff))


def dEdK(y, k, b):
    ff = np.array([k * x + b for x in range(N)])
    return -2 * np.dot((y - ff).T, range(N))


def dEdb(y, k, b):
    ff = np.array([k * x + b for x in range(N)])
    return -2 * (y - ff).sum()


N = 100
n_iter = 50
sigma = 3
kt, bt = 0.5, 2  # теоретические k, b

kk, bb = 0, 0
lmd_k, lmd_b = 0.000001, 0.0005

f = np.array([kt * x + bt for x in range(N)])
y = np.array(f + np.random.normal(0, sigma, N))

k_plt = np.arange(-1, 2, 0.1)  # просто для демонстрации
b_plt = np.arange(0, 3, 0.1)  # просто для демонстрации
E_plt = np.array([[E(y, k, b) for k in k_plt] for b in b_plt])

plt.ion()
fig = plt.figure()
ax = plt.axes(projection="3d")

k, b = np.meshgrid(k_plt, b_plt)  # погуглить, надо, чтобы построить трехмерную поверхность
ax.plot_surface(k, b, E_plt, color='yellow', alpha=0.5)

ax.set_xlabel('k')
ax.set_ylabel('b')
ax.set_zlabel('E')

point = ax.scatter(kk, bb, E(y, kk, bb), color='red')  # начальная точка

for n in range(n_iter):
    kk = kk - lmd_k * dEdK(y, kk, bb)
    bb = bb - lmd_b * dEdb(y, kk, bb)

    # point.set_offsets([kk, bb, E(y, kk, bb)])
    ax.scatter(kk, bb, E(y, kk, bb))

    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.1)

plt.ioff()
plt.show()

# двумерный график подобранных оптимальных параметров
plt.scatter(range(N), y, s=5)
plt.plot(range(N), [kk * x + bb for x in range(N)], c='green')  # верная прямая
plt.plot(range(N), f, c='red')  # предполагаемая прямая, относительно которой строили точки
plt.xlabel('k')
plt.ylabel('b')
plt.show()
