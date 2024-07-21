import numpy as np
import matplotlib.pyplot as plt

sigma = 0.05


def f(x):
    return 1 / (1 + 10 * x ** 2)


def make_polynom(x, params):
    res_points = []
    for xx in x:
        point = 0
        for i, param in enumerate(params):
            point += param * xx ** i
        res_points.append(point)
    return np.array(res_points)


x = np.arange(0, 10, 0.1)
x_test = np.arange(0, 11, 0.1)
y = np.array([f(xx) for xx in x])
y_test = np.array([f(xx) for xx in x_test])

fig, axes = plt.subplots(8, 8)

fig.set_size_inches(15, 4)
fig.set_figheight(30)
fig.set_figwidth(8)
# fig.tight_layout()

n = 0
for ax in axes:
    for ax1 in ax:
        params = np.polyfit(x, y, n)[::-1]
        points = make_polynom(x_test, params)
        ax1.plot(x_test, y_test, c='red')
        ax1.plot(x_test, points, c='green')
        ax1.set_ylim([-1, 1])
        ax1.set_title(f'n = {n}')
        ax1.axis('off')
        n += 1
plt.show()
