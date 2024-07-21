import matplotlib.pyplot as plt
from numpy import linspace
from math import sqrt, cos, sin, radians, pi

class Figures:
    '''общий класс для всех фигур'''
    name = 'Фигура'
    color = 'black'
    linewidth = 5
    x = []
    y = []

    def draw(self):
        pass

class Rect(Figures):
    '''класс прямоугольников'''
    name = 'Rectangle'
    x0 = 5
    y0 = 5
    high = 6
    weight = 10

    def get_cords(self):
        self.x = [self.x0-self.weight/2, self.x0-self.weight/2, self.x0+self.weight/2, self.x0+self.weight/2, self.x0-self.weight/2]
        self.y = [self.y0-self.high/2, self.y0+self.high/2, self.y0+self.high/2, self.y0-self.high/2, self.y0-self.high/2]

    def draw(self):
        self.get_cords()
        plt.figure()
        plt.grid(True)
        plt.suptitle(self.name, fontweight='bold', fontsize=25)
        plt.plot(self.x, self.y,
                 color=self.color, linewidth=self.linewidth)
        plt.show()

class Circle(Figures):
    '''класс окружностей'''
    name = 'Circle'
    x0 = 0
    y0 = 0
    r = 5
    x = []
    y = []

    def get_cords(self):
        for i in linspace(self.x0 - self.r, self.x0 + self.r, 1000):
            self.x.append(i)
            self.y.append(sqrt(self.r ** 2 - (i - self.x0) ** 2) + self.y0)
        for i in linspace(self.x0 + self.r, self.x0 - self.r, 1000):
            self.x.append(i)
            self.y.append(self.y0 - sqrt(self.r ** 2 - (i - self.x0) ** 2))
    def draw(self):
        self.get_cords()
        plt.figure()
        plt.grid(True)
        plt.suptitle(self.name, fontweight='bold', fontsize=25)
        plt.plot(self.x, self.y, '-', color=self.color, linewidth=self.linewidth)
        plt.axis('square')
        plt.show()


class Point(Figures):
    '''Класс точек'''
    name = 'Point'
    x = [5]
    y = [5]

    def draw(self):
        plt.figure()
        plt.grid(True)
        plt.suptitle(self.name, fontweight='bold', fontsize=25)
        plt.plot(self.x, self.y, 'o', color=self.color, linewidth=self.linewidth)
        plt.show()

class Line(Figures):
    '''Класс отрезков'''
    name = 'Line'
    x0 = 0
    y0 = 0
    a = 60 # угол наклона отрезка
    length = 8

    def draw(self):
        plt.figure()
        plt.grid(True)
        plt.suptitle(self.name, fontweight='bold', fontsize=25)
        plt.plot([self.x0, self.length * cos(radians(self.a))],
                 [self.y0, self.length * sin(radians(self.a))],
                 color=self.color, linewidth=self.linewidth)
        #plt.xlim(-10, 15) нужно, чтобы проверить угол наклона в масштабе
        #plt.ylim(-10, 15)
        plt.show()

class Triangle(Figures):
    '''Класс треугольников'''
    name = 'Triangle'
    x = [2, 4, 7, 2]
    y = [1, 5, 3, 1]
    x0 = 1
    y0 = 1
    alpha = 30 # угол между 2 известными сторонами
    a = 5
    b = 7

    def draw_by_points(self):
        plt.figure()
        plt.grid(True)
        plt.suptitle(self.name, fontweight='bold', fontsize=25)
        plt.plot(self.x, self.y, color=self.color, linewidth=self.linewidth)
        plt.show()
    def draw_by_2_sides(self):
        plt.figure()
        plt.grid(True)
        plt.suptitle(self.name, fontweight='bold', fontsize=25)
        plt.plot([self.x0, self.a * cos(radians(self.alpha)), self.x0 * sin(radians(self.alpha)), self.x0],
                 [self.y0, self.a * sin(radians(self.alpha)), self.b * cos(radians(self.alpha)), self.y0],
                 color=self.color, linewidth=self.linewidth)
        plt.show()

class Ellipse(Figures):
    '''класс эллипс'''
    name = 'Ellips'
    focus_a = 5
    focus_b = 3
    res_x = []
    res_y = []

    def draw(self):
        plt.figure()
        plt.grid(True)
        plt.suptitle(self.name, fontweight='bold', fontsize=25)
        plt.plot(self.res_x, self.res_y, color=self.color, linewidth=self.linewidth)
        plt.show()
    def make_list_points(self):
        for i in linspace(-1 * self.focus_a, self.focus_a, 1000):
            self.res_x.append(i)
            self.res_y.append(self.focus_b * sqrt(1 - i ** 2 / self.focus_a ** 2))
        for i in linspace(self.focus_a, -1 * self.focus_a, 1000):
            self.res_x.append(i)
            self.res_y.append(-1 * (self.focus_b * sqrt(1 - i ** 2 / self.focus_a ** 2)))


class Polygon(Figures):
    """Класс многоугольников"""
    name = 'Polygon'
    x0 = 0
    y0 = 0
    a = 3 # длина стороны правильного многоугольника
    res_x = []
    res_y = []

    def draw(self):
        plt.figure()
        plt.grid(True)
        plt.suptitle(self.name, fontweight='bold', fontsize=25)
        plt.plot(self.res_x, self.res_y, '-', color=self.color, linewidth=self.linewidth)
        plt.axis('square')
        plt.show()
    def make_list_points(self):
        self.r = self.a / (2 * sin(pi / self.n))
        for i in range(1, self.n + 1):
            self.res_x.append(self.x0 + self.r * cos(2 * pi * i / self.n))
            self.res_y.append(self.y0 + self.r * sin(2 * pi * i / self.n))
        i = 1
        self.res_x.append(self.x0 + self.r * cos(2 * pi * i / self.n))
        self.res_y.append(self.y0 + self.r * sin(2 * pi * i / self.n))

class Star(Figures):
    '''Класс звёздочек'''
    name = 'Star'
    x0 = 0
    y0 = 0
    a = 3  # длина стороны правильного многоугольника, в который можно вписать звезду
    x = []  # список с неправильной последовательностью точек
    y = []  # список с неправильной последовательностью точек
    res_x = []
    res_y = []
    def draw(self):
        plt.figure()
        plt.grid(True)
        plt.suptitle(self.name, fontweight='bold', fontsize=25)
        plt.plot(self.res_x, self.res_y, '-', color=self.color, linewidth=self.linewidth)
        plt.axis('square')
        plt.show()
    def make_list_points(self):
        self.r = self.a / (2 * sin(pi / self.n))
        # создание списка из значений с неправильным расположением точек
        for i in range(1, self.n + 1):
            self.x.append(self.x0 + self.r * cos(2 * pi * i / self.n))
            self.y.append(self.y0 + self.r * sin(2 * pi * i / self.n))

        # расставляю точки в списке как нужно для построения
        k = -2
        for i in range(len(self.x)):
            if i == 0:
                self.res_x.append(self.x[i])
                self.res_y.append(self.y[i])
            k += 2
            if k - 2 >= len(self.x):
                k = 3
            self.res_x.append(self.x[k + 2 - len(self.x)])
            self.res_y.append(self.y[k + 2 - len(self.y)])


if __name__ == '__main__':
    # ПРЯМОУГОЛЬНИК
    rect = Rect()
    rect.color = 'red'
    rect.linewidth = 3
    rect.draw()

    # ОКРУЖНОСТЬ
    circle = Circle()
    circle.color = 'green'
    circle.linewidth = 4
    circle.get_cords()
    circle.draw()

    # ТОЧКА
    point = Point()
    point.color = 'purple'
    point.linewidth = 10
    point.draw()

    # ОТРЕЗОК
    line = Line()
    line.color = 'pink'
    line.linewidth = 5
    line.draw()

    # ТРЕУГОЛЬНИК
    triangle = Triangle()
    triangle.color = 'green'
    triangle.linewidth = 3
    triangle.draw_by_points()

    # ОВАЛ
    ellips = Ellipse()
    ellips.make_list_points()
    ellips.draw()

    # МНОГОУГОЛЬНИК
    polygon = Polygon()
    polygon.color = 'purple'
    polygon.n = 5 # количество сторон многоугольника
    polygon.make_list_points()
    polygon.draw()

    # ЗВЕЗДА
    star = Star()
    star.n = 5
    star.color = 'pink'
    star.make_list_points()
    star.draw()