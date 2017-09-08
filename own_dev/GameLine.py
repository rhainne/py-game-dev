import sys
sys.path.insert(0, 'C:/Users/Vanadys3/Git/py-game-dev/')
sys.path.insert(0, '/home/rain/Git/py-game-dev/')
sys.path.insert(0, 'C:/Users/rain_/PycharmProjects/py-game-dev')
from own_dev.MapCollection import *
from own_dev.InBattleCharacter import *
pygame.init()


class GameLine:
    def __init__(self, screen, character, map_collection, bg_image):
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height

        self.character = character
        # Could be and ussually will be more than one InBattleCharacters
        self.in_battle_characters = [InBattleCharacter(name="rain", display_name="Rain", level=40)]

        self.bg_image = bg_image
        self.bg_surface = pygame.image.load(self.bg_image).convert()
        self.clock = pygame.time.Clock()
        self.elapsed = 0.

        self.speed_walk = 300
        self.diagonal_modifier = 0.707

        self.maps = map_collection
        self.map_collection = MapCollection("simon", self.maps)
        self.blit_map = None
        self.map_deployed = False

    def run(self):
        heading = 0
        up_down = 0
        while True:
            seconds = self.elapsed / 1000.0
            for event in pygame.event.get():
                event_handler(event)

                pressed_keys = pygame.key.get_pressed()

                if pressed_keys[K_RIGHT]:
                    self.character.state = "WALK"
                    if pressed_keys[K_UP]:
                        heading = self.speed_walk * self.diagonal_modifier
                        up_down = -self.speed_walk * self.diagonal_modifier
                    elif pressed_keys[K_DOWN]:
                        heading = self.speed_walk * self.diagonal_modifier
                        up_down = self.speed_walk * self.diagonal_modifier
                    else:
                        heading = self.speed_walk
                        up_down = 0

                if pressed_keys[K_LEFT]:
                    self.character.state = "WALK"
                    if pressed_keys[K_UP]:
                        heading = -self.speed_walk * self.diagonal_modifier
                        up_down = -self.speed_walk * self.diagonal_modifier
                    elif pressed_keys[K_DOWN]:
                        heading = -self.speed_walk * self.diagonal_modifier
                        up_down = self.speed_walk * self.diagonal_modifier
                    else:
                        heading = -self.speed_walk
                        up_down = 0

                if pressed_keys[K_UP] and not (pressed_keys[K_RIGHT] or pressed_keys[K_LEFT]):
                    self.character.state = "WALK"
                    heading = 0
                    up_down = -self.speed_walk
                if pressed_keys[K_DOWN] and not (pressed_keys[K_RIGHT] or pressed_keys[K_LEFT]):
                    self.character.state = "WALK"
                    heading = 0
                    up_down = self.speed_walk

                if not any(pressed_keys):
                    self.character.state = "IDLE"
                    heading = 0
                    up_down = 0

                if event.type == KEYUP:
                    if event.key == K_m:
                        if self.blit_map is None:
                            self.map_deployed = True
                            pygame.mouse.set_visible(True)
                            self.blit_map = self.map_collection.show_map(self.scr_width, self.scr_height)
                        else:
                            self.map_deployed = False
                            pygame.mouse.set_visible(False)
                            self.blit_map = None

                    if event.key == K_p:
                        self.character.in_game_menu.open_menu()

                if event.type == pygame.MOUSEBUTTONUP:
                    if self.map_deployed:
                        self.blit_map = self.map_collection.switch_map(self.scr_width, self.scr_height, event)

            if self.character.x > self.scr_width:
                self.character.x = -147

            self.screen.blit(self.bg_surface, (0, 0))
            self.character.update(heading, up_down, self.screen, seconds)
            if self.blit_map is not None:
                self.screen.blit(self.blit_map[0], self.blit_map[1])
            self.elapsed = self.clock.tick(60)
            pygame.display.update()
