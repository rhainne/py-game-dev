from own_dev.Stage import *


class Battleground(Stage):
    def __init__(self, location):
        Stage.__init__(self, "../assets/backgrounds/shop_1.jpg")
        self.location = location

