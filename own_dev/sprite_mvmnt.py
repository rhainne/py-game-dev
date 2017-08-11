import sys
import copy
sys.path.insert(0, 'C:/Users/Vanadys3/Git/py-game-dev/')
sys.path.insert(0, '/home/rain/Git/py-game-dev/')
sys.path.insert(0, 'C:/Users/rain_/PycharmProjects/py-game-dev')
from own_dev.Character import *
from own_dev.Inventory import *
from own_dev.MapCollection import *
from own_dev.Map import *

l_width, l_height = 1024, 720
# l_width, l_height = 1000, 30
SPEED_WALK = 200
SPEED_RUN = 400

background_image_filename = '../assets/chess1280x800.png'

pygame.init()
screen = pygame.display.set_mode((l_width, l_height), 0, 32)

clock = pygame.time.Clock()
elapsed = 0.

background = pygame.image.load(background_image_filename).convert()

blue_coin_name = "Rupieta azul"
coin_img = "../assets/knight_sprite/6-25x100/Dead_10.png"
coin_sound = "../assets/sound/coin_pick_up.wav"

list_of_items = [
    Item(0, 500, blue_coin_name, 5, 1, coin_img, coin_sound),
    Item(0, 600, blue_coin_name, 5, 1, coin_img, coin_sound),
    Item(0, 700, blue_coin_name, 5, 1, coin_img, coin_sound),
    Item(0, 800, blue_coin_name, 5, 1, coin_img, coin_sound),
    Item(0, 400, blue_coin_name, 5, 1, coin_img, coin_sound)
]

list_of_rects = [
    Rect(0, 400, 100, 100),
    Rect(0, 500, 100, 100),
    Rect(0, 600, 100, 100),
    Rect(0, 700, 100, 100),
    Rect(0, 800, 100, 100)
]

list_of_maps = [
        Map("rohan", "../assets/maps/rohan_map.jpg", "simon"),
        Map("middle_earth", "../assets/maps/middle_earth_map.jpg", "simon"),
        Map("simon"
            , "../assets/maps/map_2x2.png"
            , None
            , ["rohan", "middle_earth"]
            , [
                [(0, 0), (206.5, 409)]
                , [(206.5, 0), (413, 409)]
            ])
]

knight_1 = Character(list_of_rects)
knight_1.container = Container("Basic Backpack", 10)
map_collection = MapCollection("simon", list_of_maps)
blit_map = None
heading = 0

maps = list((filter(lambda i_map: i_map.name == "simon", map_collection.map_collection)))
print(maps[0])

while True:
    seconds = elapsed / 1000.0
    for event in pygame.event.get():
        event_handler(event)

        pressed_keys = pygame.key.get_pressed()
        pressed_mods = pygame.key.get_mods()

        if pressed_keys[K_RIGHT]:
            if pressed_mods == 64:  # 64 == Left Control Key
                knight_1.state = "RUN"
                heading = SPEED_RUN
            else:
                knight_1.state = "WALK"
                heading = SPEED_WALK
        if pressed_keys[K_LEFT]:
            if pressed_mods == 64:  # 64 == Left Control Key
                knight_1.state = "RUN"
                heading = -SPEED_RUN
            else:
                knight_1.state = "WALK"
                heading = -SPEED_WALK

        if event.type == KEYUP:
            if event.key == K_RIGHT:
                knight_1.state = "IDLE"
                heading = 0
            if event.key == K_LEFT:
                knight_1.state = "IDLE"
                heading = 0
            if event.key == K_m:
                if blit_map is None:
                    pygame.mouse.set_visible(True)
                    blit_map = map_collection.show_map(l_width, l_height)
                else:
                    pygame.mouse.set_visible(False)
                    blit_map = None

        if event.type == pygame.MOUSEBUTTONUP:
            blit_map = map_collection.switch_map(l_width, l_height, event)

    if knight_1.x > l_width:
        knight_1.x = -147

    '''
    check_collide = knight_1.img_rect.collidelist(list_of_rects)
    if check_collide != -1:
        print("Do you want to pick {0}? Y/N".format(list_of_rects[check_collide]))
        if input() == "Y":
            del list_of_rects[check_collide]
            list_of_items[check_collide].play_sound()
            knight_1.container.add(list_of_items[check_collide])
            del list_of_items[check_collide]
    '''

    screen.blit(background, (0, 0))
    knight_1.update(heading, screen, seconds)
    if blit_map is not None:
        screen.blit(blit_map[0], blit_map[1])
    elapsed = clock.tick(60)
    pygame.display.update()
