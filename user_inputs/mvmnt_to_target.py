import sys
sys.path.insert(0, 'C:/Users/Vanadys3/Git/py-game-dev/')
sys.path.insert(0, '/home/rain/Git/py-game-dev/')
from various_functions.pygame_custom_functions import *
from various_functions.vector2 import Vector2
from math import *


l_width, l_height = 800, 600
background_image_filename = '../assets/chess1280x800.png'
sprite_image_filename = '../assets/pawn.png'

pygame.init()

screen = pygame.display.set_mode((l_width, l_height), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()

sprite_pos = Vector2(200, 150)
sprite_speed = 300
sprite_rotation = 0
sprite_rotation_speed = 360  # Degrees per second

while True:
    for event in pygame.event.get():
        event_handler(event)
        if event.type == MOUSEBUTTONDOWN:
            target = Vector2(event.pos)

    direction = Vector2.from_points(sprite_pos, target)
    direction.normalize()

    screen.blit(background, (0, 0))
    screen.blit(sprite, (300, 120))


    pygame.display.update()
