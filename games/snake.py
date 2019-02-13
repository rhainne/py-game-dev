import pygame
import random

s_width = 1100
s_height = 700
play_width = 900 # 900/10 = 90
play_height = 600 # 600/10 = 60
block_size = 10
mouses = []
big_mouses = []
top_left_x = (s_width - play_width)/2
top_left_y = (s_height - play_height)/2
top_right_x = s_width - top_left_x
bottom_left_y = s_height - top_left_y
mouse_coords = (top_left_x // block_size, 
                top_right_x // block_size, 
                top_left_y // block_size, 
                bottom_left_y // block_size)

class Snake():
    def __init__(self, head_x, head_y, body_size):
        self.head_x = head_x
        self.head_y = head_y
        self.body_size = body_size
        self.movement = 0
        self.speed = 0.07
        self.positions = []
        for x in range(20):
            self.positions.append((head_x - (x * self.body_size), 
                                   head_y))

    def draw_snake(self, surface):
        for pos in self.positions:
            pygame.draw.rect(surface, 
                            (20,100,0), 
                            (pos[0], pos[1], self.body_size, self.body_size), 
                            0)

    def move_snake(self, direction=0):
        # TODO Sigue habien un bug cuando giras muy rapidamente 180º
        # Serpiento muere aunque no debería.
        def make_body_follow_head():
            for i in reversed(range(len(self.positions[1:]))):
                self.positions[i+1] = self.positions[i]

        if direction == 0: # right
            make_body_follow_head()
            if self.head_x >= top_right_x - self.body_size:
               self.positions[0] = (top_left_x, self.positions[0][1]) 
            else:
                next_position = (self.positions[0][0] + self.body_size, 
                                 self.positions[0][1])
                self.positions[0] = next_position
        if direction == 1: # down
            make_body_follow_head()
            if self.head_y >= bottom_left_y - self.body_size:
                self.positions[0] = (self.positions[0][0], top_left_y) 
            else:
                next_position = (self.positions[0][0], 
                                 self.positions[0][1] + self.body_size)
                self.positions[0] = next_position

        if direction == 2: # left
            make_body_follow_head()
            if self.head_x <= top_left_x:
                self.positions[0] = (top_right_x - self.body_size, 
                                     self.positions[0][1]) 
            else:
                next_position = (self.positions[0][0] - self.body_size, 
                                 self.positions[0][1])
                self.positions[0] = next_position

        if direction == 3: # up
            make_body_follow_head()
            if self.head_y <= top_left_y:
                self.positions[0] = (self.positions[0][0], 
                                     bottom_left_y - self.body_size) 
            else:
                next_position = (self.positions[0][0], 
                                 self.positions[0][1] - self.body_size)
                self.positions[0] = next_position

        self.head_x = self.positions[0][0]
        self.head_y = self.positions[0][1]

    def eat_mouse(self, score):
        for mouse in mouses:
            if mouse == (self.head_x, self.head_y):
                self.positions.append((0, 0))
                mouses.remove(mouse)
                score += 10
                if len(mouses) < 7:
                    mouse_spawn(mouse_coords)

        for bigmouse in big_mouses:
            for bodypart in bigmouse[0]:
                if bodypart == (self.head_x, self.head_y):
                    big_mouses.remove(bigmouse)
                    score += 50

        return score



def check_lost(snake):
    for pos in snake.positions[1:]:
        x, y = pos
        if x == snake.head_x and y == snake.head_y:
            return True
    return False

def mouse_spawn(mouse_coords):
    x = random.randint(mouse_coords[0], mouse_coords[1]) * block_size
    y = random.randint(mouse_coords[2], mouse_coords[3]) * block_size
    if x == top_right_x:
        x -= block_size
    if y == bottom_left_y:
        y -= block_size

    mouses.append((x,y))

def big_mouse_spawn(mouse_coords):
    # Comprobar que los ratones no se suporponen unos a otros
    x = random.randint(mouse_coords[0], mouse_coords[1]) * block_size
    y = random.randint(mouse_coords[2], mouse_coords[3]) * block_size
    if x == top_right_x or x == top_right_x - block_size:
        x -= (block_size * 2)
    if y == bottom_left_y or y == bottom_left_y - block_size:
        y -= (block_size * 2)
    
    bigmouse_body = ((x, y), 
                     (x + block_size, y), 
                     (x, y + block_size), 
                     (x + block_size, y + block_size))

    bigmouse_duration = random.randint(3, 7)
    big_mouses.append([bigmouse_body, bigmouse_duration])

def draw_mouses(surface):
    for mouse in mouses:
        pygame.draw.rect(surface, 
                        (200,50,50), 
                        (mouse[0], mouse[1], block_size, block_size), 
                        0)

    for bigmouse in big_mouses:
        for bodypart in bigmouse[0]:
            pygame.draw.rect(surface, 
                            (100,50,255), 
                            (bodypart[0], bodypart[1], block_size, block_size), 
                            0)

def draw_grid(surface):
    sx = top_left_x
    sy = top_left_y

    pygame.draw.line(surface, 
                    (128, 128, 128), 
                    (sx, sy), 
                    (sx + play_width, sy))
    pygame.draw.line(surface,
                    (128, 128, 128), 
                    (sx, sy), 
                    (sx, sy + play_height))
    pygame.draw.line(surface,
                    (128, 128, 128), 
                    (sx, sy + play_height), 
                    (sx + play_width, sy + play_height))
    pygame.draw.line(surface,
                    (128, 128, 128), 
                    (sx + play_width, sy), 
                    (sx + play_width, sy + play_height))

def draw_window(surface, score=0, last_score=0):
    surface.fill((0, 0, 0))

    font = pygame.font.SysFont('comicsans', 30)
    # Current score
    label = font.render('Score: ' + str(score), 1, (255, 255, 255))
    #surface.blit(label, (10, s_height/2 - label.get_height()/2))
    surface.blit(label, (10, 25))
    
    # Last score
    label = font.render('Max Score: ' + str(last_score), 1, (255, 255, 255))
    #surface.blit(label, (10, s_height/2 + 10))
    surface.blit(label, (10, 4))

    draw_grid(surface)
    draw_mouses(surface)

def draw_text_middle(surface, text, size, color):
    font = pygame.font.SysFont('comicsans', size, italic=True)
    label = font.render(text, 1, color)

    surface.blit(label, (s_width/2 - label.get_width()/2, 
                         s_height/2 - label.get_height()/2))

def update_score(nscore):
    score = max_score()
    
    with open('snake_scores.txt', 'w') as f:
        if int(score) > nscore:
            f.write(str(score))
        else:
            f.write(str(nscore))

def max_score():
    with open('snake_scores.txt', 'r') as f:
        lines = f.readlines()
        score = lines[0].strip()

    return score

def splash_screen(surface):
    draw_text_middle(surface, 'Snake!', 60, (200, 180, 255))
    pygame.display.update()
    pygame.time.delay(500)
    main(surface)
    pygame.display.quit()

def main(surface):
    run = True
    moved = False
    clock = pygame.time.Clock()
    snake = Snake(400, 400, block_size)
    mouse_spawn_time = 0
    mouse_spawn_speed = 4
    big_mouse_spawn_time = 0
    big_mouse_spawn_speed = random.randint(1, 15)
    big_mouse_countdown = 0
    score = 0
    current_direction = 0 # 0 = right, 1 = down, 2 = left, 3 = up

    while run:
        snake.movement += clock.get_rawtime()
        mouse_spawn_time += clock.get_rawtime()
        big_mouse_spawn_time += clock.get_rawtime()
        big_mouse_countdown += clock.get_rawtime()
        clock.tick()

        # Snake movement
        if snake.movement/1000 > snake.speed:
            snake.move_snake(current_direction)
            snake.movement = 0
            moved = True

        # Mouses
        if mouse_spawn_time/1000 > mouse_spawn_speed:
            mouse_spawn_time = 0
            mouse_spawn(mouse_coords)

        # Big mouses
        if big_mouse_spawn_time/1000 > big_mouse_spawn_speed:
            big_mouse_spawn_time = 0
            if len(big_mouses) < 2:
                big_mouse_spawn(mouse_coords)
                big_mouse_spawn_speed = random.randint(1, 15)
        if big_mouse_countdown/1000 > 1:
            big_mouse_countdown = 0
            for bigmouse in big_mouses:
                if bigmouse[1] == 0:
                    big_mouses.remove(bigmouse)
                bigmouse[1] -= 1
            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if moved:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if current_direction != 2:
                            current_direction = 0

                    if event.key == pygame.K_DOWN:
                        if current_direction != 3:
                            current_direction = 1

                    if event.key == pygame.K_LEFT:
                        if current_direction != 0:
                            current_direction = 2 

                    if event.key == pygame.K_UP:
                        if current_direction != 1:
                            current_direction = 3
                    
                    moved = False

                    if event.key == pygame.K_ESCAPE:
                        run = False


        if check_lost(snake):
            draw_text_middle(surface, 
                             "El Serpiento que se muerde la cola!", 
                             50, 
                             (240, 240, 240))
            pygame.display.update()
            pygame.time.delay(2000)
            run = False
            update_score(score)
    
        score = snake.eat_mouse(score)
        draw_window(surface, score)
        snake.draw_snake(surface)
        pygame.display.update()


pygame.font.init()
surface_ = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Serpiento')
splash_screen(surface_)