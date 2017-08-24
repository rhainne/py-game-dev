from math import pi

from own_dev.pygame_custom_functions import *

pygame.init()

l_width, l_height = 800, 600

screen = pygame.display.set_mode((l_width, l_height), 0, 32)
while True:
    for event in pygame.event.get():
        event_handler(event)
    x, y = pygame.mouse.get_pos()
    angle = (x / float(l_width - 1)) * pi * 2.
    screen.fill((255, 255, 255))
    pygame.draw.arc(screen, (0, 0, 0), (0, 0, (l_width - 1), (l_height - 1)), 0, angle, 5)
    pygame.display.update()
