print(round(12.5273648236, 4))# округляет заданное число до определенного знака после запятой; 4 - до какого знака надо округлять


max(1, 4, 73623786, 1874124616476766)# находит максимальное число из списка
min(3, 10, 22, -3, 0)# находит минимальное число из списка

#переводит число из десятичной системы счисления  двоичную
a = 245
b = bin(a)[2:]
print(b)


#переводит число из десятичной системы счисления в восьмеричную
a = 245
b = oct(a)[2:]
print(b)


#переводит число из десятичной системы счисления в шестнадцатиричную
a = 245
b = hex(a)[2:]
print(b)


#переводит из любой сс в десятичную; 16 - сс, из которой нужно перевести; 567 - число, которое нужно перевести
a = int('567', 16)
print(a)


# ФУНКЦИЯ ВЫВОДИТ МОЖНО ЛИ ПЕРЕВЕСТИ ЧИСЛО В INT\FLOAT
import colorama
def types(string, typing):
    typing = typing.lower().strip()
    if typing in ('int', 'integer'):
        try:
            int(string)
            return True
        except:
            return False
    elif typing == 'float':
        try:
            float(string)
            return True
        except:
            return False
    else:
        print(colorama.Fore.RED + 'Введен некорректный тип данных')
        return None
print(types('6jvhvj7', '    InTegeR        '))



# СЧИТАЕТ СУММУ ЗАДАННЫХ ЧИСЕЛ
def addNumbers(*num):
    summ = 0
    for i in num:
        summ = summ + i
    print(summ)
addNumbers(1, 35, 84)