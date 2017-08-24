import copy
import sys
sys.path.insert(0, 'C:/Users/Vanadys3/Git/py-game-dev/')
from own_dev.Enemy import *

# This will hold a dictionary with Mob names and their respective call to their Enemy constructor

# Constructors
Bestiary = {
    "red_dragon": Enemy(name="red_dragon", display_name="Red Dragon", type="Draconian", spawn_ratio=0.001
                        , hp=5000, mp=1000, strength=100
                        , vitality=100, magic=20, spirit=20
                        , skill=10, speed=40
                        , status_resistances={"sleep": 100, "stop": 80, "confusion": 70, "madness": 10}),
    "white_dragon": Enemy(name="white_dragon", display_name="White Dragon", type="Draconian"
                          , spawn_ratio=0.001, hp=7000, mp=1500, strength=60
                          , vitality=120, magic=35, spirit=35
                          , skill=5, speed=25
                          , status_resistances={"sleep": 100, "stop": 80, "confusion": 70, "madness": 10}),
    "zombie": Enemy(name="zombie", display_name="Zombie", type="humanoid"
                    , spawn_ratio=0.50, hp=100, mp=0, strength=7
                    , vitality=5, magic=0, spirit=0
                    , skill=1, speed=5
                    , status_resistances={"sleep": 0, "stop": 10, "confusion": 100, "madness": 0}),
    "skeleton": Enemy(name="skeleton", display_name="Skeleton", type="humanoid"
                      , spawn_ratio=0.50, hp=80, mp=0, strength=10
                      , vitality=10, magic=0, spirit=0
                      , skill=1, speed=7
                      , status_resistances={"sleep": 100, "stop": 10, "confusion": 50, "madness": 0}),
    "black_rat": Enemy(name="black_rat", display_name="Black Rat", type="small_mamal"
                       , spawn_ratio=0.80, hp=50, mp=0, strength=3
                       , vitality=2, magic=0, spirit=0
                       , skill=0, speed=10
                       , status_resistances={"sleep": 100, "stop": 80, "confusion": 70, "madness": 10})
}

# Data
Bestiary_data = {
    "red_dragon": {"name": "red_dragon", "display_name": "Red Dragon", "image": "../assets/enemies/red_dragon.gif"
                   , "type": "Draconian", "legendary": 1
                   , "max_spawn": 1, "spawn_ratio": 0.01
                   , "hp": 5000, "mp": 1000, "strength": 100
                   , "vitality": 100, "magic": 20, "spirit": 20
                   , "skill": 10, "speed": 40
                   , "status_resistances": {"sleep": 100, "stop": 80, "confusion": 70, "madness": 10}
                   },
    "white_dragon": {"name": "white_dragon", "display_name": "White Dragon"
                     , "image": "../assets/enemies/white_dragon.png", "type": "Draconian", "legendary": 1
                     , "max_spawn": 1, "spawn_ratio": 0.005, "hp": 7000, "mp": 1500, "strength": 60
                     , "vitality": 120, "magic": 35, "spirit": 35
                     , "skill": 5, "speed": 25
                     , "status_resistances": {"sleep": 100, "stop": 80, "confusion": 70, "madness": 10}
                     },
    "zombie": {"name": "zombie", "display_name": "Zombie", "type": "humanoid", "legendary": 0
               , "image": "../assets/enemies/zombie.png"
               , "max_spawn": 3, "spawn_ratio": 1, "hp": 100, "mp": 0, "strength": 7
               , "vitality": 5, "magic": 0, "spirit": 0
               , "skill": 1, "speed": 5
               , "status_resistances": {"sleep": 0, "stop": 10, "confusion": 100, "madness": 0}
               },
    "skeleton": {"name": "skeleton", "display_name": "Skeleton", "image": "../assets/enemies/skeleton.png"
                 , "type": "humanoid", "legendary": 0
                 , "max_spawn": 2, "spawn_ratio": 0.90, "hp": 80, "mp": 0, "strength": 10
                 , "vitality": 10, "magic": 0, "spirit": 0
                 , "skill": 1, "speed": 7
                 , "status_resistances": {"sleep": 100, "stop": 10, "confusion": 50, "madness": 0}
                 },
    "black_rat": {"name": "black_rat", "display_name": "Black Rat", "image": "../assets/enemies/black_rat.png"
                  , "type": "small_mamal", "legendary": 0
                  , "max_spawn": 4, "spawn_ratio": 1, "hp": 50, "mp": 0, "strength": 3
                  , "vitality": 2, "magic": 0, "spirit": 0
                  , "skill": 0, "speed": 10
                  , "status_resistances": {"sleep": 100, "stop": 80, "confusion": 70, "madness": 10}
                  },
    "undead": {"name": "undead", "display_name": "Undead", "image": "../assets/enemies/red_dragon.gif"
               , "type": "humanoid", "legendary": 0
               , "max_spawn": 2, "spawn_ratio": 0.80, "hp": 150, "mp": 0, "strength": 5
               , "vitality": 4, "magic": 0, "spirit": 5
               , "skill": 0, "speed": 10
               , "status_resistances": {"sleep": 100, "stop": 80, "confusion": 70, "madness": 10}
               }
}




