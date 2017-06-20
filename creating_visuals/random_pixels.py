from random import randint
from various_functions.pygame_custom_functions import *

l_width, l_height = 1024, 800

pygame.init()
screen = pygame.display.set_mode((l_width, l_height), 0, 32)

while True:
    for event in pygame.event.get():
        event_handler(event)

    rand_col = (randint(0, 255), randint(0, 255), randint(0, 255))
    for _ in range(100):
        rand_pos = (randint(0, l_width - 1), randint(0, l_height - 1))
        screen.set_at(rand_pos, rand_col)

    pygame.display.update()
