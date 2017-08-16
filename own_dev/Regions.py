import copy
import sys
sys.path.insert(0, 'C:/Users/Vanadys3/Git/py-game-dev/')
from own_dev.Location import *

attributes = {
    "name": "default_name",
    "display_name": "Default Name",
    "fauna_list": [],
    "crowdness": 0,
    "shop_list": [],
    "weather": "",
    "dominion_faction": "",
    "political_tendency": "",
    "people_political_tendency": ""
}

dict_of_faunas = {
    "halfstat": ["red_dragon", "white_dragon"],
    "sandalaar": ["zombie", "skeleton"],
    "durna": ["red_dragon", "white_dragon", "zombie", "skeleton", "undead", "black_rat"]
}

Regions = {
    "halfstat": Location(name="halfstat", display_name="Halfs Tat", fauna_list=dict_of_faunas["halfstat"]
                         , crowdness=4, shop_list=[], weather="cloudy"),
    "sandalaar": Location(name="sandalaar", display_name="San-Dalaar", fauna_list=dict_of_faunas["sandalaar"]
                          , crowdness=4, shop_list=[], weather="rainy"),
    "durna": Location(name="durna", display_name="Durna", fauna_list=dict_of_faunas["durna"]
                      , crowdness=2, shop_list=[], weather="sunny")
}

