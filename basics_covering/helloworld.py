#!/usr/bin/env python

import pygame
from pygame.locals import *
from sys import exit

background_img_filename = '../assets/sushiplate.jpg'
mouse_img_filename = '../assets/fugu.jpg'

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("Sushi game")

background = pygame.image.load(background_img_filename).convert()  # Convert could discard alpha channel
mouse_cursor = pygame.image.load(mouse_img_filename).convert_alpha()  # convert_alpha to preserve image's alpha channel

while True:
    for event in pygame.event.get():  # retrieve all items and remove them from the queue
        if event.type == QUIT:
            pygame.quit()
            exit()

        screen.blit(background, (0, 0))

        x, y = pygame.mouse.get_pos()
        x -= mouse_cursor.get_width() / 2
        y -= mouse_cursor.get_height() / 2
        screen.blit(mouse_cursor, (x, y))

        pygame.display.update()
