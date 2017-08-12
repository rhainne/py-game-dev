import glob
from various_functions.pygame_custom_functions import *

LEFT = 1
MIDDLE = 2
RIGHT = 3


class MapCollection:
    def __init__(self, current_location="", map_list=None):
        self.current_location = current_location
        self.map_collection_img = glob.glob("../assets/maps/*")
        self.map_collection_surfaces = load_sprite_list(self.map_collection_img)
        self.map_collection = map_list
        self.map_collection_img_dict = {}
        self.load_map_collection_img_dict()

    def __len__(self):
        return len(self.map_collection)

    def __contains__(self, item):
        return item.name in self.map_collection

    def __getitem__(self, item):
        return self.map_collection[item.name]

    def show_map(self, display_width, display_height):
        map_pos = [display_width * 0.05, display_height * 0.05]
        checking_map = True
        while checking_map:
            for event in pygame.event.get():
                event_handler(event)
                if event.type == KEYUP:
                    if event.key == K_m:
                        pygame.mouse.set_visible(False)
                        return None
                self.switch_map(event)
            return self.map_collection_img_dict[self.current_location], map_pos

    def load_map_collection_img_dict(self):
        for i_map in self.map_collection:
            self.map_collection_img_dict[i_map.name] = pygame.image.load(i_map.img).convert()

    def switch_map(self, display_width, display_height, event):
        map_pos = [display_width * 0.05, display_height * 0.05]
        pos = pygame.mouse.get_pos()
        maps = list((filter(lambda i_map: i_map.name == self.current_location, self.map_collection)))
        if event.button == LEFT:
            if maps[0].frontiers is not None:
                for i in range(len(maps[0].frontiers)):
                    if maps[0].frontiers[i][0][0] + map_pos[0] <= pos[0] <= maps[0].frontiers[i][1][0] + map_pos[0]:
                        if maps[0].frontiers[i][0][1] + map_pos[1] <= pos[1] <= maps[0].frontiers[i][1][1] + map_pos[1]:
                            self.current_location = maps[0].inside_maps[i]

        if event.button == RIGHT:
            if maps[0].outside_map is not None:
                self.current_location = maps[0].outside_map
        return self.map_collection_img_dict[self.current_location], map_pos
