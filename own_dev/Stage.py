import glob


class Stage(object):
    def __init__(self, background, sprite_list):
        self.background = background
        self.sprite_list = glob.glob(sprite_list)
        self.colliding_elements = []
