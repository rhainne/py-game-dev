
from various_functions.pygame_custom_functions import *

background_image_filename = 'assets/chess1280x800.png'
sprite_image_filename = 'assets/pawn.png'
l_width, l_height = 1280, 800

pygame.init()

screen = pygame.display.set_mode((l_width, l_height), 0, 32)
background = pygame.image.load(background_image_filename).convert()
pawn_sprite = pygame.image.load(sprite_image_filename)

# The x coordinate of our sprite
x = 0.

while True:
    for event in pygame.event.get():
        event_handler(event)
    screen.blit(background, (0, 0))
    screen.blit(pawn_sprite, (x, 100))
    x += 1
    # If the image goes off the end of the screen, move it back
    if x > l_width:
        x -= l_width
    pygame.display.update()
