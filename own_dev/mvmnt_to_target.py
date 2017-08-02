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
direction = Vector2(0, 0)
destination = Vector2(0, 0)
sprite_speed = 300
sprite_rotation = 0
sprite_rotation_speed = 360  # Degrees per second

# Falta que se detenga cuando llegue.
while True:
    for event in pygame.event.get():
        event_handler(event)
        if event.type == MOUSEBUTTONDOWN:
            # Hacer que la cabeza del sprite apunte a destination
            # La cabeza del sprite es (sprite.get_size()[0] / 2, sprite.get_size()[1])
            destination = Vector2(*event.pos) - (Vector2(*sprite.get_size()) / 2)
            direction = Vector2.from_points(sprite_pos, destination)
            direction.normalize()
            sprite = pygame.transform.rotate(sprite, 50)

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    distance_moved = time_passed_seconds * sprite_speed
    sprite_pos += direction * distance_moved

    # Compute to decide when to stop the sprite
    if (destination.get_x() - 1 < sprite_pos.get_x() < destination.get_x() + 1) \
            and (destination.get_y() - 1 < sprite_pos.get_y() < destination.get_y() + 1):
        direction = Vector2(0, 0)  # This stops the sprite
    sprite_pos += direction * sprite_speed * time_passed_seconds

    screen.blit(background, (0, 0))
    screen.blit(sprite, sprite_pos)

    pygame.display.update()
