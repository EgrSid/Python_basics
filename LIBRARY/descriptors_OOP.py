"""ДЕСКРИПТОРЫ"""


# non-data descriptor (include only set_name, getter) только чтобы получать инфомацию

# data descriptors (include set_name, getter, setter, deleter)

class Integer: # дескриптор

    def __set_name__(self, instance, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value



class Point3D:

    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def verify_coord(cls, c):
        if type(c) is not int:
            raise TypeError('Координата должна быть целым числом!')


if __name__ == '__main__':
    pt3D = Point3D(1, 2, 3)
    print(pt3D.__dict__)
    pt3D._x = 3
    pt3D._y = 2
    pt3D._z = 1
    print(pt3D.__dict__)
