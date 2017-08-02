import pygame
from pygame.locals import *


def scale_color(i_color, scale):
    if scale < 0:
        raise ValueError('Exception in scale_color function. Color cannot be scalled by negative scale value.')
    red, green, blue = i_color
    red = int(red*scale)
    green = int(green*scale)
    blue = int(blue*scale)
    return saturate_color((red, green, blue))  # Saturate color before retuning it


def exit_handler():
    pygame.quit()
    exit()


def event_handler(event):
    if event.type == QUIT:
        exit_handler()
    if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            exit_handler()


# Saturate color is used to keep always valid 0-255 color values.
def saturate_color(i_color):
    red, green, blue = i_color
    red = min(red, 255)
    green = min(green, 255)
    blue = min(blue, 255)
    return red, green, blue


# Possible usage of lerping to do a transition
# Define a range to loop over: lerp_range = (0.1, 0.2, 0.3, 0.4, 0.5)
def lerp(value1, value2, factor):
    return value1+(value2-value1)*factor


def blend_color(color1, color2, blend_factor):
    red1, green1, blue1 = color1
    red2, green2, blue2 = color2
    red = red1+(red2-red1)*blend_factor
    green = green1+(green2-green1)*blend_factor
    blue = blue1+(blue2-blue1)*blend_factor
    return int(red), int(green), int(blue)


def format_number(n, accuracy=6):
    """Formats a number in a friendly manner
    (removes trailing zeros and unneccesary point."""
    fs = "%."+str(accuracy)+"f"
    str_n = fs % float(n)
    if '.' in str_n:
        str_n = str_n.rstrip('0').rstrip('.')
    if str_n == "-0":
        str_n = "0"
    # str_n = str_n.replace("-0", "0")
    return str_n


def load_sprite_list(sprite_list):
    sprites = []
    for sprite in sprite_list:
        sprites.append(pygame.image.load(sprite).convert_alpha())
    return sprites
