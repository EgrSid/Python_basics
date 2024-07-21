from random import randint, choice


class Ship:
    def __init__(self, length, tp, x=None, y=None):
        self._x = x
        self._y = y
        self._length = length
        self._tp = tp
        self._is_move = True
        self._cells = [1] * self._length

    def __str__(self):
        return f'{self._cells}'

    def __getitem__(self, item):
        return self._cells[item]

    def __setitem__(self, key, value):
        self._cells[key] = value

    def set_start_cords(self, x, y):
        self._x = x
        self._y = y

    def get_start_cords(self):
        return self._x, self._y

    def move(self, go):
        if self._is_move:
            if self._tp == 1:
                self._x += go
            elif self._tp == 2:
                self._y += go

    def is_collide(self, ships):
        if self._tp == 1:
            x_lst = [k for k in range(self._x, self._x + self._length)]
            x_lst.append(self._x - 1)
            x_lst.append(self._x + self._length)

            y_lst = [self._y + 1]
            y_lst += [self._y - 1]
            y_lst += [self._y]
        elif self._tp == 2:
            y_lst = [k for k in range(self._y, self._y + self._length)]
            y_lst.append(self._y - 1)
            y_lst.append(self._y + self._length)

            x_lst = [self._x + 1]
            x_lst += [self._x - 1]
            x_lst += [self._x]
        for i in ships:
            if i != self:
                if i._x >= 0 and i._y >= 0:
                    if i._tp == 1:
                        if (i._x in x_lst or (i._x + i._length - 1) in x_lst) and i._y in y_lst: return True
                    elif i._tp == 2:
                        if i._x in x_lst and ((i._y + i._length - 1) in y_lst or i._y in y_lst): return True
        return False

    def is_out_pole(self, size):
        if self._tp == 1:
            if (self._x and self._x + self._length - 1) in range(size) and self._y in range(size):
                return False
        elif self._tp == 2:
            if (self._y and self._y + self._length - 1) in range(size) and self._x in range(size):
                return False
        return True


class GamePole:
    def __init__(self, size=10):
        self._size = size
        self._ships = []

    def init(self):
        self._ships = [Ship(4, 1, 2, 1), Ship(3, 1, 4, 3), Ship(3, 1, 1, 7),
                       Ship(2, 2, 9, 0), Ship(2, 2, 9, 6), Ship(2, 2, 0, 3),
                       Ship(1, 1, 0, 0), Ship(1, 1, 9, 4), Ship(1, 2, 2, 4),
                       Ship(1, 2, 5, 9)]

    def get_ships(self):
        return self._ships

    def get_pole(self):
        self._pole = []
        for _ in range(self._size):
            templ = []
            for _ in range(self._size):
                templ.append(0)
            self._pole.append(templ)

        for i in self._ships:
            if i._x >= 0 and i._y >= 0:
                if not i.is_out_pole(self._size) and not i.is_collide(self._ships):
                    if i._tp == 2:
                        for j in range(i._length):
                            self._pole[j + i._y][i._x] = 1
                    elif i._tp == 1:
                        for j in range(i._length):
                            self._pole[i._y][j + i._x] = 1
                    '''for i in self._pole:
                        r = ''
                        for j in i:
                            r += f'{j}  '
                        print(r)
                    print()'''
                else:
                    raise SyntaxError('корабли стоят неверно!')
            else:
                raise SyntaxError('корабли стоят неверно!')

        return self._pole

    def show(self):
        for i in self.get_pole():
            r = ''
            for j in i:
                r += f'{j}  '
            print(r)

    def move_ships(self):
        for i in self._ships:
            if i._x and i._y and i._is_move:
                num = choice((-1, 1))
                if i._tp == 1:
                    i._x += num
                    if i.is_out_pole(self._size) or i.is_collide(self._ships):
                        i._x -= num * 2
                        if i.is_out_pole(self._size) or i.is_collide(self._ships): i._x += num
                if i._tp == 2:
                    i._y += num
                    if i.is_out_pole(self._size) or i.is_collide(self._ships):
                        i._y -= num * 2
                        if i.is_out_pole(self._size) or i.is_collide(self._ships): i._y += num


g = GamePole()
g.init()
for i in range(10):
    g.show()
    g.move_ships()
    print()
