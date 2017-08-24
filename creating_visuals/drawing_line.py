from own_dev.pygame_custom_functions import *

pygame.init()

l_width, l_height = 1280, 800
screen = pygame.display.set_mode((l_width, l_height), 0, 32)

while True:
    for event in pygame.event.get():
        event_handler(event)

    screen.fill((0, 0, 0))

    mouse_pos = pygame.mouse.get_pos()

    for x in range(0, l_width, 20):
        pygame.draw.line(screen, (255, 255, 255), (x, 0), mouse_pos)
        pygame.draw.line(screen, (255, 255, 255), (x, (l_height - 1)), mouse_pos)

    for y in range(0, l_height, 20):
        pygame.draw.line(screen, (255, 255, 255), (0, y), mouse_pos)
        pygame.draw.line(screen, (255, 255, 255), ((l_width - 1), y), mouse_pos)

    pygame.display.update()
