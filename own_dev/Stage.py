import glob


class Stage(object):
    def __init__(self, background_img, sprite_list=None, colliding_elements=None):
        self.background_img = background_img
        if sprite_list is None:
            sprite_list = []
        # self.sprite_list = glob.glob(sprite_list)
        if colliding_elements is None:
            colliding_elements = []
        self.colliding_elements = colliding_elements
