def input_list_ERROR():
        #НЕ ДОРАБОТАНО
    lst = input('Введите пример: ')
    i = -1
    res = []
    while i != len(lst) - 1:
        i += 1
        if not lst[i].isdigit():
            for j in lst[:i]:
                res.append(j)
            res.append(lst[i])
            lst = lst[i + 1:]
            i = -1
    if len(lst) != 0:
        res.append(lst)
    return res

def input_list():
    lst = input('ВВОДИТЬ КАЖДЫЙ ЭЛЕМЕНТ ЧЕРЕЗ ПРОБЕЛ\nВведите пример: ')
    res = lst.split(' ')
    return res


def function_first(Moscow):
    Lipetsk = []
    Piter = []
    priority = {'+': 1,
                '-': 1,
                '*': 2,
                '/': 2,
                '**': 3}
    for i in Moscow:
        try:
            i = float(i)
            Lipetsk.append(i)
        except:
            if len(Piter) == 0:
                Piter.append(i)
            else:
                if Piter[-1] == '(' and i != ')':
                    Piter.append(i)
                    continue
                if i not in '()':
                    if priority.get(i, i) > priority.get(Piter[-1], i):
                        Piter.append(i)
                    else:
                        try:
                            while priority.get(i, i) <= priority.get(Piter[-1], i):
                                Lipetsk.append(Piter.pop())
                            Piter.append(i)
                        except:
                            Piter.append(i)
                elif i == '(':
                    Piter.append(i)
                elif i == ')':
                    while Piter[-1] != '(':
                        Lipetsk.append(Piter.pop())
                    Piter = Piter[:-1]
    if len(Piter) != 0:
        while len(Piter) != 0:
            Lipetsk.append(Piter.pop())
    return Lipetsk


def function_second(lst):
    res = 0
    i = -1
    while len(lst) != 1:
        i += 1
        try:
            float(lst[i])
        except:
            lst[i - 1] = float(lst[i - 1])
            lst[i - 2] = float(lst[i - 2])
            if lst[i] == '+':
                res = lst[i - 2] + lst[i - 1]
            elif lst[i] == '-':
                res = lst[i - 2] - lst[i - 1]
            elif lst[i] == '*':
                res = lst[i - 2] * lst[i - 1]
            elif lst[i] == '/':
                res = lst[i - 2] / lst[i - 1]
            elif lst[i] == '**':
                res = lst[i - 2] ** lst[i - 1]
            lst.pop(i)
            lst.pop(i - 1)
            lst.pop(i - 2)
            lst.insert(i - 2, str(res))
            i = -1
    answer = ''.join(lst)
    return answer


print(function_second(function_first(input_list())))
