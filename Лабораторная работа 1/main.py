import doctest
import math


class Triangle:
    def __init__(self, side1: float, side2: float, side3: float):
        """
        Создание и подготовка к работе объекта "Треугольник"

        :param side1: Длина первой стороны треугольника
        :param side2: Длина второй стороны треугольника
        :param side3: Длина третьей стороны треугольника

        :raise TypeError: Если тип передаваемых длин сторон треугольника не принадлежит классу int или float, то вызываем ошибку
        :raise ValueError: Если длина одной из сторон меньше или равно 0 или треугольник вырожденный, то вызываем ошибку

        Примеры:
        >>> triangle = Triangle(2, 3, 4)
        """
        if self.is_sides_ok(side1, side2, side3):
            self.side1, self.side2, self.side3 = side1, side2, side3

    @staticmethod
    def is_sides_ok(side1: float, side2: float, side3: float) -> bool:
        """
        Функуия для проверки сторон треугольника
        :param side1: Длина первой стороны треугольника
        :param side2: Длина второй стороны треугольника
        :param side3: Длина третьей стороны треугольника

        :return: Существует ли треугольник с указанными сторонами

        :raise TypeError: Если тип передаваемых длин сторон треугольника не принадлежит классу int или float, то вызываем ошибку
        :raise ValueError: Если длина одной из сторон меньше или равно 0 или треугольник вырожденный, то вызываем ошибку
        Примеры:
        >>> triangle = Triangle(2, 3, 4)
        >>> triangle.is_sides_ok(2, 3, 4)
        True
        """
        for side in (side1, side2, side3):
            if not isinstance(side, (int, float)):
                raise TypeError("Длина стороны треугольника должна быть типа int или float")
            if side <= 0:
                raise ValueError("Длина стороны треугольника должна быть больше 0")
        if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
            return True
        else:
            raise ValueError("Треугольник с заданными сторонами не существует")

    def get_perimeter(self) -> float:
        """
        Вычисление периметра треугольника

        :return: Периметр треугольника

        Примеры:
        >>> triangle = Triangle(2, 3, 4)
        >>> triangle.get_perimeter()
        9
        """
        return self.side1 + self.side2 + self.side3

    def get_area(self) -> float:
        """
        Вычисление площади треугольника

        :return: Площадь треугольника

        Примеры:
        >>> triangle = Triangle(2, 3, 4)
        >>> triangle.get_area()
        19.570385790780925
        """
        perimeter = self.get_perimeter()
        return math.sqrt(perimeter * (perimeter - self.side1) *
                         (perimeter - self.side2) + (perimeter - self.side3))

    def calc_triangle_angle(self, a: float, b: float, c: float) -> float:
        """
        Функция для вычисления угла треугольника по заданным сторонам
        :param a: Длина первой стороны треугольника
        :param b: Длина второй стороны треугольника
        :param c: Длина третьей стороны треугольника

        :return: Значение угла треугольника напротив третьей стороны
        Примеры:
        >>> triangle = Triangle(2, 3, 4)
        >>> triangle.calc_triangle_angle(2, 3, 4)
        104.47751218592992
        """
        if self.is_sides_ok(a, b, c):
            return math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b)) / math.pi * 180

    def get_angles(self) -> tuple:
        """
        Вычисление углов треугольника

        :return: Кортеж с углами напротив первой, второй и третьей стороны треугольника соответственно

        Примеры:
        >>> triangle = Triangle(2, 3, 4)
        >>> triangle.get_angles()
        (28.955024371859846, 46.56746344221023, 104.47751218592992)
        """
        angle1 = self.calc_triangle_angle(self.side3, self.side2, self.side1)
        angle2 = self.calc_triangle_angle(self.side1, self.side3, self.side2)
        angle3 = 180 - angle1 - angle2
        return angle1, angle2, angle3


class Rectangle:
    def __init__(self, side1: float, side2: float):
        """
        Создание и подготовка к работе объекта "Прямоугольник"

        :param side1: Длина первой стороны прямоугольника
        :param side2: Длина второй стороны прямоугольника

        :raise TypeError: Если тип передаваемых длин сторон прямоугольника не принадлежит классу int или float, то вызываем ошибку
        :raise ValueError: Если длина одной из сторон меньше или равно 0, то вызываем ошибку

        Примеры:
        >>> rectangle = Rectangle(2, 3)
        """
        if self.is_sides_ok(side1, side2):
            self.side1, self.side2 = side1, side2

    @staticmethod
    def is_sides_ok(side1: float, side2: float) -> bool:
        """
        Функуия для проверки сторон прямоугольника
        :param side1: Длина первой стороны прямоугольника
        :param side2: Длина второй стороны прямоугольника

        :return: Существует ли прямоугольник с указанными сторонами

        :raise TypeError: Если тип передаваемых длин сторон прямоугольника не принадлежит классу int или float, то вызываем ошибку
        :raise ValueError: Если длина одной из сторон меньше или равно 0, то вызываем ошибку
        Примеры:
        >>> rectangle = Rectangle(2, 3)
        >>> rectangle.is_sides_ok(2, 3)
        True
        """
        for side in (side1, side2):
            if not isinstance(side, (int, float)):
                raise TypeError("Длина стороны прямоугольника должна быть типа int или float")
            if side <= 0:
                raise ValueError("Длина стороны прямоугольника должна быть больше 0")
        return True

    def get_perimeter(self) -> float:
        """
        Вычисление периметра прямоугольника

        :return: Периметр прямоугольника

        Примеры:
        >>> rectangle = Rectangle(2, 3)
        >>> rectangle.get_perimeter()
        10
        """
        return 2 * (self.side1 + self.side2)

    def get_area(self) -> float:
        """
        Вычисление площади прямоугольника

        :return: Площадь прямоугольника

        Примеры:
        >>> rectangle = Rectangle(2, 3)
        >>> rectangle.get_area()
        6
        """
        return self.side1 * self.side2


class Pentagon:
    def __init__(self, side1: float, side2: float, side3: float, side4: float, side5: float):
        """
        Создание и подготовка к работе объекта "Пятиугольник"

        :param side1: Длина первой стороны пятиугольника
        :param side2: Длина второй стороны пятиугольника
        :param side3: Длина третьей стороны пятиугольника
        :param side4: Длина четвертой стороны пятиугольника
        :param side5: Длина пятой стороны пятиугольника

        :raise TypeError: Если тип передаваемых длин сторон пятиугольника не принадлежит классу int или float, то вызываем ошибку
        :raise ValueError: Если длина одной из сторон меньше или равно 0 или пятиугольник не может существовать, то вызываем ошибку

        Примеры:
        >>> pentagon = Pentagon(3, 4, 4, 5, 6)
        """
        if self.is_sides_ok(side1, side2, side3, side4, side5):
            self.side1, self.side2, self.side3, self.side4, self.side5 = side1, side2, side3, side4, side5

    @staticmethod
    def is_sides_ok(side1: float, side2: float, side3: float, side4: float, side5: float) -> bool:
        """
        Функуия для проверки сторон пятиугольника
        :param side1: Длина первой стороны пятиугольника
        :param side2: Длина второй стороны пятиугольника
        :param side3: Длина третьей стороны пятиугольника
        :param side4: Длина четвертой стороны пятиугольника
        :param side5: Длина пятой стороны пятиугольника

        :return: Существует ли пятиугольник с указанными сторонами

        :raise TypeError: Если тип передаваемых длин сторон пятиугольника не принадлежит классу int или float, то вызываем ошибку
        :raise ValueError: Если длина одной из сторон меньше или равно 0 или пятиугольник не может существовать, то вызываем ошибку
        Примеры:
        >>> pentagon = Pentagon(3, 4, 4, 5, 6)
        >>> pentagon.is_sides_ok(3, 4, 4, 5, 6)
        True
        """
        sides = (side1, side2, side3, side4, side5)
        sorted_sides = sorted(sides)
        if sorted_sides[0] + sorted_sides[1] > sorted_sides[4] and sorted_sides[1] + sorted_sides[2] > sorted_sides[3]:
            return True
        else:
            return False

    def get_perimeter(self) -> float:
        """
        Вычисление периметра пятиугольника

        :return: Периметр пятиугольника

        Примеры:
        >>> pentagon = Pentagon(3, 4, 4, 5, 6)
        >>> pentagon.get_perimeter()
        22
        """
        return self.side1 + self.side2 + self.side3 + self.side4 + self.side5

    def get_area(self) -> float:
        """
        Вычисление площади пятиугольника

        :return: Площадь пятиугольника

        Примеры:
        >>> pentagon = Pentagon(3, 4, 4, 5, 6)
        >>> pentagon.get_area()
        108.44353369380767
        """
        a, b, c, d, e = self.side1, self.side2, self.side3, self.side4, self.side5
        s = (a + b + c + d + e) / 2
        area = math.sqrt((s - a) * (s - b) * (s - c) * (s - d) * (s - e))
        return area


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации