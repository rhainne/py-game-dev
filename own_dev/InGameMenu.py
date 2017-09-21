from pygame_custom_functions import *
from Regions import *


class InGameMenu:
    def __init__(self, screen, location, team):
        self.screen = screen
        self.location = location
        self.team = team

        self.saving_available = Regions_data[self.location]["saving_available"]

        self.button_items = pygame.Rect(10, 10, 50, 50)
        self.button_equipment = pygame.Rect(10, 110, 50, 50)
        self.button_stats = pygame.Rect(10, 210, 50, 50)
        self.button_config = pygame.Rect(10, 310, 50, 50)
        self.button_skills = pygame.Rect(10, 410, 50, 50)

        self.buttons = [self.button_items,
                        self.button_equipment,
                        self.button_stats,
                        self.button_config,
                        self.button_skills]
        self.inflated_buttons = [0, 0, 0, 0, 0]
        self.buttons_to_inflate_init = [0, 0, 0, 0, 0]
        self.buttons_to_inflate = self.buttons_to_inflate_init

    def open_menu(self):
        print("InGameMenu is active")
        is_active = True
        while is_active:
            background = pygame.Surface(self.screen.get_size())
            background = background.convert()
            background.fill((0, 0, 0))

            self.screen.blit(background, (0, 0))
            self.blit_options()
            self.button_inflator()

            pygame.display.update()

            for event in pygame.event.get():
                event_handler(event)

                if event.type == KEYUP:
                    if event.key == K_p:
                        is_active = False

                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = pygame.mouse.get_pos()
                    for idx, button in enumerate(self.buttons):
                        if button.collidepoint(mouse_pos):
                            self.buttons_to_inflate[idx] = 1
                        else:
                            self.buttons_to_inflate[idx] = 0

                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.button_items.collidepoint(mouse_pos):
                        print("self.button_items clicked")
                    elif self.button_equipment.collidepoint(mouse_pos):
                        print("self.button_equipment clicked")
                    elif self.button_stats.collidepoint(mouse_pos):
                        print("self.button_stats clicked")
                    elif self.button_skills.collidepoint(mouse_pos):
                        print("self.button_skills clicked")
                    elif self.button_config.collidepoint(mouse_pos):
                        print("self.button_config clicked")

    def blit_options(self):

        # if self.saving_available:

        # for character in self.team:
            # print("Blit character: {0}".format(character))

        pygame.draw.rect(self.screen, [255, 0, 0], self.button_items)
        pygame.draw.rect(self.screen, [255, 255, 0], self.button_equipment)
        pygame.draw.rect(self.screen, [0, 255, 0], self.button_skills)
        pygame.draw.rect(self.screen, [0, 0, 255], self.button_config)
        pygame.draw.rect(self.screen, [255, 0, 255], self.button_stats)

    def button_inflator(self):
        for idx, button in enumerate(self.buttons):
            if self.buttons_to_inflate[idx] == 1:
                if self.inflated_buttons[idx] == 0:
                    self.buttons[idx].inflate_ip(10, 10)
                    self.inflated_buttons[idx] = 1
            else:
                if self.inflated_buttons[idx] == 1:
                    self.buttons[idx].inflate_ip(-10, -10)
                    self.inflated_buttons[idx] = 0
