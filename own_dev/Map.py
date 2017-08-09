import glob
import pygame
from various_functions.pygame_custom_functions import *


class Map:
    def __init__(self, current_location=""):
        self.init_location = "middle_earth"
        self.current_location = current_location
        self.map_collection = glob.glob("../assets/maps/*")
        self.map_collection_surfaces = load_sprite_list(self.map_collection)

        self.map_collection_dict = {'middle_earth': pygame.image.load("../assets/maps/middle_earth_map.jpg").convert()
                                    , 'rohan': pygame.image.load("../assets/maps/rohan_map.jpg").convert()}

    def show_map(self, display_width, display_height, display):
        map_pos = [display_width * 0.05, display_height * 0.05]
        checking_map = True
        while checking_map:
            for event in pygame.event.get():
                if event.type == KEYUP:
                    if event.key == K_m:
                        checking_map = False
            display.blit(self.map_collection_dict["rohan"], map_pos)
            pygame.display.update()
