from copy import deepcopy
import colorama

colorama.init(autoreset=True)


def input_matrix(rows, cols):
    """Ввод СЛАУ"""
    A, B = [], []
    for row in range(rows):
        while True:
            try:
                l = input(str(row + 1) + ': ').strip().split()
                if len(l) == rows + 1:
                    for i in range(len(l)):
                        l[i] = float(l[i])
                    break
                else:
                    print(colorama.Fore.RED + 'введено некорректное значение!')
            except:
                print(colorama.Fore.RED + 'введено некорректное значение!')
                continue
        A.append(l[:cols])
        B.append([l[cols]])
    return A, B


def output_matrix(A, B):
    """Вывод СЛАУ"""
    for row in range(len(A)):
        for col in range(len(A[row])):
            print(A[row][col], end=' ')
        print('|', B[row][0])


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


if __name__ == '__main__':
    print(colorama.Fore.MAGENTA + '\t\tИНСТРУКЦИЯ К ПРИМЕНЕНИЮ ПРОГРАММЫ')
    print('''
Для начала программа попросит вас ввести ранг матрицы. Ранг 
матрицы - это количество строчек в квадратной матрице
(матрице, количество строк и столбцов в которой одинаково).
Затем необходимо ввести саму матрицу построчно. Это значит, 
что сначала вводится строчка коэффициентов при переменных 
через пробел, а затем свободный член уравнения. К примеру,
для матрицы: 

    1 2 3 4 | 5
А = 6 7 8 9 | 10
    1 2 3 4 | 5

ранг равен 3, а саму матрицу следует вводить таким образом:

1 2 3 4 5 "enter"
6 7 8 9 10 "enter"
1 2 3 4 5 "enter"
''')
    while True:
        while True:
            rang = input(colorama.Fore.CYAN + 'Введите ранг матрицы: ')
            if rang.isdigit() and int(rang) >= 1:
                rang = int(rang)
                break
            else:
                print(colorama.Fore.RED + 'Введено некорректное значение!')

        print()
        A, B = input_matrix(rang, rang)
        print(B)
        print()
        output_matrix(A, B)
        print()
        det = determinant(A)
        Kramer_Function(A, B, det)
        print()
        answer = input(colorama.Fore.CYAN + 'Желаете ли вы посчитать еще какую-либо СЛАУ? ').lower().strip()
        print()
        if answer not in ('да', 'yes'):
            break
