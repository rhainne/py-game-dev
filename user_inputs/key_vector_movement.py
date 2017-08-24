import sys
sys.path.insert(0, 'C:/Users/Vanadys3/Git/py-game-dev/')
from own_dev.pygame_custom_functions import *
from various_functions.vector2 import Vector2

l_width, l_height = 800, 600
background_image_filename = '../assets/chess1280x800.png'
sprite_image_filename = '../assets/pawn.png'

pygame.init()

screen = pygame.display.set_mode((l_width, l_height), 0, 32)
background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()
clock = pygame.time.Clock()
sprite_pos = Vector2(200, 150)
sprite_speed = 250

while True:
    for event in pygame.event.get():
        event_handler(event)
    pressed_keys = pygame.key.get_pressed()
    key_direction = Vector2(0, 0)
    if pressed_keys[K_LEFT]:
        key_direction.x = - 1
    elif pressed_keys[K_RIGHT]:
        key_direction.x = + 1
    if pressed_keys[K_UP]:
        key_direction.y = - 1
    elif pressed_keys[K_DOWN]:
        key_direction.y = + 1

    key_direction.normalize()

    screen.blit(background, (0, 0))
    screen.blit(sprite, (sprite_pos.x, sprite_pos.y))

    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.0

    sprite_pos += key_direction * sprite_speed * time_passed_seconds

    pygame.display.update()
