# Добавьте в задачу Rectangle, которую писали ранее, исключение NegativeValueError, которое
# выбрасывается при некорректных значениях ширины и высоты, как при создании объекта,
# так и при установке их через сеттеры.

class Rectangle:
    __slots__ = ['_width', '_height', '_area']

    def __init__(self, width: int, height: int = None):
        if width > 0:
            self._width = width
        else:
            raise NegativeValueError('Ширина', width)
        if height > 0:
            self._height = height if height else width
        else:
            raise NegativeValueError('Высота', height)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise NegativeValueError('Ширина', value)
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise NegativeValueError('Высота', value)
        self._height = value

    def perimeter(self):
        return self.width * 2 + self.height * 2

    @property
    def area(self):
        return self.width * self.height

    def __add__(self, other):
        """Adding perimeters of two rectangles and returning a new rectangle with a resulting perimeter"""
        if isinstance(other, Rectangle):
            new_width = self.width + other.width
            new_height = float(self.height + other.height)
            return Rectangle(new_width, new_height)
        else:
            raise TypeError

    def __sub__(self, other):
        """Subtracting perimeters of two rectangles and returning a new rectangle with a resulting perimeter"""
        if isinstance(other, Rectangle):
            if self.width - other.width > 0 or self.height - other.height > 0:
                new_width = self.width - other.width
                new_height = float(self.height - other.height)
                return Rectangle(new_width, new_height)
            else:
                None
        else:
            raise ValueError

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area < other.area
        else:
            raise TypeError

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area == other.area
        else:
            raise TypeError

    def __le__(self, other):
        if isinstance(other, Rectangle):
            return self.area <= other.area
        else:
            raise TypeError

    def __str__(self):
        return f'Прямоугольник со сторонами {self.width} и {self.height}'

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'


class OwnBaseError(Exception):
    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return self.message


class NegativeValueError(OwnBaseError):
    def __init__(self, name: str, value: int):
        super(NegativeValueError, self).__init__(f'{name} должна быть положительной, а не {value}')


r = Rectangle(4, 4)
r.width = -3