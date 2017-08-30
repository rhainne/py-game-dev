

class InBattleCharacter:
    def __init__(self, **kwargs):
        attributes = {
            "team_allies": [],
            "name": "",
            "display_name": "",
            "image": "",
            "type": "",
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
            "exp": 0,
            "equipment": {
                "main_weapon": "",
                "secondary_weapon": "",
                "helmet": "",
                "gloves": "",
                "boots": "",
                "shoulders": "",
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
               "\nStatus Resistances: {5} " \
               "\nStrength: {6} " \
               "\nVitality: {7} " \
               "\nMagic: {8} " \
               "\nSpirit: {9} " \
               "\nSkill: {10} " \
               "\nSpeed: {11} " \
               "\nEvasion: {12} " \
               "\nMagical Evasion: {13} " \
               "\nAccuracy: {14} " \
               "\nLuck: {15} ".format(self.display_name, self.level, self.hp,
                                      self.mp, self.equipment, self.status_resistances,
                                      self.strength, self.vitality, self.magic, self.spirit, self.skill,
                                      self.speed, self.evasion, self.mg_evasion, self.accuracy, self.luck
                                      )
    __repr__ = __str__
