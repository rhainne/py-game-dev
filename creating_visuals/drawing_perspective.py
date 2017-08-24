from own_dev.pygame_custom_functions import *

pygame.init()

l_width, l_height = 1280, 800
perspective_field_modifier = 100
line_width = 10
screen = pygame.display.set_mode((l_width, l_height), 0, 32)

while True:
    for event in pygame.event.get():
        event_handler(event)

    screen.fill((0, 0, 0))

    mouse_pos = pygame.mouse.get_pos()
    square_points = [[(mouse_pos[0] - perspective_field_modifier), (mouse_pos[1] - perspective_field_modifier)],  # bottom left
                     [(mouse_pos[0] + perspective_field_modifier), (mouse_pos[1] - perspective_field_modifier)],  # bottom right
                     [(mouse_pos[0] + perspective_field_modifier), (mouse_pos[1] + perspective_field_modifier)],  # top right
                     [(mouse_pos[0] - perspective_field_modifier), (mouse_pos[1] + perspective_field_modifier)],  # top left
                     [(mouse_pos[0] - perspective_field_modifier), (mouse_pos[1] - perspective_field_modifier)]]  # bottom left

    pygame.draw.line(screen, (255, 255, 255), (0, 0), square_points[0], line_width)  # bottom left
    pygame.draw.line(screen, (255, 255, 255), (0, (l_height - 1)), square_points[3], line_width)  # top left
    pygame.draw.line(screen, (255, 255, 255), ((l_width - 1), 0), square_points[1], line_width)  # top right
    pygame.draw.line(screen, (255, 255, 255), ((l_width - 1), (l_height - 1)), square_points[2], line_width)  # bottom right

    pygame.draw.lines(screen, (255, 255, 255), False, square_points, line_width)

    pygame.display.update()
