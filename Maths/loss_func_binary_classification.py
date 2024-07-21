# ДЛЯ КВАДРАТИЧНОЙ ФУНКЦИИ ПОТЕРЬ

import numpy as np
import matplotlib.pyplot as plt

x_train = [[10, 50], [20, 30], [25, 30], [20, 60], [15, 70], [40, 40], [30, 45], [20, 45], [40, 30], [7, 35]]
x_train = np.array([x + [1] for x in x_train])  # добавили еще один признак для веса bias
y_train = np.array([-1, 1, 1, -1, -1, 1, 1, -1, 1, -1])

pt = np.sum([x * y_train[i] for i, x in enumerate(x_train)], axis=0)
xxt = np.sum([np.outer(x, x) for x in x_train], axis=0)
w = np.dot(pt, np.linalg.inv(xxt))

x0 = x_train[y_train == 1]
x1 = x_train[y_train == -1]
x_test = []

for i in range(0, 40, 5):
    x_test.append([i, i, 1])

test_data = [[30, 60, 1], [35, 10, 1], [6, 18, 1]]

plt.scatter([x[0] for x in x0], [x[1] for x in x0], c='red')
plt.scatter([x[0] for x in x1], [x[1] for x in x1], c='green')
plt.plot([x[0] for x in x_test], [(-x[2] * w[2] - x[0] * w[0]) / w[1] for x in x_test])
plt.scatter([x[0] for x in test_data], [x[1] for x in test_data], c='purple')
plt.grid(True)
plt.xticks(range(0, 50, 5))
plt.yticks(range(0, 70, 10))
plt.show()

print(f'веса модели: {w}')
print(f'предсказания модели: {[np.sign(np.dot(x, w)) for x in test_data]}')
