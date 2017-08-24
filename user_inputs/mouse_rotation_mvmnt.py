import sys
sys.path.insert(0, 'C:/Users/Vanadys3/Git/py-game-dev/')
from own_dev.pygame_custom_functions import *
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

pygame.mouse.set_visible(False)
pygame.event.set_grab(True)  # pygame takes full control of the mouse
sprite_pos = Vector2(l_width / 2, l_height / 2)
sprite_speed = 300.
sprite_rotation = 0.
sprite_rotation_speed = 360.  # Degrees per second
mouse_sensitivity = 50.

while True:
    for event in pygame.event.get():
        event_handler(event)

    pressed_keys = pygame.key.get_pressed()
    pressed_mouse = pygame.mouse.get_pressed()
    movement_direction = 0.
    rotation_direction = pygame.mouse.get_rel()[0] / mouse_sensitivity

    if pressed_keys[K_LEFT]:
        rotation_direction = +1.
    if pressed_keys[K_RIGHT]:
        rotation_direction = -1.
    if pressed_keys[K_UP] or pressed_mouse[0]:  # mouse left button
        movement_direction = -1.
    if pressed_keys[K_DOWN] or pressed_mouse[2]:  # mouse right button
        movement_direction = +1.

    screen.blit(background, (0, 0))
    rotated_sprite = pygame.transform.rotate(sprite, sprite_rotation)
    w, h = rotated_sprite.get_size()
    sprite_draw_pos = Vector2(sprite_pos.x - w/2, sprite_pos.y - h/2)
    screen.blit(rotated_sprite, sprite_draw_pos)

    time_passed = clock.tick(60)
    time_passed_seconds = time_passed / 1000.0
    sprite_rotation += rotation_direction * sprite_rotation_speed * time_passed_seconds

    heading_x = sin(sprite_rotation * pi/180.)
    heading_y = cos(sprite_rotation * pi/180.)
    heading = Vector2(heading_x, heading_y)
    heading *= movement_direction
    sprite_pos += heading * sprite_speed * time_passed_seconds

    pygame.display.update()
