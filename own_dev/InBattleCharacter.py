from MDInventory import *


class InBattleCharacter:
    def __init__(self, **kwargs):
        attributes = {
            "team_allies": [],
            "name": "",
            "display_name": "",
            "image": "",
            "type": "",
            "level": 1,
            "hp": 100,
            "mp": 50,
            "strength": 1,
            "vitality": 1,
            "magic": 1,
            "spirit": 1,
            "skill": 0,
            "speed": 10,
            "evasion": 1,
            "mg_evasion": 1,
            "accuracy": 5,
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
                "accessory_1": "",
                "accessory_2": "",
                "necklace": ""
            }
        }

        for (prop, default) in list(attributes.items()):
            setattr(self, prop, kwargs.get(prop, default))

        self.recalc_equipment_bonus()
        self.recalc_level_bonus()
        print(self)

    def recalc_equipment_bonus(self):
        for key, value in self.equipment.items():
            if value != "":
                self.recalc_item_bonus(value)

    def recalc_item_bonus(self, item):
        wearable_item_data = Wearable_item_Data[item]

        self.hp += wearable_item_data["hp_mod"]
        self.mp += wearable_item_data["mp_mod"]
        self.strength += wearable_item_data["strength_mod"]
        self.vitality += wearable_item_data["vitality_mod"]
        self.magic += wearable_item_data["magic_mod"]
        self.spirit += wearable_item_data["spirit_mod"]
        self.skill += wearable_item_data["skill_mod"]
        self.speed += wearable_item_data["speed_mod"]
        self.evasion += wearable_item_data["evasion_mod"]
        self.mg_evasion += wearable_item_data["mg_evasion_mod"]
        self.accuracy += wearable_item_data["accuracy_mod"]
        self.luck += wearable_item_data["luck_mod"]

    def recalc_level_bonus(self):
        bonus = self.level / 25 + 1

        self.hp = (self.hp + self.level * 5) * bonus
        self.mp = (self.mp + self.level * 2) * bonus
        self.strength = (self.strength + self.level) * bonus
        self.vitality = (self.vitality + self.level) * bonus
        self.magic = (self.magic + self.level) * bonus
        self.spirit = (self.spirit + self.level) * bonus
        self.skill = (self.skill + self.level / 2) * bonus
        self.speed = (self.speed + self.level / 4) * bonus
        self.evasion = (self.evasion + self.level / 6) * bonus
        self.mg_evasion = (self.mg_evasion + self.level / 6) * bonus
        self.accuracy = (self.accuracy + self.level / 6) * bonus

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
