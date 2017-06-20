from various_functions.pygame_custom_functions import *

l_width = 1280
l_height = 800
SCREEN_SIZE = (l_width, l_height)

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
color1 = (0, 100, 100)
color2 = (255, 255, 0)
factor = 0.

while True:
    for event in pygame.event.get():
        event_handler(event)

    screen.fill((255, 255, 255))
    tri = [(0, 120), (l_width - 1, 80), (l_width - 1, 160)]
    pygame.draw.polygon(screen, (0, 200, 200), tri)
    pygame.draw.circle(screen, (0, 0, 0), (int(factor * float(l_width - 1)), 120), 15)
    x, y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:  # [0] for left click, [1] for wheel, [2] for right click
        factor = x / float(l_width - 1)
        pygame.display.set_caption("PyGame Color Blend Test - %.3f" % factor)

    color = blend_color(color1, color2, factor)
    pygame.draw.rect(screen, color, (0, 240, l_width, 240))

    pygame.display.update()
