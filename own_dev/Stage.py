import glob


class Stage(object):
    def __init__(self, background, sprite_list=None, colliding_elements=None):
        self.background = background
        if sprite_list is None:
            sprite_list = []
        self.sprite_list = glob.glob(sprite_list)
        if colliding_elements is None:
            colliding_elements = []
        self.colliding_elements = colliding_elements
