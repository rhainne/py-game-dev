import sys
sys.path.insert(0, 'C:/Users/Vanadys3/Git/py-game-dev/')
from various_functions.pygame_custom_functions import *

l_width, l_height = 800, 600

pygame.init()
screen = pygame.display.set_mode((l_width, l_height), 0, 32)
font = pygame.font.SysFont("arial", 32)
font_height = font.get_linesize()

while True:
    for event in pygame.event.get():
        event_handler(event)

    screen.fill((255, 255, 255))
    pressed_key_text = []
    pressed_keys = pygame.key.get_pressed()
    y = font_height
    for key_constant, pressed in enumerate(pressed_keys):
        if pressed:
            key_name = pygame.key.name(key_constant)
            text_surface = font.render(key_name + " pressed", True, (0, 0, 0))
            screen.blit(text_surface, (8, y))
            y += font_height
        pygame.display.update()
