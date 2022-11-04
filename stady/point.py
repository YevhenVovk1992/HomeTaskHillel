from math import sqrt


class Point:
    def __init__(self, x, y):
        self.__y = self.__x = None
        self.x = x
        self.y = y

    def __check_coord(self, x):
        if type(x) == int or type(x) == float:
            return True
        raise TypeError('Coordinates must be numbers')

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, number):
        if self.__check_coord(number):
            self.__x = number

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, number):
        if self.__check_coord(number):
            self.__y = number

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)

    @staticmethod
    def length(p1, p2):
        return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)


if 'name' == '__main__':
    point1 = Point(1, 2)
    point2 = Point(2, 2)
    sum = point1+point2
    print(sum.__dict__)
    print(Point.length(point1, point2))
