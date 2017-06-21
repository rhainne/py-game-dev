import sys
sys.path.insert(0, 'C:/Users/Vanadys3/Git/py-game-dev/')
from various_functions.vector2 import Vector2

A = (10.0, 20.0)
B = (30.0, 35.0)
AB = Vector2.from_points(A, B)
step = AB * .1
position = Vector2(*A)
for n in range(10):
    position += step
    print(position)
