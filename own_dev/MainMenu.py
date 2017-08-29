#!/usr/bin/python
import sys
sys.path.insert(0, 'C:/Users/Vanadys3/Git/py-game-dev/')
from own_dev.GameLine import *
from own_dev.Character import *
from own_dev.GlobeMaps import *
from own_dev.Inventory import Container

pygame.init()


class GameMenu:
    def __init__(self, screen, items, bg_color=(0, 0, 0), font=None, font_size=30,
                 font_color=(255, 255, 255)):
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height

        self.bg_color = bg_color
        self.clock = pygame.time.Clock()

        self.items = items
        self.font = pygame.font.SysFont(font, font_size)
        self.font_color = font_color

        self.items = []
        self.item_rects = []
        self.on_quit_options = []
        self.on_quit_option_rects = []

        self.set_items(items, font_color)

    def set_items(self, items, font_color):
        for index, item in enumerate(items):
            label = self.font.render(item, 1, font_color)

            width = label.get_rect().width
            height = label.get_rect().height

            posx = (self.scr_width / 2) - (width / 2)
            # t_h: total height of text block
            t_h = len(items) * height
            posy = (self.scr_height / 2) - (t_h / 2) + (index * height)

            self.items.append([item, label, (width, height), (posx, posy)])
            self.item_rects.append(label.get_rect(topleft=(posx, posy)))

    def run(self):
        running = True
        while running:
            # Limit frame speed to 50 FPS
            self.clock.tick(50)

            for event in pygame.event.get():
                event_handler(event)

                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.item_rects[0].collidepoint(mouse_pos):
                        self.start_new_game()
                    if self.item_rects[1].collidepoint(mouse_pos):
                        print("Load Game pressed")
                    if self.item_rects[2].collidepoint(mouse_pos):
                        print("Options pressed")
                    if self.item_rects[3].collidepoint(mouse_pos):
                        print("Exit pressed")
                        self.raise_warning_on_exit()

            # Redraw the background
            self.screen.fill(self.bg_color)

            for name, label, (width, height), (posx, posy) in self.items:
                self.screen.blit(label, (posx, posy))

            pygame.display.update()

    def raise_warning_on_exit(self):
        options = ["Quit Game", "Cancel"]
        for index, item in enumerate(options):
            # Quit Game Button
            label_quit = self.font.render("Quit Game", 1, self.font_color)

            width_quit = label_quit.get_rect().width
            height_quit = label_quit.get_rect().height

            posx_quit = (self.scr_width / 2) - (width_quit / 2) - 100
            posy_quit = (self.scr_height / 5) * 3 - (height_quit / 2)

            self.on_quit_options.append([item, label_quit, (width_quit, height_quit), (posx_quit, posy_quit)])
            self.on_quit_option_rects.append(label_quit.get_rect(topleft=(posx_quit, posy_quit)))

            # Cancel Button
            label_cancel = self.font.render("Cancel", 1, self.font_color)

            width_cancel = label_cancel.get_rect().width
            height_cancel = label_cancel.get_rect().height

            posx_cancel = (self.scr_width / 2) - (width_cancel / 2) + 100
            posy_cancel = (self.scr_height / 5) * 3 - (height_cancel / 2)

            self.on_quit_options.append([item, label_cancel, (width_cancel, height_cancel), (posx_cancel, posy_cancel)])
            self.on_quit_option_rects.append(label_cancel.get_rect(topleft=(posx_cancel, posy_cancel)))

        running = True
        while running:
            self.clock.tick(50)
            for event in pygame.event.get():
                event_handler(event)

                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.on_quit_option_rects[0].collidepoint(mouse_pos):
                        pygame.quit()
                        exit()
                    if self.on_quit_option_rects[1].collidepoint(mouse_pos):
                        running = False

            self.screen.fill(self.bg_color)
            for name, label, (width, height), (posx, posy) in self.on_quit_options:
                self.screen.blit(label, (posx, posy))

            pygame.display.update()

    def start_new_game(self):
        container = Container("Standard Bag", 0)
        character = Character(self.screen, "durna", container, [])
        map_collection = [Map_constructors["rohan"]
                          , Map_constructors["middle_earth"]
                          , Map_constructors["simon"]
                          ]
        # self, screen, character, container, map_collection, bg_image
        bg_image = "../assets/chess1280x800.png"
        gl = GameLine(self.screen, character, map_collection, bg_image)
        gl.run()


if __name__ == "__main__":
    # Creating the screen
    screen = pygame.display.set_mode((1042, 600), 0, 32)

    menu_items = ('Start Game', 'Load Game', 'Options', 'Quit')

    pygame.display.set_caption('Game Menu')
    gm = GameMenu(screen, menu_items)
    gm.run()
