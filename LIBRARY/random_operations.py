import random
import numpy
import string

print('Вывод случайного числа от 0 до 1: ')
print(random.random())


a = 9
b = 39
print('Вывод числа из диапазона от a до b: ')
print(random.randrange(a, b, 2)) # 2 - шаг


a = 9
b = 39
print('Вывод числа из диапазона от a до b: ')
print(random.randint(a, b))


lst = ['Паша', 'Гриша', 8, True, -0.7]
print('Вывод случайного элемента из списка: ')
print(random.choice(lst))


print('Вывод случайного дробного числа из диапазона от a до b: ')
print(random.uniform(a, b))



print('Вывод случайного дробного числа из диапазона от a до b: ')
print(random.triangular(a, b, 2.3))# 2.3 - шаг


num_lst = [3, 7, 12, -9, -4, 45, 1, True, 'dvkbaev']
print('Вывод случайной выборки из num_list: ')
print(random.sample(num_lst, k = 3)) # k - количество элементов в выборке


step_int = 2
print(numpy.random.uniform(a, b, size=(3, 2)))


random.seed(7) # семя рандома(точка отсчета для всего вывода random)

        # ФУНКЦИЯ ГЕНЕРАЦИИ СЛУЧАЙНОГО ПАРОЛЯ
def full_answer(length = 10, numbers=True, letters=True, symbols=True):
    answer1 = ''
    while True:
        if numbers:
            answer1 += string.digits
        if letters:
            answer1 += string.ascii_letters
        if symbols:
            answer1 += string.punctuation
        if answer1 == '':
            print('Вводные данные некорректны!')
            exit()
        else:
            break
    answer = ''.join(random.choice(answer1) for i in range(length))
    print(answer)
full_answer(15, True, True, False)