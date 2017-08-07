import glob
from own_dev.Inventory import *
from various_functions.pygame_custom_functions import *


class Character:
    def __init__(self, stage_colliders=None):
        self.container = Container("")
        self.init_state = "IDLE"
        self.state = self.init_state
        self.x = 5
        self.y = 5
        self.stage_colliders = stage_colliders

        # Idle animation
        self.ani_idle_speed_init = 4
        self.ani_idle_speed = self.ani_idle_speed_init
        self.ani_idle_sprite_list = glob.glob("../assets/knight_sprite/25x100/Idle*.png")
        self.ani_idle_sprite_list.sort()  # Order the frames
        self.idle_ani = load_sprite_list(self.ani_idle_sprite_list)
        self.idle_ani_pos = 0
        self.idle_ani_max = len(self.idle_ani) - 1

        # Walk animation
        self.ani_walk_speed_init = 4
        self.ani_walk_speed = self.ani_walk_speed_init
        self.ani_walk_sprite_list = glob.glob("../assets/knight_sprite/25x100/Walk*.png")
        self.ani_walk_sprite_list.sort()  # Order the frames
        self.walk_ani = load_sprite_list(self.ani_walk_sprite_list)
        self.walk_ani_pos = 0
        self.walk_ani_max = len(self.walk_ani) - 1

        # Run animation
        self.ani_run_speed_init = 4
        self.ani_run_speed = self.ani_run_speed_init
        self.ani_run_sprite_list = glob.glob("../assets/knight_sprite/25x100/Run*.png")
        self.ani_run_sprite_list.sort()  # Order the frames
        self.run_ani = load_sprite_list(self.ani_run_sprite_list)
        self.run_ani_pos = 0
        self.run_ani_max = len(self.run_ani) - 1

        self.img = self.idle_ani[0]
        self.img_rect = self.img.get_rect()
        self.update(0, pygame.display.set_mode((0, 0), 0, 32), self.init_state)

    def update(self, heading, screen, delta, state=""):
        print("State: {0}".format(state))
        if state == "":
            state = self.state
        if state == "IDLE":
            self.ani_idle_speed -= 1
            if self.ani_idle_speed == 0:
                self.img = self.idle_ani[self.idle_ani_pos]
                self.ani_idle_speed = self.ani_idle_speed_init
                if self.idle_ani_pos == self.idle_ani_max:
                    self.idle_ani_pos = 0
                else:
                    self.idle_ani_pos += 1
        if state == 'WALK':
            if heading != 0:
                self.ani_walk_speed -= 1
                # self.x += heading * delta
                self.move(heading * delta, 0)
                if self.ani_walk_speed == 0:
                    self.img = self.walk_ani[self.walk_ani_pos]
                    self.ani_walk_speed = self.ani_walk_speed_init
                    if self.walk_ani_pos == self.walk_ani_max:
                        self.walk_ani_pos = 0
                    else:
                        self.walk_ani_pos += 1
        if state == "RUN":
            if heading != 0:
                self.ani_run_speed -= 1
                # self.x += heading * delta
                self.move(heading * delta, 0)
                if self.ani_run_speed == 0:
                    self.img = self.run_ani[self.run_ani_pos]
                    self.ani_run_speed = self.ani_run_speed_init
                    if self.run_ani_pos == self.run_ani_max:
                        self.run_ani_pos = 0
                    else:
                        self.run_ani_pos += 1

        # if state == 'DEATH':
        self.update_img_rect()
        screen.blit(self.img, (self.x, self.y))

    def update_img_rect(self):
        self.img_rect = self.img.get_rect()
        self.img_rect.top = self.x
        self.img_rect.left = self.y

    def move(self, dx, dy):
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):
        print("x: {0}, y = {1}".format(self.x, self.y))
        # Move the rect
        self.x += dx
        self.y += dy

        # If you collide with a collider, move out based on velocity
        for collider in self.stage_colliders:
            if self.img_rect.colliderect(collider):
                if dx > 0:  # Moving right; Hit the left side of the collider
                    self.img_rect.right = collider.left
                if dx < 0:  # Moving left; Hit the right side of the collider
                    self.img_rect.left = collider.right
                if dy > 0:  # Moving down; Hit the top side of the collider
                    self.img_rect.bottom = collider.top
                if dy < 0:  # Moving up; Hit the bottom side of the collider
                    self.img_rect.top = collider.bottom

    def purchase(self, *items):
        for item in items:
            if item.value > self.container.gold:
                print("You don't have enough money.")
                print("Come back when you have {0} more gold.".format(item.value - self.container.gold))
            else:
                self.container.gold -= item.value
                self.container.add(item)
                print("{0} purchased".format(item.name))

    def sell(self, item):
        if item in self.container:
            self.container.gold += item.value
            print("{0} sold. {1} earned.".format(item.name, item.value))
        else:
            print("You cannot sell an item you don't have.")
