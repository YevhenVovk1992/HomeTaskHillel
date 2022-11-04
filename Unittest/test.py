from point import Point
import unittest


class TestLineLength(unittest.TestCase):
    point1 = Point(1, 2)
    point2 = Point(2, 2)
    point3 = Point(-2, 2)
    point4 = Point(-2, -2)
    point5 = Point(2, -2)
    point6 = Point(2, 1)
    point7 = Point(1, 3)
    point8 = Point(1, 1)
    point9 = Point(3, 5)
    point10 = Point(0, 5)
    point11 = Point(-1, 5)
    point12 = Point(-1, -5)
    point13 = Point(1, -5)
    point14 = Point(-1, 1)
    point15 = Point(-1, -1)
    point16 = Point(0, -5)
    point17 = Point(0, 0)
    point18 = Point(0, 2)


    def test_point1(self):
        self.assertEqual(Point.length(self.point1, self.point2), 1.0)

    def test_point2(self):
        self.assertEqual(Point.length(self.point1, self.point3), 3)

    def test_point3(self):
        self.assertEqual(Point.length(self.point1, self.point4), 5)

    def test_point4(self):
        self.assertEqual(Point.length(self.point1, self.point5), 4.123105625617661)

    def test_point5(self):
        self.assertEqual(Point.length(self.point1, self.point6), 1.4142135623730951)

    def test_point6(self):
        self.assertEqual(Point.length(self.point1, self.point7), 1.0)

    def test_point7(self):
        self.assertEqual(Point.length(self.point1, self.point10), 3.1622776601683795)

    def test_point8(self):
        self.assertEqual(Point.length(self.point1, self.point9), 3.605551275463989)

    def test_point9(self):
        self.assertEqual(Point.length(self.point1, self.point17), 2.23606797749979)

    def test_point10(self):
        self.assertEqual(Point.length(self.point1, self.point8), 1.0)

    def test_point11(self):
        self.assertEqual(Point.length(self.point1, self.point11), 3.605551275463989)

    def test_point12(self):
        self.assertEqual(Point.length(self.point1, self.point14), 2.23606797749979)

    def test_point13(self):
        self.assertEqual(Point.length(self.point1, self.point12), 7.280109889280518)

    def test_point14(self):
        self.assertEqual(Point.length(self.point1, self.point15), 3.605551275463989)

    def test_point15(self):
        self.assertEqual(Point.length(self.point1, self.point16), 7.0710678118654755)

    def test_point16(self):
        self.assertEqual(Point.length(self.point1, self.point18), 1.0)

    def test_point17(self):
        self.assertEqual(Point.length(self.point1, self.point13), 7.0)
