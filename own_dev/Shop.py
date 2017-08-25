from own_dev.Character import *
from own_dev.NPC import *


class Shop:
    def __init__(self, screen, character, npc):
        self.items_to_sell = [NPCs_data][npc]["items_to_sell"]
        self.items_to_buy = [NPCs_data][npc]["items_to_buy"]
        self.greetings = [NPCs_data][npc]["greetings"]
        self.farewells = [NPCs_data][npc]["farewells"]
        self.not_enough_money = [NPCs_data][npc]["not_enough_money"]
        self.character = character

    def start_buying(self):
        # if self.items_to_sell:  # checks for emptiness
           # Desplegar los items que tiene en venta ETC
        # if self.items_to_buy:
           # Desplegar los items que esta dispuesto a comprar
        return None

    def not_enough_money(self):
        npc_sentence = random.choice(self.not_enough_money)
