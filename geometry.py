import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        semi_perimeter = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(semi_perimeter * (semi_perimeter - self.side1) * (semi_perimeter - self.side2) * (semi_perimeter - self.side3))
        return area

    def is_right_angled(self):
        sides = sorted([self.side1, self.side2, self.side3])
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2

def calculate_area(shape):
    return shape.area()