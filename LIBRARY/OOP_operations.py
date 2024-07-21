from accessify import protected, private
from math import sin

'''ООП'''


# ТЕРМИНОЛОГИЯ
# ЗНАТЬ

class Book:  # имя класса всегда с заглавной буквы
    '''книга для обучения'''
    # АТРИБУТЫ КЛАССА(свойства класса):
    title = 'заголовок'
    pages = 143

    # метод
    def set_title(self, title):
        self.title = title

    def print_title(self):
        title = 'Кому на Руси жить хорошо'  # создали ПЕРЕМЕННУЮ
        print(title)  # напечатали ПЕРЕМЕННУЮ
        print(self.title)


class Animals:
    '''класс животных'''
    color = 'orange'
    weight = 55

    def sleep(self):
        pass


class Dogs(Animals):  # НАСЛЕДОВАНИЕ. теперь Dogs имеет атрибуты Animals
    '''класс собак'''
    number_of_legs = 4

    def layat(self):
        print('гав' * 3)


if __name__ == '__main__':
    book1 = Book()  # объект/экземпляр класса

    print(book1.pages)
    book1.pages = 493  # задаем значение атрибуту pages
    print(book1.pages)

    print(book1.title)
    book1.set_title('Как закалялась сталь')
    print(book1.title)

    book1.print_title()

    print(type(book1) == Book)  # проверяет описан ли объект с помощью класса
    print(isinstance(book1, Book))

    book1.part = 1  # создаем атрибут класса внутри объекта
    print(book1.part)

    Book.year = 2023  # добавляем атрибут в класс(те он появится и у всех объектов класса)
    setattr(book1, 'title', 'lalala')  # заменили атрибут объекта book1(также можно и создавать новые)

    print(getattr(book1, 'color', 'такого свойства нет'))  # работает по принципу .get в словарях(проверка атрибутов)

    print(hasattr(Book, 'year'))  # проверяет есть ли такой атрибут в объекте book1

    print(hasattr(book1, 'part'))
    del book1.part  # удаляет ЧТО УГОДНО
    print(hasattr(book1, 'part'))

    delattr(Book, 'year')  # удаляет ТОЛЬКО АТРИБУТЫ/МЕТОДЫ

    # МАГИЧЕСКИЕ МЕТОДЫ
    print(book1.__dict__)  # вернет словарь из атрибутов и из значений

    print(book1.__doc__)  # возвращает описание класса(только то, что после объявления класса и в ''' ''')

    print(type(book1).__name__)  # возвращает класс атрибута


def s(b, time, *args, error=0.01, **kwargs):  # аргументы без ключей - *args - аргументы с ключами - **kwargs
    # *args всегда пишется крайним аргументом в функции
    # *args это картеж из всего, что осталось без ключ-значений
    # **kwargs это словарь из всего, что осталось с ключ значением
    print('b:', b)
    print('time: ', time)
    print(args)
    print('kwargs: ', kwargs)
    print(args[1])
    print(kwargs.get('message', '404'))


if __name__ == '__main__':
    s(True, '11:30', 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
      message='труляля')  # аргументы без ключей - *args - аргументы с ключами
    print()
    s(*[1, 8, 0, 6],
      **{'1': 'one', '2': 'two'})  # разгруппировка


class Class:
    name = ''
    teacher = ''

    def __new__(cls, *args, **kwargs):  # выплняется при создании КЛАССА
        print('Привет')
        return super().__new__(cls)

    # атрибуты объекта
    def __init__(self, letter):  # выполняется после создания ОБЪЕКТА
        self.letter = letter

    def __del__(self):  # финализатор, выполняется при удалении класса
        # или при завершении работы программы
        print('delete attr Class')

    def method(self):
        pass


if __name__ == '__main__':
    c = Class('I')
    print(c.__dict__)
    # del c


# Pattern Singleton

class DataBase:
    __instance = None  # None == нет объекта, иначе ссылка на объект

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, password, port):
        self.user = user
        self.password = password
        self.port = port

    def connect(self):
        print(f'Connecting to DB {self.user}, {self.password}, {self.port}')

    def close(self):
        print('Closing DB')

    def read(self):
        return 'data from DB'


if __name__ == '__main__':
    db = DataBase('root', 'password', 80)
    db2 = DataBase('root2', 'password2', 40)


class Vector:
    min_coords = 0
    max_coords = 100

    @classmethod  # позволяет пользоваться только атрибутами класса,
    # доступ к атрибутам объекта закрыт
    def validate(cls, arg):  # --> без self, вместо него cls
        return cls.min_coords <= arg <= cls.max_coords

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    @staticmethod  # статический метод
    # (нет надобности создавать внутренние атрибуты для объекта)
    def norm2(x, y):
        return x + y

    """ИНКАПСУЛЯЦИЯ - ограничение доступа к данным и методам извне"""

    # attribute = public (без одного и двух подчеркиваний вначале)

    # _attribute = protected (одно подчеркивание вначале); служит для обращения внутри класса и
    # во всех дочерних классах, как предупреждение

    # __attribute = privat (два подчеркивания вначале); служит для обращения только внутри данного класса и
    # для обращения требует getter & setter

    class Bild:
        stock = 300
        _money = 0
        __password = '1234'

        @classmethod
        def get_password(cls):
            return cls.__password

        def set_password(self, psw):
            if type(psw) is str and 4 < len(psw) < 8:
                self.__password = psw

    print(Bild._money)
    print(Bild.stock)
    print(Bild.get_password())

    print(dir(Bild))
    print(Bild.__dict__)
    Bild._Bild__password = '4321'
    print(Bild.__dict__)

    class Point:
        def __init__(self, x=0, y=0):
            self.__x = self.__y = 0
            if self.__check_value1(x) and self.check_value2(y):
                self.__x = x
                self.__y = y

        @classmethod
        def __check_value1(cls, x):
            return type(x) in (int, float)

        @private  # всегда первый(самый главный)
        @classmethod
        def check_value2(cls, x):
            return type(x) in (int, float)

        def get_coord(self):
            return self.__x, self.__y

        def set_coord(self, x, y):
            if self.__check_value1(x) and self.check_value2(y):
                self.__x = x
                self.__y = y
            else:
                raise ValueError('Координаты должны быть числом!')

    pt = Point(1, 2)
    print(pt.__dict__)
    pt = Point('1', 2)
    print(pt.__dict__)
    print(pt.get_coord())
    pt.set_coord(3, 4)
    print(pt.get_coord())

    # pt.set_coord(3, '4') с ошибкой

    class Person:
        def __init__(self, name, age):
            self.__name = name
            self.__age = age

        def get_age(self):
            return self.__age

        def set_age(self, age):
            self.__age = age

        age = property(get_age, set_age)  # СНАЧАЛА ГЕТТЕР, А ПОТОМ СЕТТЕР
        # объединяет геттер и сеттер

    p = Person('Егор', 16)
    print(p.__dict__)
    p.age = 35
    print(p.__dict__)

    print('Age:', p.age)

    class Person2:
        def __init__(self, name, age):
            self.__name = name
            self.__age = age

        @property
        def age(self):
            return self.__age

        @age.setter
        def age(self, age):
            self.__age = age

        @age.deleter  # удаление приватного атрибута
        def age(self):
            del self.__age

    p = Person2('Егор', 16)
    print(p.__dict__)
    p.age = 35
    print(p.__dict__)

    print('Age:', p.age)

    from math import sin, pi

    '''МАГИЧЕСКИЕ МЕТОДЫ'''

    # __getattribute__
    # __setattr__
    # __getattr__
    # __delattr__

    class Point:
        min_coord = 0
        max_coord = 100

        def __init__(self, x, y):
            self.x = x
            self.y = y

        def set_coord(self, x, y):
            if self.min_coord <= x <= self.max_coord and \
                    self.min_coord <= y <= self.max_coord:
                self.x = x
                self.y = y

        # управление обращением к атрибуту ОБЪЕКТА (срабатывает при общащении к атрибуту ОБЪЕКТА)
        def __getattribute__(self, item):
            print('__getattribute__')

            if item == 'x':
                raise ValueError('Доступ запрещен')
            else:
                return object.__getattribute__(self, item)  # необходимо для присваивания

        # управление присваиванием атрибутов ОБЪЕКТА КЛАССА (вкулючается при измении атрибуктов ОБЪЕКТА класса)
        def __setattr__(self, key, value):
            print('__setattr__')
            if key == 'z':  # if key == 'z' - к ключу атрибута
                raise AttributeError('Недопустимое имя атрибута')
            else:
                object.__setattr__(self, key, value)
                # self.__dict__[key] = value

        # управляет обращением к НЕСУЩЕСТВУЮЩЕМУ атрибуту ОБЪЕКТА класса
        def __getattr__(self, item):
            print('__getattr__')
            return False

        # удаление атрибута
        def __delattr__(self, item):
            print('__delattr__')
            object.__delattr__(self, item)

    class Counter:  # класс с методом __call__ называется функтор
        def __init__(self):
            self.__counter = 0

        # нужно для управления вызовом от объекта класса
        def __call__(self, *args, **kwargs):
            print('__call__')
            self.__counter += 1
            return self.__counter

    class Derivate:  # производная
        def __init__(self, funk):  # funk - расширяемая (оборачиваемая) функция
            self.__fn = funk  # ссылка на расширяемую функцию

        def __call__(self, x, dx=0.0001, *args, **kwargs):
            return (self.__fn(x + dx) - self.__fn(x)) / dx

    if __name__ == '__main__':
        '''pt1 = Point(1, 2)  # setattr, setattr, no getattribute, getattribute!
        pt2 = Point(10, 20)  # setattr, setattr, no getattribute, getattribute!

        print()
        b = Point.max_coord  #обращаемся к классу --> не сработает никакой магический метод
        print(b) # 100

        print()
        a = pt1.y # __getattribute__
        print(a) # 2

        print()
        print(pt1.a) # __getattr__, False

        print()
        del pt1.x # __delattr__

        print()
        pt1.z = 6  # AttributeError('Недопустимое имя атрибута')
        pt1.z = '5'  # AttributeError('Недопустимое имя атрибута')
        x = pt1.x  # ValueError('Доступ запрещен')

        #x = pt1.x  доступ запрещен'''

        c_url = Counter  # ссылка на класс Counter. Теперь Counter можно вызывать через переменную c_url
        d = c_url()  # == Counter()
        c = Counter()
        c()  # ошибки нет
        c()  # ошибки нет
        c()  # ошибки нет
        print(c())
        print()
        c2 = Counter()
        print(c2())

        @Derivate
        def f_sin(x):
            return sin(x)

        print(f_sin(pi / 6))

        # ------

        class Person:
            def __init__(self, name):
                self.name = name

            def __str__(self):  # отражает информацию об объекте класса, например, с помощью print() или str()
                print('__str__')
                return f'{self.name}'

            def __repr__(self):  # отображает информацию об объекте класса В РЕЖИМЕ ОТЛАДКИ
                print('__repr__')
                return f'{self.__class__}: {self.name}'

        class Point:
            def __init__(self, *args):
                self.coords = args

            def __len__(self):  # разрешает применять функцию len() к объектам класса
                print('__len__')
                return len(self.coords)

            def __abs__(self):  # разрешает применять функцию abs() к объектам класса
                print('__abs__')
                return list(map(abs, self.coords))

        # add = для операции сложения +
        # sub = для операции вычитания -
        # mul = для операции умножения *
        # truediv = для операции деления /
        # floordiv = для операции целочисленного деления //
        # mod = для операции взятия остатка от деления %

        # eq = для операции '==' (убийство hash)
        # ne = для операции '!='
        # lt = для операции '<'
        # le = для операции '<='
        # gt = для операции '>'
        # ge = для операции '>='

        class Clock:
            __day = 86400

            def __init__(self, sec: int):
                # isistance - проверка принадлежносли sec  к классу int
                if not isinstance(sec, int): raise TypeError('секунды должны быть int')
                self.sec = sec % self.__day

            def get_time(self):
                s = self.sec % 60
                m = self.sec // 60 % 60
                h = self.sec // 3600 % 24
                return f'{h:0>2}:{m:0>2}:{s:0>2}'

            @classmethod
            def __verification(cls, other):
                if not isinstance(other, (int, Clock)): raise ArithmeticError('должен быть int')
                return other.sec if isinstance(other, Clock) else other

            def __add__(self, other):
                return Clock(self.sec + self.__verification(other))

            def __radd__(self, other):
                return self + other

            def __iadd__(self, other):
                return self

            def __eq__(self, other):  # not __eq__ создздается автоматически при создании __eq__
                return self.sec == self.__verification(other)

            def __lt__(self, other):
                return self.sec < self.__verification(other)

        if __name__ == '__main__':
            p = Person('egor')
            print(p)  # обращение через __str__
            print(p.name)  # обращение через атрибут
            print(str(p))  # обращение к __str__

            print()

            pt = Point(12, 14, -15)
            print(f'{len(pt)}D')  # размероность точки: 1D, 2D, 3D ...
            print(abs(pt))  # насильный перевод координат точки в неотрицательную область

            print()

            c = Clock(5000)
            print(c.get_time())
            c.sec = c.sec + 100
            print(c.get_time())
            c += 500
            print(c.get_time())
            c = c + Clock(155)
            print(c.get_time())
            print()
            # -----
            c1 = Clock(1000)
            c2 = Clock(1000)
            print(c1 == c2)
            print(c1 < c2)

            # hash() формирует по определенному алгоритму целочисленное значение для неизменяемый объектов

            print(hash(123))
            print(hash('Python'))
            print(hash('Python'))
            print(hash((1, 2, 3)))
            # print(hash([1, 2, 3])) - ошибка, так как список НЕ изменяемый объеки

            """СВОЙСТВА ХЕША"""

            # 1)при чем для равных объектов на выходе всегда должны получаться равные хеши
            # 2а) обратное утверждение НЕВЕРНО
            # 2б) равные хеши не гарантируют равенство объектов: 'селедка - рыба, но не каждая рыба - селедка'
            # 3) если хеши не равны, то и объекты точно не равны

            class Point:
                def __init__(self, x, y):
                    self.x = x
                    self.y = y

                def __eq__(self, other):  # убийство hash
                    return self.x == other.x and self.y == other.y

                def __hash__(self):  # воскрешение hash
                    return hash((self.x, self.y))

            pt1 = Point(1, 2)
            pt2 = Point(1, 2)
            print(hash(pt1))
            print(pt1 == pt2)

            # =============

            # __bool__ - магический метод истинности

            print(f'bool(123): {bool(123)}')
            print(f'bool(-1): {bool(-1)}')
            print(f'bool(0): {bool(0)}')
            print(f'bool("Python"): {bool("Python")}')
            print(f'bool(""): {bool("")}')
            print(f'bool([False, None, 9]): {bool([False, None, 9])}')
            print(f'bool([]): {bool([])}')

            # __len__() вызывается функцией bool(), если мегический метод __bool__() не определен

            class Point:
                def __init__(self, x, y):
                    self.x = x
                    self.y = y

                def __len__(self):
                    print('__len__')
                    return self.x ** 2 + self.y ** 2

                def __bool__(self):
                    print('__bool__')
                    return self.x == self.y

            p = Point(1, 2)
            print(bool(p))
            print(len(p))
            print()
            p0 = Point(0, 0)
            print(len(p0))
            print(bool(p0))
            print()
            p1 = Point(10, 10)
            print(bool(p1))
            print(len(p1))

            # ==============

            # __getitem__(self, item) - нужен для получения значения по ключу item
            # __setitem__(self, key, value) - запись значения value по ключу key
            # __delitem__(self, key) - удаление элемента по ключу key

            class Student:
                def __init__(self, name, *marks):
                    self.name = name
                    self.marks = list(marks)
                    print(self.marks)

                def __getitem__(self, item):
                    if 0 <= item <= len(self.marks):
                        return self.marks[item]
                    else:
                        raise IndexError('Индекс вне границ!')

                def __setitem__(self, key, value):
                    if not isinstance(key, int) and key < 0:
                        raise TypeError('индекс int > 0!')
                    if key >= len(self.marks):
                        temp = key + 1 - len(self.marks)
                        self.marks.extend([None] * temp)
                    self.marks[key] = value

                def __delitem__(self, key):
                    if not isinstance(key, int) or key > len(self.marks) or 0 > key:
                        raise TypeError('неверное значение')
                    del self.marks[key]

            s = Student('egor', 2, 2, 3, 2, 2, 2)
            print(s.marks[2])
            print(s[0])
            s[20] = 5
            print(s[19])  # None
            print(s[20])  # 5
            # del s[23] не удалит, тк неверный индекс
            print(s.marks)

            # ============

            # __iter__(self) - получение итератора для перебора объекта
            # __next__(self) - переход к следующему значению и его считывание

            lst = [1, 2, 3, 4, 5, 6, 7, 8]
            it = iter(lst)
            print(next(it))  # 1
            print(next(it))  # 2
            print(next(it))  # 3 и так далее
            print('==============')

            class Arange:
                """range в вещественных числах"""

                def __init__(self, start=0.0, end=0.0, step=1.0):
                    self.start = start
                    self.end = end
                    self.step = step

                def __iter__(self):
                    self.value = self.start - self.step
                    return self

                def __next__(self):
                    if self.value + self.step < self.end:
                        self.value += self.step
                        return self.value
                    else:
                        raise StopIteration

            for x in iter(Arange(-34.6, 89, 3.3)):
                print(x)


"""НАСЛЕДОВАНИЕ"""

# issubclass принимает ТОЛЬКО КЛАССЫ
if 0:
    class Geom:
        pass


    class Line(Geom):
        pass


    print(f'issubclass(Line, Geom): {issubclass(Line, Geom)}')  # проверяет, наследован ли класс Line от класса Geom

# переопределение и расщирение класса
if 0:
    class Geom:
        name = 'Geom'

        def draw(self):  # переопределение
            print('рисую геометрию')


    class Line(Geom):
        def draw(self):  # расширение класса
            print('рисую линию')

# порядок обращениия к методам класса при наследовании
if 0:
    class Geom:
        name = 'Geom'

        def __init__(self):
            print('инициализация Geom')

        def draw(self):
            print('рисую геометрию')


    class Line(Geom):
        def draw(self):
            print('рисую геометрию')


    l = Line()  # инициализация Geom
    # вызвалм магический метод __call__(self, *args, *kwargs)
    # def __call__(self, *args, *kwargs):
    #   obj = self.__new__(self, *args, *kwargs)
    #   self.__init__(obj, *args, *kwargs)
    #   return obj

# super() = делегирование
# возвращает объект-посредник (следующий по __mro__ класс)
if 0:
    class Geom:
        name = 'Geom'

        def __init__(self, x1, y1, x2, y2):
            print(f'инициализация Geom для {self.__class__}')
            self.x1 = x1
            self.x2 = x2
            self.y1 = y1
            self.y2 = y2

        def draw(self):
            print('рисую геометрию')


    class Line(Geom):
        def draw(self):
            print('рисую геометрию')


    class Rectangle(Geom):
        def __init__(self, x1, y1, x2, y2, fill=None):
            super().__init__(x1, y1, x2, y2)  # вызываем в 1 очередь!
            print(f'инициализация Rectangle')
            self.fill = fill


    l = Line(0, 0, 10, 20)
    r = Rectangle(1, 2, 3, 4)
    print(r.__dict__)

# режимы доступа при наследовании
# - public
# - _protected = наследуется в дочерний класс
# - __private = он жестко привязан к классу, где создан
if 0:
    class Geom:
        name = 'Geom'

        def __init__(self, x1, y1, x2, y2):
            print(f'инициализация Geom для {self.__class__}')
            self.__x1 = x1
            self.__y1 = y1
            self.__x2 = x2
            self.__y2 = y2

        def draw(self):
            print('рисую геометрию')

        def get_coords(self):
            return (self.__x1, self.__x2)


    class Rectangle(Geom):
        def __init__(self, x1, y1, x2, y2, fill=None):
            super().__init__(x1, y1, x2, y2)
            print(f'инициализация Rectangle')
            self.__fill = fill

        def get_coords(self):
            return (self.__x1, self.__x2)


    r = Rectangle(1, 2, 3, 4)
    g = Geom(1, 2, 3, 4)
    print(r.__dict__)
    print(g.get_coords())  # надо вызывать именно от родительсткого класса, так как атрибуты приватные

# Полиморфизм - возможность работать с совершенно разными объектами ЕДИНЫМ ОБРАЗОМ
if 0:
    class Geom:
        def get_p(self): raise NotImplemented('в дочернем классе нет метода get_p')


    class Rectangle(Geom):
        def __init__(self, w, h): self.w, self.h = w, h

        def get_p(self): return 2 * (self.w + self.h)


    class Square(Geom):
        def __init__(self, a): self.a = a

        def get_p(self): return 4 * self.a


    class Triangle(Geom):
        def __init__(self, a, b, c): self.a, self.b, self.c = a, b, c


    geom = [Rectangle(1, 2), Rectangle(3, 4),
            Square(10), Square(15),
            Triangle(1, 2, 3)]

    t = Triangle(4, 5, 6)
    geom.append(t)

    for g in geom: print(g.get_p())

# множественное наследование (примеси)
if 0:
    import time


    class Goods:
        def __init__(self, name, weight, price):
            super().__init__()
            print(f'init Goods')
            self.name = name
            self.price = price
            self.weight = weight

        def print_info(self):
            print(f'{self.name}, {self.weight}, {self.price}')


    class LogVK:  # при множественном наследовании в __init__ ничего не передаем
        ID = 0

        def __init__(self):
            print('пользователь зарегестрирован')
            LogVK.ID += 1
            self.id = LogVK.ID

        def save_cell_log(self):
            print(f'пользователю {self.id} товар был продан в {time.ctime()}')

        def print_info(self): print(f'{self.id}')


    class NoteBook(Goods, LogVK):  # порядок наследования
        pass


    n = NoteBook('ASUS', 3, 150_000)
    n.print_info()
    n.save_cell_log()
    print(NoteBook.__mro__)  # порядок поиска метода в наследовании
    LogVK.print_info(n)  # вызовется print_info от второго по __mro__ класса

# __slots__ - ограничение названия локальных атрибутов класса + уменьшение занимаемой памяти под объект >> увеличение быстродействия с локальными атрибутами
if 1:
    if 0:
        class Point:
            def __init__(self, x, y):
                self.x = x
                self.y = y


        p = Point(1, 2)
        print(p.__dict__)
        p.z = 3
        print(p.__dict__)

    if 1:
        class Point2D:
            __slots__ = ('x', 'y')  # убийство __dict__

            # ограничение того, как ты можешь называть локальные атрибуты объекта

            def __init__(self, x, y):
                self.x, self.y = x, y


        p = Point2D(1, 2)
        p.x = 3
