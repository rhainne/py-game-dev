
import pygame
from pygame.locals import *
from sys import exit

l_width = 1280
l_height = 800
SCREEN_SIZE = (l_width, l_height)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)


# Creates images with smooth gradients
def create_scales(height):
    red_scale_surface = pygame.surface.Surface(SCREEN_SIZE)
    green_scale_surface = pygame.surface.Surface(SCREEN_SIZE)
    blue_scale_surface = pygame.surface.Surface(SCREEN_SIZE)
    for x_coord in range(l_width):
        c = int((x_coord/float(l_width - 1)) * 255.)
        red = (c, 0, 0)
        green = (0, c, 0)
        blue = (0, 0, c)
        line_rect = Rect(x_coord, 0, 1, height)
        pygame.draw.rect(red_scale_surface, red, line_rect)
        pygame.draw.rect(green_scale_surface, green, line_rect)
        pygame.draw.rect(blue_scale_surface, blue, line_rect)
    return red_scale_surface, green_scale_surface, blue_scale_surface

red_scale, green_scale, blue_scale = create_scales(100)
color = [127, 127, 127]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()
                
    screen.fill((0, 0, 0))

    # Draw the scales to the screen
    screen.blit(red_scale, (0, 00))
    screen.blit(green_scale, (0, 100))
    screen.blit(blue_scale, (0, 200))

    x, y = pygame.mouse.get_pos()

    # If the mouse was pressed on one of the sliders, adjust the color component
    if pygame.mouse.get_pressed()[0]:
        for component in range(3):
            if y > component * 100 and y < (component + 1) * 100:
                color[component] = int((x / float(l_width - 1)) * 255.)
            pygame.display.set_caption("PyGame Color Test - " + str(tuple(color)))

    # Draw a circle for each slider to represent the current setting
    for component in range(3):
        pos = (int((color[component]/255.) * float(l_width - 1)), component * 100 + 40)
        pygame.draw.circle(screen, (255, 255, 255), pos, 20)

    pygame.draw.rect(screen, tuple(color), (0, 300, l_width, 300))

    pygame.display.update()
