import sys
sys.path.insert(0, 'C:/Users/Vanadys3/Git/py-game-dev/')
from various_functions.pygame_custom_functions import *
from various_functions.vector2 import Vector2

background_image_filename = '../assets/chess1280x800.png'
sprite_image_filename = '../assets/pawn.png'

l_width, l_height = 800, 600

pygame.init()

screen = pygame.display.set_mode((l_width, l_height), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()

position = Vector2(100.0, 100.0)
speed = 250
heading = Vector2()

while True:
    for event in pygame.event.get():
        event_handler(event)
    if event.type == MOUSEBUTTONDOWN:
        destination = Vector2(*event.pos) - (Vector2(*sprite.get_size())/2)
        heading = Vector2.from_points(position, destination)
        heading.normalize()

    screen.blit(background, (0, 0))
    screen.blit(sprite, (position.x, position.y))

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    distance_moved = time_passed_seconds * speed
    position += heading * distance_moved

    pygame.display.update()
