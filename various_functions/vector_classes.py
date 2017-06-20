import math


class Vector2:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(X coord: {}, Y coord: {})".format(self.x, self.y)

    def from_points(p1, p2):
        return Vector2(p2[0] - p1[0], p2[1] - p1[1])

    def get_magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        magnitude = self.get_magnitude()
        self.x /= magnitude
        self.y /= magnitude
