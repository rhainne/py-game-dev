import copy
import sys
sys.path.insert(0, 'C:/Users/Vanadys3/Git/py-game-dev/')
from own_dev.Enemy import *

# This will hold a dictionary with Mob names and their respective call to their Enemy constructor

Bestiary = {
    "red_dragon": Enemy(name="red_dragon", display_name="Red Dragon", type="Draconian"
                        , hp=5000, mp=1000, strength=100
                        , vitality=100, magic=20, spirit=20
                        , skill=10, speed=40
                        , status_resistances={"sleep": 100, "stop": 80, "confusion": 70, "madness": 10}),
    "white_dragon": Enemy(name="white_dragon", display_name="White Dragon", type="Draconian"
                          , hp=7000, mp=1500, strength=60
                          , vitality=120, magic=35, spirit=35
                          , skill=5, speed=25
                          , status_resistances={"sleep": 100, "stop": 80, "confusion": 70, "madness": 10})
}

enemies = [
    copy.copy(Bestiary["red_dragon"]),
    copy.copy(Bestiary["red_dragon"]),
    copy.copy(Bestiary["white_dragon"])
]

enemies[0].hp -= 1000

for enemy in enemies:
    print(enemy)
