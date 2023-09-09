import math


class Shape:
    def __init__(self, ):
        self.result = None

    def area_display(self):
        return "the area is = " + str(self.result)


# inhered Shape class
class Rectangle(Shape):
    def __init__(self, wight, hight):
        super().__init__()
        self.wight = wight
        self.hight = hight

    def area_cal(self, ):
        self.result = self.hight * self.wight


# inhered Shape class
class Circle(Shape):
    def __init__(self, radius):
        super(Circle, self).__init__()
        self.radius = radius

    def area_cal(self, ):
        self.result = math.pi * self.radius * self.radius


# inhered Shape Rectangle class
class Square(Rectangle):
    def __init__(self, a):
        super(Square, self).__init__(a, a)


# crate an object of Rectangle
r = Rectangle(3, 2)
r.area_cal()
print(r.area_display())

# Crate an object of Circle class
c = Circle(3)
c.area_cal()
print(c.area_display())

# Crate an object of Square class
s = Square(3)
s.area_cal()
print(s.area_display())
