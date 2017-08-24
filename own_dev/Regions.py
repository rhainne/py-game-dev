import sys
sys.path.insert(0, 'C:/Users/Vanadys3/Git/py-game-dev/')
from own_dev.Location import *

#
# attributes = {
#     "name": "default_name",
#     "display_name": "Default Name",
#    "fauna_list": [],
#    "crowdness": 0,
#    "shop_list": [],
#    "weather": "",
#    "dominion_faction": "",
#    "political_tendency": "",
#    "people_political_tendency": ""
#}
#

dict_of_faunas = {
    "halfstat": ["red_dragon", "white_dragon"],
    "sandalaar": ["zombie", "skeleton"],
    "durna": ["red_dragon", "white_dragon", "zombie", "skeleton", "undead", "black_rat"],
    "middle_earth": ["zombie", "skeleton"]
}

# Data
Regions_data = {
    "halfstat": {"name": "halfstat", "display_name": "Halfs Tat", "fauna_list": dict_of_faunas["halfstat"]
                 , "crowdness": 4, "shop_list": [], "weather": "cloudy", "background_img": ""
                 },
    "sandalaar": {"name": "sandalaar", "display_name": "San-Dalaar", "fauna_list": dict_of_faunas["sandalaar"]
                  , "crowdness": 4, "shop_list": [], "weather": "rainy", "background_img": ""
                  },
    "durna": {"name": "durna", "display_name": "Durna", "fauna_list": dict_of_faunas["durna"]
              , "crowdness": 2, "shop_list": [], "weather": "sunny"
              , "background_img": "../assets/backgrounds/battle/battle_2.jpg"
              },
    "middle_earth": {"name": "middle_earth", "display_name": "Middle Earth", "fauna_list": dict_of_faunas["middle_earth"]
                     , "crowdness": 10, "shop_list": [], "weather": "cloudy"
                     , "background_img": "../assets/backgrounds/battle/battle_1.jpg"
                     }
}
