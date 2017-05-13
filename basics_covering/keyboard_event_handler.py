
import pygame
from pygame.locals import *
from sys import exit

background_image_filename = '../assets/Valkyrie_Wallpaper.jpg'

pygame.init()

# screen = pygame.display.set_mode((640, 480), 0, 32)
screen = pygame.display.set_mode((1920, 1080), FULLSCREEN, 32)
background = pygame.image.load(background_image_filename).convert()

x, y = 0, 0
move_x, move_y = 0, 0

# Following line make pygame ignore mouse motion
pygame.event.set_blocked(MOUSEMOTION)

# pygame.event.set_blocked([KEYDOWN, KEYUP]) # set_blocked also works for specific keys
# pygame.event.set_blocked(None) # You can also unblock all events
# pygame.event.set_allowed(None) # Or block them

my_event = pygame.event.Event(KEYDOWN, key=K_SPACE, mod=0, unicode=u' ')  # you can also pass as dictionary
pygame.event.post(my_event)

CATONKEYBOARD = USEREVENT + 1
my_event = pygame.event.Event(CATONKEYBOARD, message="Bad cat!")
pygame.event.post(my_event)

print(pygame.display.list_modes())

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == CATONKEYBOARD:
            print(event.message)
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                move_x = -1
            elif event.key == K_RIGHT or event.key == K_d:
                move_x = +1
            elif event.key == K_UP or event.key == K_w:
                move_y = -1
            elif event.key == K_DOWN or event.key == K_s:
                move_y = +1
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                move_x = 0
            elif event.key == K_RIGHT:
                move_x = 0
            elif event.key == K_UP:
                move_y = 0
            elif event.key == K_DOWN:
                move_y = 0
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()

        x += move_x
        y += move_y

        screen.fill((0, 0, 0))
        screen.blit(background, (x, y))

        pygame.display.update()

