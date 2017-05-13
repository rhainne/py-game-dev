import pygame

pygame.init()
'''
If Pygame doesn't find the font you are asking for, it will use a default font that may not look the
same. The solution is to distribute the .ttf files with your game, but make sure you have permission from the
font author to do this!
'''
my_font_1 = pygame.font.SysFont("arial", 16)
# my_font_2 = pygame.font.Font("my_font.ttf", 16)
my_font_3 = pygame.font.SysFont("arial", 64)
# Has to be a single line; if you want multiple lines, you will have to break the string and use multiple render calls.
text_surface = my_font_3.render("Text render example_3.", True, (0, 0, 0), (255, 255, 255))
pygame.image.save(text_surface, "../assets/name.png")
