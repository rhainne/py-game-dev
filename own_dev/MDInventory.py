# This file will hold information needed for the constructor to create Items and Containers.

# Containers
Container_Data = {
    "muddy_bag": {
        "name": "muddy_bag", "max_capacity": 6, "img": "url a la imagen de muddy_bag"
    },
    "filthy_bag": {
        "name": "filthy_bag", "max_capacity": 8, "img": "url a la imagen de filthy_bag"
    },
    "small_bag": {
        "name": "filthy_bag", "max_capacity": 10, "img": "url a la imagen de small_bag"
    },
    "bag": {
        "name": "bag", "max_capacity": 12, "img": "url a la imagen de bag"
    }
}

# Items
Item_Data = {
    "hp_small_potion": {
        "x": 0, "y": 0, "name": "hp_small_potion", "display_name": "HP small potion"
    },
    "mp_small_potion": {
        "x": 0, "y": 0, "name": "mp_small_potion", "display_name": "MP small potion"
    },
    "hp_potion": {
        "x": 0, "y": 0, "name": "hp_potion", "display_name": "HP potion"
    },
    "mp_potion": {
        "x": 0, "y": 0, "name": "mp_potion", "display_name": "MP potion"
    },
    "copper_sword": {
        "x": 0, "y": 0, "name": "copper_sword", "display_name": "Copper sword"
    },
    "bronze_sword": {
        "x": 0, "y": 0, "name": "bronze_sword", "display_name": "Bronze sword"
    }
}

# Wearable Items
Wearable_item_Data = {
    "copper_sword": {
        "name": "copper_sword", "display_name": "Copper sword", "hp_mod": 20, "mp_mod": 0, "strength_mod": 3,
        "vitality_mod": 2, "magic_mod": 0, "spirit_mod": 0, "skill_mod": 0, "speed_mod": 1, "evasion_mod": 0,
        "mg_evasion_mod": 0, "accuracy_mod": 1, "luck_mod": 0,
        "status_resistances_mod": {"sleep_mod": 0, "stop_mod": 0, "confusion_mod": 0, "madness_mod": 0},
        "element_resistances_mod": {"fire_mod": 0, "ice_mod": 0, "earth_mod": 0, "water_mod": 0,
                                    "shadow_mod": 0, "light_mod": 0, "lightning_mod": 0
                                    },
        "is_set": False, "set_2_mod": [], "set_4_mod": [], "set_5_mod": []
    },
    "bronze_sword": {
        "name": "bronze_sword", "display_name": "Bronze sword", "hp_mod": 40, "mp_mod": 0, "strength_mod": 5,
        "vitality_mod": 2, "magic_mod": 0, "spirit_mod": 0, "skill_mod": 1, "speed_mod": 0, "evasion_mod": 0,
        "mg_evasion_mod": 0, "accuracy_mod": 1, "luck_mod": 0,
        "status_resistances_mod": {"sleep_mod": 0, "stop_mod": 0, "confusion_mod": 0, "madness_mod": 0},
        "element_resistances_mod": {"fire_mod": 0, "ice_mod": 0, "earth_mod": 0, "water_mod": 0,
                                    "shadow_mod": 0, "light_mod": 0, "lightning_mod": 0
                                    }
    },
    "golden_sword": {
        "name": "golden_sword", "display_name": "Golden sword", "hp_mod": 120, "mp_mod": 40, "strength_mod": 25,
        "vitality_mod": 7, "magic_mod": 7, "spirit_mod": 7, "skill_mod": 2, "speed_mod": 5, "evasion_mod": 0,
        "mg_evasion_mod": 0, "accuracy_mod": 3, "luck_mod": 1,
        "status_resistances_mod": {"sleep_mod": 0, "stop_mod": 0, "confusion_mod": 0, "madness_mod": 0},
        "element_resistances_mod": {"fire_mod": 0, "ice_mod": 0, "earth_mod": 0, "water_mod": 0,
                                    "shadow_mod": 0, "light_mod": 0, "lightning_mod": 0
                                    }
    }
}
