
class Enemy(object):
    def __init__(self, **kwargs):
        attributes = {
            "name": "default_name",
            "display_name": "Default Name",
            "image": "",
            "type": "",
            "max_spawn": 1,
            "spawn_ratio": 0.00,
            "level": 1,
            "hp": 1,
            "mp": 1,
            "strength": 0,
            "vitality": 0,
            "magic": 0,
            "spirit": 0,
            "skill": 0,
            "speed": 0,
            "evasion": 0,
            "mg_evasion": 0,
            "accuracy": 0,
            "luck": 0,
            "status_resistances": {
                "sleep": 0,
                "stop": 0,
                "confusion": 0,
                "madness": 0
            },
            "element_resistances": {
                "fire": 0,
                "ice": 0,
                "earth": 0,
                "water": 0,
                "shadow": 0,
                "light": 0,
                "lightning": 0
            },
            "loot": [
                {"loot": "no_loot",
                 "loot_rate": 0,
                 "count": 0}
            ],
            "drop": [
                {"drop": "no_drop",
                 "drop_rate": 0,
                 "count": 0}
            ],
            "exp": 0,
            "equipment": {
                "main_weapon": "",
                "secondary_weapon": "",
                "armor": "",
                "accessory": []
            }
        }

        for (prop, default) in list(attributes.items()):
            setattr(self, prop, kwargs.get(prop, default))

    def recalc_level_bonus(self):
        bonus = self.level / 100 + 1

        self.hp = self.hp * bonus
        self.mp = self.mp * bonus
        self.strength = self.strength * bonus
        self.vitality = self.vitality * bonus
        self.magic = self.magic * bonus
        self.spirit = self.spirit * bonus
        self.skill = self.skill * bonus
        self.speed = self.speed * bonus
        self.evasion = self.evasion * bonus
        self.mg_evasion = self.mg_evasion * bonus
        self.accuracy = self.accuracy * bonus

    def __str__(self):
        return "Name: {0}" \
               "\nLevel: {1}" \
               "\nHealth: {2}" \
               "\nMagic points: {3} " \
               "\nEquipment: {4}" \
               "\nStatus Resistances: {5}".format(self.display_name, self.level, self.hp, self.mp, self.equipment, self.status_resistances)

    __repr__ = __str__
