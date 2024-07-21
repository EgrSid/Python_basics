from colorama import Fore, init
import random
init(autoreset=True)

class TicTacToe:
    def __init__(self):
        self.FREE_CELL = ' '  # свободная клетка
        self.HUMAN_X = 'x'  # крестик (игрок - человек)
        self.COMPUTER_O = 'o'  # нолик (игрок - компьютер)
        self.res = []

    def init(self):
        #self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))
        self.pole = []
        for i in range(3):
            templ_list = []
            temple = []
            for j in range(3):
                templ_list.append(Cell())
                temple.append(Cell().value)
            self.pole.append(templ_list)
            self.res.append(temple)

        print(Fore.MAGENTA + "ФОРМАТ ВВОДА НОМЕРА КЛЕТКИ ПОЛЬЗОВАТЕЛЕМ\
        \n - вводится 2 числа через пробел\
        \n - 1 число: номер строки от 1 до 3\
        \n - 2 число: номер столбца от 1 до 3")

    def __validate(self, item):
        return item[0] in (1, 2, 3) and item[1] in (1, 2, 3)

    def __str__(self):
        return f'{self.res}'

    def __getitem__(self, item):
        if self.__validate(item):
            return self.res[item[0]-1][item[1]-1]
        raise IndexError('некорректно указанные индексы')

    def __setitem__(self, key, value):
        if self.__validate(key) and value in (0, 1, 2):
            self.res[key[0]-1][key[1]-1] = value

    def __bool__(self):
        j = 0
        for i in self.res:
            if i.count(' ') == 0:
                j += 1
        if j == 3: return False
        return True

    def show(self):
        print()
        for i, n in enumerate(self.res):
            if i == 2:
                print(f'  {n[0]} | {n[1]} | {n[2]}')
            else:
                print(f'  {n[0]} | {n[1]} | {n[2]}')
                print(f' ———————————')
        print()

    def human_go(self):
        while True:
            a = input('Ваш ход: ').split()
            try:
                a = list(map(int, a))
            except:
                print(Fore.CYAN + 'неверный индекс')
                continue
            if a[0] not in (1, 2, 3) or a[1] not in (1, 2, 3) or self.res[a[0]-1][a[1]-1] != ' ':
                print(Fore.CYAN + 'неверный индекс')
            else:
                break
        self.res[a[0]-1][a[1]-1] = 'X'  # -1 чтобы отсчет начинался по человечески, а не с нуля
        if self.is_human_win:
            print(Fore.MAGENTA + 'ПОБЕДА ЗА ТОБОЙ!')
            self.show()
            exit()
        elif self.is_draw and not self:
            print(Fore.MAGENTA + 'игра завершена! ничья!')
            self.show()
            exit()

    def computer_go(self):
        for i in range(9):
            a = random.randint(0, 2)
            b = random.randint(0, 2)
            if self.res[a][b] == ' ':
                self.res[a][b] = 'O'
                if self.is_computer_win:
                    print(Fore.MAGENTA + 'машина победила, но не расстраивайся!')
                    self.show()
                    exit()
                break
        else:
            # если компьютер не нашел свободного места для хода и никто не выигрывал соответственно
            print(Fore.MAGENTA + 'игра завершена! ничья!')
            self.show()
            exit()

    @property
    def is_human_win(self):
        # рассматриваю игровое поле относительно гравной диагонали

        '''
        all - все были True (замена and) В КАРТЕЖЕ
        any - хотя бы одна True (замена or) В КАРТЕЖЕ
        if all(self.res[r][c] != 1 for r in range(3) for c in range(3))
        if any(self.res[r][c] != 1 for r in range(3) for c in range(3))
        '''

        if self.res[0][0] != 'X' and self.res[1][1] != 'X' and self.res[2][2] != 'X':
            return False
        if self.res[0][0] == 'X':
            if self.res[0].count('X') == 3 or (self.res[1][0] == 'X' and self.res[2][0] == 'X')\
                    or (self.res[1][1] == 'X' and self.res[2][2] == 'X'):
                return True
        elif self.res[1][1] == 'X':
            if (self.res[0][1] == 'X' and self.res[2][1] == 'X') or (self.res[1][0] == 'X' and self.res[1][2] == 'X')\
                    or (self.res[0][2] == 'X' and self.res[2][0] == 'X'):
                return True
        elif self.res[2][2] == 'X':
            if (self.res[0][2] == 'X' and self.res[1][2] == 'X') or (self.res[2][0] == 'X' and self.res[2][1] == 'X'):
                return True
        return False

    @property
    def is_computer_win(self):
        if self.res[0][0] != 'O' and self.res[1][1] != 'O' and self.res[2][2] != 'O':
            return False
        if self.res[0][0] == 'O':
            if self.res[0].count(1) == 3 or (self.res[1][0] == 'O' and self.res[2][0] == 'O')\
                    or (self.res[1][1] == 'O' and self.res[2][2] == 'O'):
                return True
        elif self.res[1][1] == 'O':
            if (self.res[0][1] == 'O' and self.res[2][1] == 'O') or (self.res[1][0] == 'O' and self.res[1][2] == 'O')\
                    or (self.res[0][2] == 'O' and self.res[2][0] == 'O'):
                return True
        elif self.res[2][2] == 'O':
            if (self.res[0][2] == 'O' and self.res[1][2] == 'O') or (self.res[2][0] == 'O' and self.res[2][1] == 'O'):
                return True
        return False

    @property
    def is_draw(self):
        if not any((self.is_computer_win, self.is_human_win)): return True
        return False




class Cell:
    def __init__(self):
        self.value = ' '

    def __str__(self):
        return f'{self.value}'

    def __bool__(self, cell):
        return not cell.value


if __name__ == '__main__':
    game = TicTacToe()
    game.init()
    step_game = 0
    while game:
        game.show()

        if step_game % 2 == 0:
            game.human_go()
        else:
            game.computer_go()

        step_game += 1

    game.show()

