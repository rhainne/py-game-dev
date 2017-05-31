
from various_functions.pygame_custom_functions import *

pygame.init()

l_width, l_height = 1024, 800
screen = pygame.display.set_mode((l_width, l_height), 0, 32)
points = []

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit_handler()
        if event.type == MOUSEBUTTONDOWN:
            points.append(event.pos)

    screen.fill((255, 255, 255))

    if len(points) >= 3:
        pygame.draw.polygon(screen, (0, 255, 0), points, 10)
    for point in points:
        pygame.draw.circle(screen, (0, 0, 255), point, 5)

    pygame.display.update()
