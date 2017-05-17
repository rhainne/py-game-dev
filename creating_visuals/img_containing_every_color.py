import pygame

pygame.init()
SCREEN_SIZE = (1280, 768)
screen = pygame.display.set_mode(SCREEN_SIZE)

all_colors = pygame.Surface((4096, 4096), depth=24)

for r in range(256):
    print(r + 1, "out of 256")
    x = (r & 15) * 256
    y = (r >> 4) * 256
    for g in range(256):
        for b in range(256):
            all_colors.set_at((x + g, y + b), (r, g, b))

pygame.image.save(all_colors, "../assets/allcolors.bmp")
pygame.quit()
