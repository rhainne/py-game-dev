
import pygame
from pygame.locals import *
from sys import exit

SCREEN_SIZE = (1280, 768)
background_image_filename = '../assets/Valkyrie_Wallpaper.jpg'

pygame.init()

'''
It is usually best to use the value 0 for windowed displays 
and FULLSCREEN for full-screen displays to ensure your game 
will work well on all platforms.

HWSURFACE: Surface created in your graphic card. Can speedup blitting but its not
supported in every platform. Can only be used in combination with FULLSCREEN
Example: screen = pygame.display.set_mode(SCREEN_SIZE, HWSURFACE | FULLSCREEN, 32)
You can also use Double buffer (DOUBLEBUF) with HWSURFACE. This creates 2 buffers, only one visible at a time
Example: screen = pygame.display.set_mode(SCREEN_SIZE, DOUBLEBUF | HWSURFACE | FULLSCREEN, 32)
'''


screen = pygame.display.set_mode(SCREEN_SIZE, NOFRAME, 32)  # Window with no border (NOFRAME)
background = pygame.image.load(background_image_filename).convert()

Fullscreen = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()
            if event.key == K_f:
                Fullscreen = not Fullscreen
            if Fullscreen:
                screen = pygame.display.set_mode((1280, 768), FULLSCREEN, 32)
            else:
                screen = pygame.display.set_mode((1280, 768), NOFRAME, 32)  # Window with no border (NOFRAME)

    screen.blit(background, (0, 0))
    pygame.display.update()
