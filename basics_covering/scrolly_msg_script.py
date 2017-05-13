import pygame
from pygame.locals import *
from sys import exit

background_image_filename = '../assets/Valkyrie_Wallpaper.jpg'
SCREEN_SIZE = (1280, 768)

message = " This is a demonstration of the scrolly message script. "

pygame.init()


def exit_handler():
    pygame.quit()
    exit()

screen = pygame.display.set_mode(SCREEN_SIZE)
font = pygame.font.SysFont("arial", 80)
text_surface = font.render(message, True, (0, 0, 255))
x = 0
y = (SCREEN_SIZE[1] - text_surface.get_height()) / 2
background = pygame.image.load(background_image_filename).convert()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit_handler()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit_handler()

    screen.blit(background, (0, 0))

    x -= 1
    if x < -text_surface.get_width():
        x = 0

    screen.blit(text_surface, (x, y))
    screen.blit(text_surface, (x + text_surface.get_width(), y))
    pygame.display.update()
