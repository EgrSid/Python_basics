import numpy as np
import matplotlib.pyplot as plt
import time


def f(x):
    return np.sin(x) + x / 2


def df(x):
    """градиент"""
    return np.cos(x) + 0.5


N = 50  # количество итераций
xx = 13  # начальное значение
lmd = 0.7  # шаг сходимости
g = 0.9  # шаг момента

x_plt = np.arange(-15, 15, 0.1)
f_plt = [f(x) for x in x_plt]

plt.ion()  # интерактивный режим
fig, ax = plt.subplots()
ax.grid(True)
ax.plot(x_plt, f_plt, c='black')
point = ax.scatter(xx, f(xx), c='red')

nu = lmd * df(xx)  # начальное вычисление градиента для реализации momentum
for i in range(N):
    xx = xx - nu
    nu = g * nu + lmd * df(xx) * (1 - g)
    point.set_offsets([xx, f(xx)])

    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.1)

plt.ioff()
print(xx)
ax.scatter(xx, f(xx), c='green')
plt.show()
