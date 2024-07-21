from copy import deepcopy


class Decimal:
    def __init__(self, num):
        num = str(num)
        try:
            float(num)
        except:
            raise TypeError('неверный тип данных')
        self.num = num

    def __str__(self):
        return f'{self.num}'

    @classmethod
    def __verification(cls, other):
        if not isinstance(other, (int, float, str, Decimal)): raise ArithmeticError('неверное значение')
        return str(other.num).replace(',', '.') if isinstance(other, Decimal) else str(other).replace(',', '.')

    def addition(self, number):
        mn = 1  # множитель разрядов числа
        res = 0
        lst = [self.num, number]  # список складываемых чисел
        before_point = []  # список цифр числа до точки
        after_point = []  # список цифр числа после точки

        for i in range(len(lst)):
            point_counter = lst[i].find('.')
            if point_counter != -1:
                before_point.append(lst[i][:point_counter])
                after_point.append(lst[i][point_counter + 1:])
            else:
                before_point.append(lst[i])
                after_point.append('0')

        before_point.sort(key=len)
        after_point.sort(key=len)
        before_point[0] = before_point[0].rjust(len(before_point[1]), '0')
        after_point[0] = after_point[0].ljust(len(after_point[1]), '0')

        lst[0] = before_point[0] + '.' + after_point[0]
        lst[1] = before_point[1] + '.' + after_point[1]

        point_loc = lst[1].find('.')
        lst[0] = lst[0].replace('.', '')
        lst[1] = lst[1].replace('.', '')
        lst[0] = lst[0].rjust(len(lst[1]), '0')

        for i in range(len(lst[0]))[::-1]:
            res += (int(lst[0][i]) + int(lst[1][i])) * mn
            mn *= 10

        res = list(str(res))
        res.insert(point_loc, '.')
        res = ''.join(res)

        return res

    def subtraction(self, number):
        mn = 1  # множитель разрядов числа
        res = 0
        t = False
        a = [self.num, number]  # список складываемых чисел
        b = []
        c = []

        for i in range(len(a)):
            point_counter = a[i].find('.')
            if point_counter != -1:
                b.append(a[i][:point_counter])
                c.append(a[i][point_counter + 1:])
            else:
                b.append(a[i])
                c.append('0')
        d = deepcopy(b)
        e = deepcopy(c)

        d.sort(key=len)
        e.sort(key=len)
        b[b.index(d[0])] = d[0].rjust(len(d[1]), '0')
        c[c.index(e[0])] = e[0].ljust(len(e[1]), '0')

        a[0] = b[0] + '.' + c[0]
        a[1] = b[1] + '.' + c[1]

        point_loc = a[1].find('.')
        a[0] = a[0].replace('.', '')
        a[1] = a[1].replace('.', '')

        for i in range(len(a[0]))[::-1]:
            res += (int(a[0][i]) - int(a[1][i])) * mn
            mn *= 10

        print(a)

        if res == 0:
            return 0
        elif res < 0:
            t = True

        res = str(res).rjust(len(a[0]), '0')

        res = list(str(res))
        if t:
            res.remove('-')
        if 0 < float(''.join(res)) < 100 or 10000000 > float(''.join(res)) > 1000000:
            res.insert(point_loc-1, '.')
        else:
            res.insert(point_loc, '.')
        res = ''.join(res)

        for j in range(len(res)):
            if res.startswith('0'):
                res = res[1:]
            if res.endswith('0'):
                res = res[:-1]

        if res.endswith('.'):
            res = res[:-1]
        elif res.startswith('.'):
            res = '0' + res

        if t:
            res = '-' + res

        return res

    def multiplication(self,  number):
        lst = [self.num, number]
        before_point = []
        after_point = []
        decimal_places = 0  # знаки после запятой
        res = 0
        sign = 0  # арифметический знак результата

        for i in range(len(lst)):
            if lst[i].find('-') != -1:
                lst[i] = lst[i][1:]
                sign += 1
            point_counter = lst[i].find('.')
            if point_counter != -1:
                decimal_places += len(lst[i]) - point_counter - 1
                before_point.append(lst[i][:point_counter])
                after_point.append(lst[i][point_counter + 1:])
            else:
                before_point.append(lst[i])
                after_point.append('')

        lst[0] = before_point[0] + after_point[0]
        lst[1] = before_point[1] + after_point[1]

        for i in range(len(lst[1])):
            res += int(lst[0]) * int(lst[1][i]) * (10 ** (len(lst[1]) - i - 1))

        res = list(str(res))
        res.insert(len(res)-decimal_places, '.')

        if res[0] == '.':
            res.insert(0, '0')
        elif ''.join(res).endswith('.'):
            res = res[:-1]

        if sign == 1:
            res.insert(0, '-')

        res = ''.join(res)

        return res

    def division(self, number):
        lst = [self.num, number]
        """ЧЕРЕЗ .FIND"""



    def __add__(self, other):
        return self.addition(str(self.__verification(other)))

    def __radd__(self, other):
        return self.addition(str(self.__verification(other)))

    def __sub__(self, other):
        return self.subtraction(str(self.__verification(other)))

    def __rsub__(self, other):
        return self.subtraction(str(self.__verification(other)))

    def __mul__(self, other):
        return self.multiplication(str(self.__verification(other)))

    def __rmul__(self, other):
        return self.multiplication(str(self.__verification(other)))

    def __truediv__(self, other):
        return self.division(str(self.__verification(other)))

    def __rtruediv__(self, other):
        return self.division(str(self.__verification(other)))

if __name__ == '__main__':
    c = Decimal('13')
    print('c =', c)
    c /= 12.44
    print('c =', c)
