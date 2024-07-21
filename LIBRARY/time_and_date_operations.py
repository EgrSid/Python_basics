from sys import getsizeof
s = 'Я помню чудное мгновение!'
print('string:', getsizeof(s)) # выводит сколько байт занимает значение




from datetime import datetime

print(datetime.now()) # выводит точное время и точную дату
print(datetime.now().time()) # выводит только точное время
print(datetime.now().date()) # выводит только точную дату

import time


print(time.altzone/3600) # показывает насколько мое время смещено в часовых поясах к западу от 0 мередиана(в секундах)
print(time.asctime()) # вся точная информация на данный момент(время, день недели и тд)
#print(time.clock()) # время для MAC и LINUX
print(time.ctime()) # уменьшенное от asctime
print(time.daylight) # показывает зимнее и летнее время(0 - значит ничего не перевели)
print(time.gmtime(12455)) # отправляем любое число в секундах, а программа разбивает на годы, месяцы, часы и тд

time.sleep(1) # искусственная задержка исполнения программы на заданное кол-во секунд
print(time.time()) # выводит кол-во секунд с начала эпохи
print(time.timezone / 3600) # часовой пояс по GMT