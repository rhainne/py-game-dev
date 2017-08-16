import numpy as np
import random
from own_dev.Stage import *
from own_dev.Bestiary import *


class Battleground(Stage):
    def __init__(self, location):
        Stage.__init__(self, location.background_img)
        self.location = location
        self.spawned_enemies = self.spawn_enemies()
        print(self.spawned_enemies)

    def spawn_enemies(self):
        # This function will create Enemy instances.
        # Enemies will be chosen from location.fauna_list
        # using the crowness modifier and min_/max_spawn attribute of each Enemy,
        # until a number between 1 and MAX_NUMBER_OF_ENEMIES is reached.

        current_ratio = random.uniform(0, 1)
        max_number_of_mobs = random.randint(1, self.location.crowdness)
        possible_mobs = []
        for mob in self.location.fauna_list:
            if Bestiary_data[mob]["spawn_ratio"] > current_ratio:
                possible_mobs.append(mob)

        mobs_nearby = list(np.random.choice(possible_mobs, max_number_of_mobs))

        for mob in mobs_nearby:
            if mobs_nearby.count(mob) > Bestiary_data[mob]["max_spawn"]:
                for y in range(mobs_nearby.count(mob) - Bestiary_data[mob]["max_spawn"]):
                    del mobs_nearby[mobs_nearby.index(mob)]

        return mobs_nearby
