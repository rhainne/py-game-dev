from various_functions.pygame_custom_functions import *

background_image_filename = 'assets/chess1280x800.png'
sprite_image_filename = 'assets/pawn.png'

l_width, l_height = 1280, 800

pygame.init()

screen = pygame.display.set_mode((l_width, l_height), 0, 32)
background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename)

# Our clock object
clock = pygame.time.Clock()
# X coordinate of our sprite
x = 0
# Speed in pixels per second
speed = 5000

while True:
    for event in pygame.event.get():
        event_handler(event)

    screen.blit(background, (0, 0))
    screen.blit(sprite, (x, 100))
    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    distance_moved = time_passed_seconds * speed
    x += distance_moved
    if x > l_width:
        x -= l_width
    pygame.display.update()
