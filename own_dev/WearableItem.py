from own_dev.Inventory import *


class WearableItem(Item):
    def __init__(self, **kwargs):
        attributes = {
            "hp_mod": 0,
            "mp_mod": 0,
            "strength_mod": 0,
            "vitality_mod": 0,
            "magic_mod": 0,
            "spirit_mod": 0,
            "skill_mod": 0,
            "speed_mod": 0,
            "evasion_mod": 0,
            "mg_evasion_mod": 0,
            "accuracy_mod": 0,
            "luck_mod": 0,
            "status_resistances_mod": {
                "sleep_mod": 0,
                "stop_mod": 0,
                "confusion_mod": 0,
                "madness_mod": 0
            },
            "element_resistances_mod": {
                "fire_mod": 0,
                "ice_mod": 0,
                "earth_mod": 0,
                "water_mod": 0,
                "shadow_mod": 0,
                "light_mod": 0,
                "lightning_mod": 0
            },
            "is_set": False,
            "set_2_mod": [],
            "set_4_mod": [],
            "set_5_mod": []
        }
        for (prop, default) in list(attributes.items()):
            setattr(self, prop, kwargs.get(prop, default))

        Item.__init__(self.rect.x, self.rect.y, self.name, self.value
                      , self.weight, self.quantity, self.img, self.sound)

    # def on_equip(self):

    # def on_unequip(self):


