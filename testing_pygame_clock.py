from various_functions.pygame_custom_functions import *

clock = pygame.time.Clock()

while True:
    time_passed = clock.tick(60)
    time_passed_seconds = time_passed / float(1000.0)
    print(str(time_passed) + ' - ' + str(time_passed_seconds))
