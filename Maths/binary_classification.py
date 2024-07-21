import matplotlib.pyplot as plt
import numpy as np

X = np.array([[10, 50], [20, 30], [25, 30], [20, 60], [15, 70], [40, 40], [30, 45], [20, 45], [40, 30], [7, 35]])
y = np.array([-1, 1, 1, -1, -1, 1, 1, -1, 1, -1])

cl1 = X[np.where(y == 1)]
cl2 = X[np.where(y == -1)]

# гусеница = 1
# божья коровка = -1
x1 = [x[0] for x in X]  # ширина
x2 = [x[1] for x in X]  # длина

N = 3_000  # количество итераций обучения
mu = 0.001  # шаг обучения
w = [0, -1]


def plot(show=True):
    """Рисование основных графиков"""
    plt.grid(True)
    plt.xticks(np.arange(0, 55, 5))
    plt.yticks(np.arange(0, 90, 10))
    plt.scatter([x[0] for x in cl1], [x[1] for x in cl1], c='green')
    plt.scatter([x[0] for x in cl2], [x[1] for x in cl2], c='red')
    plt.plot(x1, [w[0] * x for x in x1])
    for i, x in enumerate(X):
        plt.text(x[0], x[1], y[i], fontsize=15)

    if show: plt.show()


def a(x):
    """Линейная модель"""
    return np.dot(x, w)


def L(x):
    """Функция потерь - sigmoid"""
    return 1 / (1 + np.exp(-x))


Q_prev = -1
for n in range(N):
    Q = 0
    for i, x in enumerate(X):
        w[0] += mu * y[i] if a(x) * y[i] < 0 else -mu * y[i]  # корректировка весов
        Q += L(-a(x) * y[i])  # '-' потому что в формуле сигмоиды '-' стоит внутри экспоненты
    print(f'{n}: {Q / len(X)}')

    # plot() демонстрация улучшения весов модели
    # если найдены оптимальные параметры и средний эмпирический риск не меняется
    if Q == Q_prev:
        print('early stopping')
        break
    Q_prev = Q

# вывод информации о модели
print(f'Веса модели: {np.round(w, 2)}')
print(f'Средний эмпирический риск: {Q_prev}')

# тест модели
x_test = [[30, 30], [40, 50], [8, 25]]
y_pred = [int(np.sign(a(x))) for x in x_test]

# рисование точек и прямой модели
plot(False)
plt.scatter([x[0] for x in x_test], [x[1] for x in x_test], c='purple')
for i, x in enumerate(x_test):
    plt.text(x[0], x[1], y_pred[i], fontsize=15)
plt.show()
