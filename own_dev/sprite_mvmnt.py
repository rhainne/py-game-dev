import sys
sys.path.insert(0, 'C:/Users/Vanadys3/Git/py-game-dev/')
sys.path.insert(0, '/home/rain/Git/py-game-dev/')
sys.path.insert(0, 'C:/Users/rain_/PycharmProjects/py-game-dev')
from own_dev.Character import *
from own_dev.Inventory import *

l_width, l_height = 1024, 720
SPEED_WALK = 200
SPEED_RUN = 400

background_image_filename = '../assets/chess1280x800.png'

pygame.init()
screen = pygame.display.set_mode((l_width, l_height), 0, 32)

clock = pygame.time.Clock()
elapsed = 0.

background = pygame.image.load(background_image_filename).convert()

knight_1 = Character()
knights_bag = Container("Basic Backpack", 10)
heading = 0

rect1 = Rect(0, 0, 50, 50)
rect2 = Rect(50, 50, 50, 50)
print("Does rect1 collides with rect2? ".format(rect1.colliderect(rect2)))


bronze_sword = Item("Bronze Sword ", 10)
potion = Item("Potion", 5)

knights_bag.add(bronze_sword)
knights_bag.add(bronze_sword)
knights_bag.add(potion)

print("Current Gold quantity: {0}".format(knights_bag.gold))
print(len(knights_bag))
for name, item in knights_bag:
    print(name, item.quantity)
knight_1.purchase(bronze_sword)
knight_1.purchase(bronze_sword)
print("Current Gold quantity: {0}".format(knights_bag.gold))

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

    if knight_1.x > l_width:
        knight_1.x = -147
    screen.blit(background, (0, 0))
    knight_1.update(heading, screen, seconds)
    elapsed = clock.tick(60)
    pygame.display.update()
