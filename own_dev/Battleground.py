import numpy as np
import random
from own_dev.Bestiary import *
from own_dev.Regions import *
from own_dev.pygame_custom_functions import *


class Battleground(Stage):
    def __init__(self, screen, location):
        Stage.__init__(self, Regions_data[location]["background_img"])
        self.screen = screen
        self.location = location
        self.spawned_enemies = ""
        self.battle_loop()

    def spawn_enemies(self):
        # This function will create Enemy instances.
        # Enemies will be chosen from location.fauna_list
        # using the crowness modifier and min_/max_spawn attribute of each Enemy,
        # until a number between 1 and MAX_NUMBER_OF_ENEMIES is reached.

        # current_ratio = random.uniform(0, 1)
        current_ratio = 0.0000000001
        max_number_of_mobs = random.randint(1, Regions_data[self.location]["crowdness"])
        possible_mobs = []
        for mob in Regions_data[self.location]["fauna_list"]:
            if Bestiary_data[mob]["spawn_ratio"] > current_ratio:
                possible_mobs.append(mob)

        mobs_nearby = list(np.random.choice(possible_mobs, max_number_of_mobs))

        for mob in mobs_nearby:
            if mobs_nearby.count(mob) > Bestiary_data[mob]["max_spawn"]:
                for y in range(mobs_nearby.count(mob) - Bestiary_data[mob]["max_spawn"]):
                    del mobs_nearby[mobs_nearby.index(mob)]

        return mobs_nearby

    def battle_loop(self):
        battle_active = True
        # clock = pygame.time.Clock()
        # elapsed = 0.
        screen_size = self.screen.get_size()
        background = pygame.image.load(self.background_img).convert()
        background = pygame.transform.scale(background, screen_size)
        self.spawned_enemies = self.spawn_enemies()
        enemy_surfaces = []
        for enemy in self.spawned_enemies:
            enemy_surfaces.append(pygame.image.load(Bestiary_data[enemy]["image"]).convert_alpha())

        while battle_active:
            # seconds = elapsed / 1000.0
            for event in pygame.event.get():
                event_handler(event)

            self.screen.blit(background, (0, 0))
            first_coords = (50, 0)
            enemy_positions_gap = (screen_size[0] / len(enemy_surfaces), screen_size[0] / len(enemy_surfaces))

            for idx, enemy in enumerate(enemy_surfaces):
                self.screen.blit(enemy, (first_coords[0] + enemy_positions_gap[0] * idx, first_coords[1]))
            # elapsed = clock.tick(60)
            pygame.display.update()
