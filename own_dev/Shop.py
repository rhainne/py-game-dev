from own_dev.Stage import *


class Shop(Stage):
    def __init__(self, trader_list):
        Stage.__init__(self, "../assets/backgrounds/shop_1.jpg")
        self.traders = trader_list
