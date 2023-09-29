
class Triangle:

    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c
        if not self._check_triangle():
            raise ValueError('Such triangle can not exist')

    def _check_triangle(self):
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return False
        if self.a >= self.b + self.c or self.b >= self.a + self.c or self.c >= self.a + self.b:
            return False
        return True

    def get_perimeter(self):
        return self.a + self.b + self.c

    def get_area(self):
        s = (self.a + self.b + self.c) / 2
        return round((s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5, 3)


triangle = Triangle(5, 2, 4)
print(triangle.get_area())
print(triangle.get_perimeter())
triangle = Triangle(0, 2, 4)
print(triangle.get_area())
