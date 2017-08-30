import pygame


class Item(object):
    def __init__(self, x, y, name, display_name, value, weight, quantity=1, img=None, sound=None):
        self.name = name
        self.display_name = display_name
        self.raw = name.strip().lower()
        self.quantity = quantity
        self.value = value
        self.net_value = quantity * value
        self.weight = weight

        self.img = img
        self.load_img(self.img)
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.sound = sound
        self.load_sound(self.sound)

        self.wearable = False

    def recalc(self):
        self.net_value = self.quantity * self.value

    def load_img(self, img):
        if img is not None:
            self.img = pygame.image.load(img).convert_alpha()

    def load_sound(self, sound):
        if sound is not None:
            self.sound = pygame.mixer.Sound(sound)

    def play_sound(self):
        if self.sound is not None:
            self.sound.play()

    def pick_up(self):
        self.play_sound()


class Container(object):
    def __init__(self, name, max_capacity, img, gold=0):
        self.name = name
        self.inside = {}
        self.max_capacity = max_capacity
        self.img = img
        self.gold = gold

    def __iter__(self):
        return iter(self.inside.items())

    def __len__(self):
        return len(self.inside)

    def __contains__(self, item):
        return item.raw in self.inside

    def __getitem__(self, item):
        return self.inside[item.raw]

    def __setitem__(self, item, value):
        self.inside[item.raw] = value
        return self[item]

    def add(self, item, quantity=1):
        if quantity < 0:
            raise ValueError("Negative quantity. Use Inventory.remove() instead.")

        if self.max_capacity > self.__len__():
            if item in self:
                self[item].quantity += quantity
                self[item].recalc()
                return True
            else:
                self[item] = item
        else:
            print("Too much burden. You cannot wear anything more")
        return False

    def remove(self, item, quantity=1):
        if item not in self:
            raise KeyError("Item not present in Container.")
        if quantity < 0:
            raise ValueError("Negative quantity. Use Inventory.add() instead.")

        if self[item].quantity <= quantity:
            del self.inside[item.raw]
        else:
            self[item].quantity -= quantity
            self[item].recalc()
