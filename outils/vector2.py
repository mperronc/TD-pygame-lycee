import math

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __mul__(self, k):
        return Vector2(k * self.x, k * self.y)

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def length_squared(self):
        return self.x ** 2 + self.y ** 2

    def normalized(self):
        return Vector2(self.x / self.length(), self.y / self.length())

    def dot(self, other):
        return self.x * other.y + self.y * other.x

