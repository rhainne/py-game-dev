import pygame
from pygame.locals import *

pygame.init()

SCREEN_SIZE = (800, 600)
l_width, l_height = 800, 600
screen = pygame.display.set_mode(SCREEN_SIZE)

'''
Pygame will have to do more work if you are using images with
different formats, and that can potentially decrease game performance.
Convert all images using convert() method. convert_alpha() for images with alpha channel.
'''
blank_surfaces = pygame.Surface((256, 256))
blank_alpha_surface = pygame.Surface((256, 256), depth=32)

surface_1 = pygame.surface.Surface((l_width, l_height))
rect_1 = Rect((100, 100), (50, 10))
rect_2 = Rect((100, 200), (50, 10))

while True:
    for event in pygame.event.get():  # retrieve all items and remove them from the queue
        if event.type == QUIT:
            pygame.quit()
            exit()

        screen.blit(blank_surfaces, (0, 0))
        screen.blit(blank_alpha_surface, (0, 0))
        
        pygame.draw.rect(surface_1, (255, 0, 0), rect_1)
        pygame.draw.rect(surface_1, (0, 255, 0), rect_2)
