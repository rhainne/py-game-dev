from various_functions.pygame_custom_functions import *

background_image_filename = 'assets/chess1280x800.png'
sprite_image_filename = 'assets/pawn.png'

l_width, l_height = 800, 600

pygame.init()

screen = pygame.display.set_mode((l_width, l_height), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()
x, y = 100, 100
speed_x, speed_y = 133, 170

while True:
    for event in pygame.event.get():
        event_handler(event)

    screen.blit(background, (0, 0))
    screen.blit(sprite, (x, y))

    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.0

    x += speed_x * time_passed_seconds
    y += speed_y * time_passed_seconds

    # If the sprite goes off the edge of the screen, make it move in the opposite direction
    if x > l_width - sprite.get_width():
        speed_x = -speed_x
        x = l_width - sprite.get_width()
    elif x < 0:
        speed_x = -speed_x
        x = 0
    if y > l_height - sprite.get_height():
        speed_y = -speed_y
        y = l_height - sprite.get_height()
    elif y < 0:
        speed_y = -speed_y
        y = 0
    pygame.display.update()
