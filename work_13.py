
class TriangleNotValid(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class Triangle:
    def __init__(self, a: int | float,
                     b: int | float,
                     c: int | float):
        self.a = a
        self.b = b
        self.c = c
        try:
            if (a < 0) and (b < 0) and (c < 0):
                raise TriangleNotValid("Недопустимые аргументы")
        except TriangleNotValid as e:
            print(e)

    def existence_triangle(self) -> str:
        if (self.a + self.b > self.c and self.b + self.c > self.a and self.a + self.c > self.b):
            print("Треугольник существует!")
            return True
        else:
            print("Треугольник не существует!")
            return False

    def triangle_versatile(self) -> str:
        if (self.a != self.c) and (self.b != self.c) and (self.a != self.b):
            print("Треугольник разносторонний!")
            return True
        else:
            return False

    def triangle_equilateral(self) -> str:
        if self.a == self.c == self.b:
            print("Треугольник равносторонний!")
            return True
        else:
            return False

    def triangle_isosceles(self) -> str:
        if (self.a == self.c) or (self.b == self.c) or (self.a == self.b):
            print("Треугольник равнобедренний!")
            return True
        else:
            return False



side_riangle = Triangle(-3,4,-5)

print(side_riangle)
     # side_riangle.existence_triangle(),
     # side_riangle.triangle_versatile(),
     # side_riangle.triangle_equilateral(),
     # side_riangle.triangle_isosceles(),
     # side_riangle.triangle_isosceles())

