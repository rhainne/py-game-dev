from various_functions.pygame_custom_functions import *
from random import *

pygame.init()

l_width, l_height = 1280, 800
screen = pygame.display.set_mode((l_width, l_height), 0, 32)

for _ in range(25):
    random_color = (randint(0,255), randint(0,255), randint(0,255))
    random_pos = (randint(0,639), randint(0,479))
    random_radius = randint(1,200)
    pygame.draw.circle(screen, random_color, random_pos, random_radius)
    pygame.display.update()

while True:
    for event in pygame.event.get():
        event_handler(event)
