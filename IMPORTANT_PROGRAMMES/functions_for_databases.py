import csv
import colorama
colorama.init(autoreset=True)

def total_profit_counter(file):
    # ПОДСЧЕТ ОБЩЕГО ДОХОДА
    counter_money = 0
    with open(file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            try:
                counter_money += float(row[-1])
            except:
                continue
    print(counter_money)

def all_countries(file):
    # ВСЕ СТРАНЫ В БД
    lst_countries = []
    with open(file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            try:
                a = row.index('Country')
            except:
                if row[a] not in lst_countries:
                    lst_countries.append(row[a])
    print(lst_countries)

def all_regions(file):
        #ВСЕ РЕГИОНЫ В БД
    lst_regions = []
    with open(file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            try:
                a = row.index('Region')
            except:
                if row[a] not in lst_regions:
                    lst_regions.append(row[a])
    print(lst_regions)

def Order_Date_to_Ship_Date(file):
    # ПОКАЗЫВАЕТ ДАТУ ПОГРУЗКИ И РАЗГРУЗКИ ТОВАРОВ
    ended_lst = []
    with open(file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            mini_str = ''
            try:
                a = row.index('Order Date')
                b = row.index('Ship Date')
            except:
                mini_str =str(row[a]) + '-->' + str(row[b])
            ended_lst.append(mini_str)
    print(ended_lst)

def Units_Sold_Counter(file):
     # КОЛИЧЕСТВО ПРОДАННЫХ ЕДИНИЦ ПРОДУКЦИИ ВСЕГО
    counter = 0
    with open(file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            try:
                a = row.index('Units Sold')
            except:
                counter += float(row[a])
    print(counter)

def Order_ID_Finder(file):
     # ВЫВОДИТ IDшники ИЗ ПРОДАННЫХ ТОВАРОВ
    lst = []
    with open(file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            try:
                a = row.index('Order ID')
            except:
                lst.append(row[a])
    print(lst)

def total_profit_checker(file):
    with open(file, 'r') as csvfile:
            # ПРОВЕРЯТ, ВЕРНО ЛИ ПОДСЧИТАНА ИТОГОВАЯ ВЫРУЧКА
        k = False
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            try:
                a = row.index('Unit Price')
                b = row.index('Unit Cost')
                c = row.index('Units Sold')
                d = row.index('Total Profit')
            except:
                if round((float(row[a]) - float(row[b])) * float(row[c]), 2) != float(row[d]):
                    k = True
                    print(colorama.Fore.RED + 'ОШИБКА!!!\n', row)
                else:
                    continue
    if not k:
            print('Все данные посчитаны верно!')

total_profit_checker('Sales.csv')


