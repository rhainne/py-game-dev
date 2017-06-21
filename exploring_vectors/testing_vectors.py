import numpy as np
import sys
sys.path.insert(0, 'C:/Users/Vanadys3/Git/py-game-dev/')
from various_functions.vector2 import Vector2

v = (10.0, 20.0)
v2_1 = Vector2(15.0, 20.0)
print(v)
print(v2_1)

# Using custom Vector2
A = (10.0, 20.0)
B = (50.0, 50.0)
AB = Vector2.from_points(A, B)
print(AB)
print('Magnitude: {}'.format(AB.get_magnitude()))

# Using NumPy
C = np.array([10., 20.])
D = np.array([50., 50.])
CD = D - C
print(CD)
print('Magnitude: {}'.format(np.sqrt(CD.dot(CD))))

# Custom Vector2 methods
# Normalization
AB.normalize()
print('Normalized AB: {}'.format(AB))

# Addition
vAB = Vector2(30.0, 40.0)
vCD = Vector2(10.0, 20.0)
print("Vector2 vAB: {}".format(vAB))
print("Vector2 vCD: {}".format(vCD))
vAD = vAB + vCD
print("Vector2 vAD: {}".format(vAD))

