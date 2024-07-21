import csv
import matplotlib.pyplot as plt
from numpy import linspace, sin, random, cos

    #БАЗА ДАННЫХ

with open('addresses.csv', 'r') as csv_file:
    csvreader = csv.reader(csv_file) # считал файл как ссылку на чтение
    for row in csvreader: # считал файл
        print(row)

data = [['Name', 'Age', 'City'],
        ['Alice', '30', 'New York'],
        ['Bob', '25', 'Lipetsk']]

with open('output.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile) # создает ссылку на запись
    for row in data:
        csvwriter.writerow(row) # запись одной строчки или одного списка

data = [{'ID': '000', 'datatime': '12.32.43', 'price': '120'},
        {'ID': '001', 'datatime': '32.22.83', 'price': '5450'},
        {'ID': '010', 'datatime': '92.39.13', 'price': '9'}]

with open('csv_write_dicts.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=list(data[0].keys())) # считываем заголовки
    writer.writeheader() # записывает заголовки
    for d in data:
        writer.writerow(d)


with open('addresses.csv', 'r') as csv_file:
    reader = csv.DictReader(csvfile) # считывает словарь
    for row in reader:
        print(row)



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