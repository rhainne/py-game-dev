import sys
sys.path.insert(0, 'C:/Users/Vanadys3/Git/py-game-dev/')
sys.path.insert(0, '/home/rain/Git/py-game-dev/')
sys.path.insert(0, 'C:/Users/rain_/PycharmProjects/py-game-dev')
from own_dev.Character import *

l_width, l_height = 1024, 720
background_image_filename = '../assets/chess1280x800.png'

pygame.init()
screen = pygame.display.set_mode((l_width, l_height), 0, 32)

background = pygame.image.load(background_image_filename).convert()

knight_1 = Character()
heading = 0

while True:
    for event in pygame.event.get():
        event_handler(event)

        pressed_keys = pygame.key.get_pressed()
        pressed_mods = pygame.key.get_mods()

        if pressed_keys[K_RIGHT]:
            if pressed_mods == 64:  # 64 == Left Control Key
                knight_1.state = "RUN"
                heading = 2
            else:
                knight_1.state = "WALK"
                heading = 1
        if pressed_keys[K_LEFT]:
            if pressed_mods == 64:  # 64 == Left Control Key
                knight_1.state = "RUN"
                heading = -2
            else:
                knight_1.state = "WALK"
                heading = -1

        if event.type == KEYUP:
            if event.key == K_RIGHT:
                knight_1.state = "IDLE"
                heading = 0
            if event.key == K_LEFT:
                knight_1.state = "IDLE"
                heading = 0

    if knight_1.x > l_width:
        knight_1.x = -147
    screen.blit(background, (0, 0))
    knight_1.update(heading, screen)

    pygame.display.update()
