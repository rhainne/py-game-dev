from various_functions.pygame_custom_functions import *

pygame.init()

l_width, l_height = 1280, 800

screen = pygame.display.set_mode((l_width, l_height), 0, 32)

while True:
    for event in pygame.event.get():
        event_handler(event)
    x, y = pygame.mouse.get_pos()
    screen.fill((255, 255, 255))
    pygame.draw.ellipse(screen, (0, 255, 0), (0, 0, x, y))
    pygame.display.update()
