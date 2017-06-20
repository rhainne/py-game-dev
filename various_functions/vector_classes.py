class Vector2:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

    def from_points(p1, p2):
        return Vector2(p2[0] - p1[0], p2[1] - p1[1])
