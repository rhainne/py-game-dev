import pygame


def scale_color(color, scale):
    red, green, blue = color
    red = int(red*scale)
    green = int(green*scale)
    blue = int(blue*scale)
    return red, green, blue


def exit_handler():
    pygame.quit()
    exit()


def saturate_color(color):
    red, green, blue = color
    red = min(red, 255)
    green = min(green, 255)
    blue = min(blue, 255)
    return red, green, blue
