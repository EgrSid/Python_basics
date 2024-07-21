# СТАХОСТИЧЕСКИЙ ГРАДИЕНТНЫЙ СПУСК ДЛЯ РЕШЕНИЯ ЗАДАЧ БИНАРНОЙ КЛАССИФИКАЦИИ

import numpy as np
import matplotlib.pyplot as plt


def loss(w, x, y):
    """Функция потерь"""
    M = np.dot(w, x) * y
    return 2 / (1 + np.exp(M))


def dLdw(w, x, y):
    """Производная функции потерь по весам"""
    M = np.dot(w, x) * y
    return -2 * np.exp(M) * x * y * (1 + np.exp(M)) ** -2


def plot(show=True):
    """Рисование основных графиков"""
    plt.grid(True)
    plt.xticks(np.arange(0, 55, 5))
    plt.yticks(np.arange(0, 90, 10))
    plt.scatter([x[0] for x in cl1], [x[1] for x in cl1], c='green')
    plt.scatter([x[0] for x in cl2], [x[1] for x in cl2], c='red')
    line_x = list(range(50))
    plt.plot(line_x, [-x * w[0] / w[1] - w[2] / w[1] for x in line_x])
    for i, x in enumerate(X):
        plt.text(x[0], x[1], y[i], fontsize=15)

    if show: plt.show()


X = [[10, 50], [20, 30], [25, 30], [20, 60], [15, 70], [40, 40], [30, 45], [20, 45], [40, 30], [7, 35]]
X = np.array([x + [1] for x in X])
y = np.array([-1, 1, 1, -1, -1, 1, 1, -1, 1, -1])
w = [0, 0, 0]

cl1 = X[np.where(y == 1)]
cl2 = X[np.where(y == -1)]

# гусеница = 1
# божья коровка = -1
x1 = [x[0] for x in X]  # ширина
x2 = [x[1] for x in X]  # длина

nt = 0.0005
lm = 0.01
N = 500

Q = np.mean([loss(x, y, y) for x, y in zip(X, y)])
Q_plt = [Q]

for i in range(N):
    k = np.random.randint(0, len(y) - 1)
    ek = loss(w, X[k], y[k])
    w = w - nt * dLdw(w, X[k], y[k])
    Q = lm * ek + (1 - lm) * Q
    Q_plt.append(Q)

print(f'w: {w}')
print(f'Q: {Q_plt[-1]}')

plot()


