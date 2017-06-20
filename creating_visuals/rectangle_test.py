
from random import *
from various_functions.pygame_custom_functions import *

l_width, l_height = 1024, 800

pygame.init()

screen = pygame.display.set_mode((l_width, l_height), 0, 32)

screen.lock()
for count in range(20):
    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    random_pos = (randint(0, (l_width - 1)), randint(0, (l_height - 1)))
    random_size = ((l_width - 1) - randint(random_pos[0], (l_width - 1)), (l_height - 1)-randint(random_pos[1], (l_height - 1)))
    pygame.draw.rect(screen, random_color, Rect(random_pos, random_size))
screen.unlock()
pygame.display.update()

while True:
    for event in pygame.event.get():
        event_handler(event)
