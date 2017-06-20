from various_functions.pygame_custom_functions import *

"""
lines have a jagged appearance.
This is because a pixel can only be drawn at a coordinate on a grid, which may not lie directly underneath a
line if it is not horizontal or vertical. This effect is called ALIASING.
"""

pygame.init()

l_width, l_height = 1280, 800
screen = pygame.display.set_mode((l_width, l_height), 0, 32)

points = []

while True:
    for event in pygame.event.get():
        event_handler(event)
        if event.type == MOUSEMOTION:
            points.append(event.pos)
            if len(points) > 100:
                del points[0]
    screen.fill((0, 0, 0))
    if len(points) > 1:
        # pygame.draw.lines(screen, (255, 0, 0), False, points, 2)
        pygame.draw.aalines(screen, (255, 0, 0), False, points, 1)
    pygame.display.update()
