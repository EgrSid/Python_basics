import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
import colorama
colorama.init(autoreset=True)

"""ЛИНЕЙНАЯ АППРОКСИМАЦИЯ"""

N = 100  # число экспериментов
sigma = 3  # стандартное отклонение
mu = 0  # мат ожидание распределения

k, b = 0.5, 2  # нулевые приближения (случайные значения)

x = np.array(range(N))

f = np.array([k*x+b for x in range(N)])  # теория
y = f + np.random.normal(mu, sigma, N)  # эксперимент (добавляет случайное число ПО ГАУССУ по мат ожиданию и стандартному отклонению)

mx = x.sum() / N  # мат ожидание по х
my = y.sum() / N  # мат ожидание по y

a2 = np.dot(x.T, x) / N  # второй смешанный начальный момент
a11 = np.dot(x.T, y) / N  # первый смешанный начальный момент

kk = (a11-mx*my) / (a2-mx**2)  # новое k, оптимальное
bb = my - kk*mx  # новое b, оптимальное

ff = np.array([kk*x+bb for x in range(N)])  # новая функция, описывающая набор точек

plt.title('Линейная аппроксимация')
plt.plot(f, color='red')
plt.plot(ff, color='green')  # оптимальная модель для данных, которые ведут себя линейно
plt.grid(True)
plt.scatter(x, y, color='blue', s=4)
plt.show()


"""КВАДРАТИЧНАЯ АППРОКСИМАЦИЯ"""

def minor(M, row2del, col2del):
    """Вычеркивание строки и столбца"""
    Mi = []  # результат работы функции
    for r in range(len(M)):
        if row2del != r:
            Mi.append([])
            for c in range(len(M[row2del])):
                if col2del != c:
                    Mi[-1].append(M[r][c])
    return Mi

def determinant(M):
    """Нахождение определителя матрицы"""
    if len(M) == 1:
        return M[0][0]  # выход из рекурсии
    res = 0
    k = 1
    for c in range(len(M[0])):
        res += k * M[0][c] * determinant(minor(M, 0, c))
        k *= -1
    return res

def Kramer_Function(A, B, det):
    """Нахождение корней СЛАУ методом Крамера"""
    res_list = []
    for j in range(len(A)):
        A_copy = deepcopy(A)
        for row in range(len(A)):
            for col in range(len(A)):
                A_copy[col][j] = B[col][0]
        res_list.append(determinant(A_copy))
    if det != 0:
        ans = []
        for i in range(len(res_list)):
            print(colorama.Fore.GREEN + 'x' + str(i + 1), '=', res_list[i] / det)
            ans.append(res_list[i] / det)
        return ans
    else:
        if res_list.count(0) == len(res_list):
            print(colorama.Fore.RED + 'СЛАУ имеет бесконечное множество решений')
        else:
            print(colorama.Fore.RED + 'СЛАУ не имеет решений')

# ИЗНАЧАЛЬНЫЙ СБОР ТОЧЕК ИСХОДЯ ИЗ ЗАДАННОЙ КВАДРАТИЧНОЙ ФУНКЦИИ
a, b, c = 1, 2, 3  # начальное приближение
N = 100
sigma = 100
mu = 100

x = np.array(range(-1*N // 2, N // 2))

f = np.array([a*x**2 + b*x + c for x in range(-1*N // 2, N // 2)])
y = f + np.random.normal(mu, sigma, N)

# НАХОЖДЕНИЕ ОПТИМАЛЬНЫХ ПАРАМЕТРОВ
A = [[np.sum(x**4) / N, np.sum(x**3) / N, np.sum(x**2) / N],
     [np.sum(x**3) / N, np.sum(x**2) / N, np.sum(x) / N],
     [np.sum(x**2) / N, np.sum(x) / N, 1]]

B = [[np.sum(x**2 * y) / N],
     [np.sum(x * y) / N],
     [np.sum(y) / N]]

det = determinant(A)
res = Kramer_Function(A, B, det)

# ПОСТРОЕНИЕ ОПТИМАЛЬНООГО ГРАФИКА АППРОКСИМАЦИИ
aa = res[0]
bb = res[1]
cc = res[2]

ff = np.array([aa*x**2 + bb*x + cc for x in range(-1*N // 2, N // 2)])

# ПОСТРОЕНИЕ ГРАФИКОВ
plt.title('Квадратичная аппроксимация')
plt.plot(x, f, color='red')  # неоптимальный график аппроксимации
plt.plot(x, ff, color='green')  # оптимальный график аппроксимации
plt.grid(True)
plt.scatter(x, y, color='blue', s=4)
plt.show()