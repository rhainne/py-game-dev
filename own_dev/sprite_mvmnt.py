import sys
import glob
sys.path.insert(0, 'C:/Users/Vanadys3/Git/py-game-dev/')
from various_functions.pygame_custom_functions import *
from various_functions.vector2 import Vector2

l_width, l_height = 1024, 720
background_image_filename = '../assets/chess1280x800.png'
knight_imgs = ['../assets/knight_sprite/Attack_1.png'
                 , '../assets/knight_sprite/Dead_10.png'
                 , '../assets/knight_sprite/JumpAttack_5.png'
                 , '../assets/knight_sprite/Walk_10.png']

def animate_sprite(heading, i_sprite):
    switcher = {
        'left': i_sprite[0],
        'right': i_sprite[1],
        'up': i_sprite[2],
        'down': i_sprite[3]
    }
    o_sprite = switcher.get(heading)
    return o_sprite

pygame.init()
screen = pygame.display.set_mode((l_width, l_height), 0, 32)


class knight:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.ani_speed_init = 5
        self.ani_speed = self.ani_speed_init
        self.walk_ani = glob.glob('../assets/knight_sprite/W*.png')
        self.walk_ani.sort()  # Order the frames
        self.walk_ani_pos = 0
        self.walk_ani_max = len(self.walk_ani) - 1
        self.img = pygame.image.load(self.walk_ani[0])
        self.update(0)

    def update(self, heading):
        if heading != 0:
            self.ani_speed -= 1
            self.x += heading
            if self.ani_speed == 0:
                self.img = pygame.image.load(self.walk_ani[self.walk_ani_pos])
                self.ani_speed = self.ani_speed_init
                if self.walk_ani_pos == self.walk_ani_max:
                    self.walk_ani_pos = 0
                else:
                    self.walk_ani_pos += 1
        screen.blit(self.img, (self.x, self.y))

background = pygame.image.load(background_image_filename).convert()
knight_sprites = load_sprite_list(knight_imgs)
sprite = knight_sprites[0]
clock = pygame.time.Clock()
sprite_pos = Vector2(200, 150)
sprite_speed = 250

# Directional normalized vectors
direction_up = Vector2(0, -1)  # UP
direction_up_right = Vector2(0.707, -0.707)
direction_right = Vector2(1, 0)
direction_down_right = Vector2(0.707, 0.707)
direction_down = Vector2(0, 1)
direction_down_left = Vector2(-0.707, 0.707)
direction_left = Vector2(-1, 0)
direction_up_left = Vector2(-0.707, -0.707)

char_1 = knight()
heading = 0

while True:
    for event in pygame.event.get():
        event_handler(event)
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                heading = 1
            if event.key == K_LEFT:
                heading = -1

        elif event.type == KEYUP:
            if event.key == K_RIGHT:
                heading = 0
            if event.key == K_LEFT:
                heading = 0

    '''
    # Diagonals
    if pressed_keys[K_UP] and pressed_keys[K_LEFT]:
        key_direction = direction_up_left  # UP + LEFT
    if pressed_keys[K_UP] and pressed_keys[K_RIGHT]:
        key_direction = direction_up_right  # UP + RIGHT
    if pressed_keys[K_DOWN] and pressed_keys[K_LEFT]:
        key_direction = direction_down_left  # DOWN + LEFT
    if pressed_keys[K_DOWN] and pressed_keys[K_RIGHT]:
        key_direction = direction_down_right  # DOWN + RIGHT
    '''

    screen.blit(background, (0, 0))
    char_1.update(heading)
    time_passed = clock.tick(50)
    time_passed_seconds = time_passed / 1000.0

    # sprite_pos += key_direction * sprite_speed * time_passed_seconds

    pygame.display.update()
