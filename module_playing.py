import random
import pygame

random.seed(100)
for roll in range(10):
    print(random.randint(1, 160))

print("Re-seeded")
random.seed(200)
for roll in range(10):
    print(random.randint(1, 150))

print("Re-seeded")
random.seed()
for roll in range(10):
    print(random.randint(1, 150))

if pygame.font is None:
    print("The font is not available on this platform")