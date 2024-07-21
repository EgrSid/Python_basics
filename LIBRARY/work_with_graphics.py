        # СОЗДАНИЕ ГРАФИКОВ
import matplotlib.pyplot as plt
from numpy import linspace, sin, random, cos

x = linspace(0, 15, 300)
y = sin(x) #+ 0.1 * random.randn(len(x))
y2 = cos(x)


plt.figure(figsize=(8, 8)) # создание пространвтса для графиков
plt.grid(True) # добавили сетку

plt.suptitle('Тригонометрия', fontweight='bold', fontsize=20)


plt.plot(x, y, '-', label='sin(x)', color='red', linewidth=3) #linewidth=3 - жирность линии
# plt.show()   показать фигуру
plt.plot(x, y2, '-', label='cos(x)', color='blue', linewidth=3)


plt.xlim(0, 8) # установили лимиты отображения
plt.ylim(-1, 1) # установили лимиты отображения


plt.xlabel('x', fontsize=12, fontweight='bold') # подписи данных
plt.ylabel('sin(x)', fontsize=12, fontweight='bold') # подписи данных

plt.xticks() # задаем единичный отрезок

plt.legend(loc='upper right') # создание легенды

plt.axis('square') # задает одинаковый масштаб осей x и y

plt.show()



        #СТОБЧАТЫЕ ДИАГРАММЫ
res = random.randn(1000)*0.2+0.4

plt.hist(res, bins=100, histtype='step') # создание гистограммы(bins - количество видимыз столбиков)
# histtype='step'- все внутри графика не закрашено
plt.text(0.4, 10, 'парарам', fontsize=10, rotation=90)
plt.show()


# '.'  график из точек, по которым он строится
# '-'  обычный график
# '--'  график из пунктира
# '.--'  график из жирных точек, соединенных пунктиром
# '0--'  О - будет являться точкой, а -- будет соединять
# ':'  график чистыми точками


import csv
# ГРАФИК ОБЩЕГО ДОХОДА ПО ИСХОДНЫМ ЗНАЧЕНИЯМ\РАБОТА С БД
with open('company_sales_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    lst1 = []
    lst2 = []
    for row in csvreader:
        try:
            row[-1] = int(row[-1])
            row[0] = int(row[0])
            lst1.append(row[0])
            lst2.append(row[-1] / 1000)
        except:
            continue

plt.figure()
plt.grid(True)
plt.suptitle('Total profit', fontweight='bold', fontsize=20)
plt.xlabel('months', fontsize=15)
plt.ylabel('income[тыс. руб.]', fontsize=15)
plt.plot(lst1, lst2, '-', color='black', linewidth=3)
plt.xlim(min(lst1), max(lst1))
plt.ylim(0, 500)
plt.xticks(lst1)
plt.yticks(linspace(0, 500, 6))
plt.show()



# ГРАФИК ПОКУПАЕМОСТИ КАЖДОГО ПРОДУКТА/РАБОТА С БД
plt.figure()

graph_color = ('red', 'blue', 'black', 'green', 'purple', 'grey')

with open('company_sales_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    file = []
    lst = []
    lst_x = []
    counter = -1
    for row in csvreader:
        file.append(row)
        try:
            row[0] = int(row[0])
            lst_x.append(row[0])
        except:
            continue
    for i in range(len(file[0])):
        lst = []
        if i == 0 or i >= len(file[0]) - 2 or i >= len(file[0]) - 1:
            continue
        counter += 1
        for j in file:
            try:
                j[i] = int(j[i])
                lst.append(j[i] / 1000)
            except:
                continue
        plt.plot(lst_x, lst, '-', linewidth=3, color=graph_color[counter],
                     label=file[0][1:-2][counter])

plt.grid(True)
plt.suptitle('Продажи товаров', fontsize=20, fontweight='bold')
plt.xlabel('месяцы', fontsize=15)
plt.ylabel('сумма покупки[тыс.руб.]', fontsize=15)
plt.legend()
plt.xticks(lst_x)
plt.show()



# РАБОТА С БД
from math import prod

g = 9.8
file = []
graph = []
graph_x = []
graph_no_zero = []
graph_error = []
graph_stretching = []
graph_middle = []

with open('hooke.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        mini_file = []
        for i in row:
            try:
                i = float(i.strip())
                mini_file.append(i)
            except:
                continue
        file.append(mini_file)
file = file[1:-1]
for i in file:
    graph_x.append(int(i[0]))
    graph_stretching.append(float(i[-2]) - float(i[-1]))
    if i[-2] - i[-1] == 0:
        graph.append(0)
    else:
        graph.append(i[1] * g / (i[-2] - i[-1]))
        graph_no_zero.append(i[1] * g / (i[-2] - i[-1]))
    if i[-1] == 0:
        graph_error.append(0)
    else:
        graph_error.append((i[-2] - i[-1]) / i[-1])


for i in range(len(file)):
    graph_middle.append((sum(graph) / len(graph) - graph[i]) / sum(graph) / len(graph))

graph_stretching = graph_stretching[2:]
graph_middle = graph_middle[2:]

for i in range(len(graph_stretching) - 1):
    for j in range(len(graph_stretching) - 1 - i):
        if graph_stretching[j] > graph_stretching[j+1]:
            graph_stretching[j], graph_stretching[j+1] = graph_stretching[j+1], graph_stretching[j]
            graph_middle[j], graph_middle[j + 1] = graph_middle[j + 1], graph_middle[j]
# ГРАФИК ОТНОСИТЕЛЬНОЙ ПОГРЕШНОСТИ ЖЕСТКОСТИ ОТ РАСТЯЖЕНИЯ ПРУЖИНЫ
plt.figure()
plt.grid(True)
plt.suptitle('График относительной погрешности\nжесткости от растяжения', fontweight='bold', fontsize=25)
plt.plot(graph_stretching, graph_middle, linewidth=3, label='относительная погрешность\nизмерений растяжения\nпружины')
plt.xlabel('растяжение пружины', fontsize=15)
plt.ylabel('относительная погрешность жесткости\nв конкретном испытании', fontsize=15)
plt.legend()


# ГРАФИК ЖЕСТКОСТИ ПРУЖИНЫ
plt.figure()
plt.grid(True)
plt.suptitle('Жесткость пружины', fontweight='bold', fontsize=25)
plt.plot(graph_x, graph, linewidth=5, color='black', label='график жесткости пружины')
plt.xticks(graph_x)
plt.xlabel('Номер эксперимента', fontsize=15)
plt.ylabel('Жесткость пружины в\nданном эксперименте', fontsize=15)


# ГРАФИК СРЕДНЕГО АРИФМЕТИЧЕСКОГО И ГЕОМЕТРИЧЕСКОГО
plt.plot([1, 10], [sum(graph) / len(graph), sum(graph) / len(graph)], color='red', linewidth=2, label='среднее арифметическое')
plt.plot([1, 10], [prod(graph_no_zero) ** (1/len(graph_no_zero)), prod(graph_no_zero) ** (1/len(graph_no_zero))], color='blue', linewidth=2, label='среднее геометрическое')
plt.legend()

plt.show()