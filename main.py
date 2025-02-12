import pygame
import random
import time
import math

pygame.display.init()
pygame.font.init()

WIDTH, HEIGHT = 1000, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Crossy Road Clone")
print(pygame.font.get_fonts())


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

AREA_SCHEMES = {
    1: [  
        {"type": "grass", "y": HEIGHT-50, "height": 50},
        {"type": "road", "y": HEIGHT - 150, "height": 100},
        {"type": "grass", "y": HEIGHT - 200, "height": 50},
        {"type": "river", "y": HEIGHT - 250, "height": 50},
        {"type": "grass", "y": HEIGHT - 300, "height": 50},
        {"type": "road", "y": HEIGHT - 400, "height": 100},
        {"type": "river", "y": HEIGHT - 450, "height": 50},
        {"type": "grass", "y": HEIGHT - 500, "height": 50},
        {"type": "road", "y": HEIGHT - 600, "height": 100},
        {"type": "grass", "y": HEIGHT - 650, "height": 50},
        {"type": "river", "y": HEIGHT - 700, "height": 50},
        {"type": "grass", "y": 0, "height": 100}
    ],
    2: [ 
        {"type": "grass", "y": HEIGHT-50, "height": 50},
        {"type": "river", "y": HEIGHT - 100, "height": 50},
        {"type": "road", "y": HEIGHT - 200, "height": 100},
        {"type": "grass", "y": HEIGHT - 250, "height": 50},
        {"type": "river", "y": HEIGHT - 300, "height": 50},
        {"type": "road", "y": HEIGHT - 400, "height": 100},
        {"type": "river", "y": HEIGHT - 450, "height": 50},
        {"type": "grass", "y": HEIGHT - 500, "height": 50},
        {"type": "river", "y": HEIGHT - 550, "height": 50},
        {"type": "road", "y": HEIGHT - 650, "height": 100},        
        {"type": "grass", "y": HEIGHT - 700, "height": 50},
        {"type": "grass", "y": 0, "height": 100}
    ],
    3: [ 
        {"type": "grass", "y": HEIGHT-50, "height": 50},
        {"type": "river", "y": HEIGHT - 100, "height": 50},
        {"type": "road", "y": HEIGHT - 200, "height": 100},
        {"type": "grass", "y": HEIGHT - 250, "height": 50},
        {"type": "grass", "y": HEIGHT - 300, "height": 50},
        {"type": "river", "y": HEIGHT - 350, "height": 50},
        {"type": "river", "y": HEIGHT - 400, "height": 50},
        {"type": "grass", "y": HEIGHT - 450, "height": 50},
        {"type": "road", "y": HEIGHT - 550, "height": 100},
        {"type": "grass", "y": HEIGHT - 600, "height": 50},
        {"type": "road", "y": HEIGHT - 700, "height": 100},
        {"type": "grass", "y": 0, "height": 50}
    ],
    4: [ 
        {"type": "grass", "y": HEIGHT-50, "height": 50},
        {"type": "road", "y": HEIGHT - 150, "height": 100},
        {"type": "road", "y": HEIGHT - 250, "height": 100},
        {"type": "river", "y": HEIGHT - 300, "height": 50},
        {"type": "grass", "y": HEIGHT - 350, "height": 50},
        {"type": "river", "y": HEIGHT - 400, "height": 50},
        {"type": "river", "y": HEIGHT - 450, "height": 50},
        {"type": "road", "y": HEIGHT - 550, "height": 100},
        {"type": "river", "y": HEIGHT - 600, "height": 50},
        {"type": "grass", "y": HEIGHT - 650, "height": 50},
        {"type": "river", "y": HEIGHT - 700, "height": 50},
        {"type": "grass", "y": 0, "height": 50}
    ],
    5: [ 
        {"type": "grass", "y": HEIGHT-50, "height": 50},
        {"type": "river", "y": HEIGHT - 100, "height": 50},
        {"type": "road", "y": HEIGHT - 200, "height": 100},
        {"type": "river", "y": HEIGHT - 250, "height": 50},
        {"type": "road", "y": HEIGHT - 350, "height": 100},
        {"type": "river", "y": HEIGHT - 400, "height": 50},
        {"type": "river", "y": HEIGHT - 450, "height": 50},
        {"type": "road", "y": HEIGHT - 550, "height": 100},
        {"type": "river", "y": HEIGHT - 600, "height": 50},
        {"type": "road", "y": HEIGHT - 700, "height": 100},
        {"type": "grass", "y": 0, "height": 50}
    ]
}


car_img = pygame.image.load('images/car-toy.png').convert_alpha()
car_img = pygame.transform.scale(car_img, (60, 40))

coin_img = pygame.image.load('images/money_3213537.png').convert_alpha()
coin_img = pygame.transform.scale(coin_img, (30, 30))

player_img = pygame.image.load('images/monster_4701936.png').convert_alpha()
player_img = pygame.transform.scale(player_img, (40, 40))

log_img = pygame.image.load('images/picture2.png').convert_alpha()
original_size = log_img.get_rect().size
scale_factor = 40 / original_size[1]
new_width = int(original_size[0] * scale_factor)
log_img = pygame.transform.scale(log_img, (new_width, 40))
level_up_img = pygame.image.load('images/level up.png').convert_alpha()
level_up_img = pygame.transform.scale(level_up_img, (400, 350))

game_over_img = pygame.image.load('images/game over.png').convert_alpha()
game_over_img = pygame.transform.scale(game_over_img, (600, 400))

confetti_img = pygame.image.load('images/5676045.jpg').convert_alpha()
confetti_img = pygame.transform.scale(confetti_img, (WIDTH, HEIGHT))

trophy_img = pygame.image.load('images/trophy.png').convert_alpha()
trophy_img = pygame.transform.scale(trophy_img, (200, 200))

keys_img = pygame.image.load('images/keys1.png').convert_alpha()
keys_img = pygame.transform.scale(keys_img, (200, 100))

title_img = pygame.image.load('images/Untitled-1.png').convert_alpha()
title_img = pygame.transform.scale(title_img, (600, 150))  
grass_img = pygame.image.load('images/grass03.png').convert_alpha()
road_img = pygame.image.load('images/crossy-road.png').convert_alpha()
river_img = pygame.image.load('images/crossy-river.png').convert_alpha()

grass_img.set_alpha(200)  

def scale_terrain_image(image, desired_height):
    original_size = image.get_rect().size
    scale_factor = desired_height / original_size[1]
    new_width = int(original_size[0] * scale_factor)
    return pygame.transform.scale(image, (new_width, desired_height))

grass_img = scale_terrain_image(grass_img, 50)  
road_img = scale_terrain_image(road_img, 100)   
river_img = scale_terrain_image(river_img, 50)  


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT - 10
        self.rect.centerx = WIDTH // 2
        self.normal_step = 30
        self.river_step = 50  
        self.current_step = self.normal_step

    def move(self, dx, dy):
        actual_dx = dx * (self.current_step / self.normal_step)
        actual_dy = dy * (self.current_step / self.normal_step)
        self.rect.x += actual_dx
        self.rect.y += actual_dy
        self.rect.clamp_ip(screen.get_rect())

    def update_step_size(self, areas, current_y):
        for i in range(len(areas) - 1):
            if (areas[i]["type"] == "river" and 
                areas[i+1]["type"] == "river" and 
                areas[i]["y"] < current_y < areas[i]["y"] + areas[i]["height"] + areas[i+1]["height"]):
                self.current_step = self.river_step
                return
        self.current_step = self.normal_step

class Car(pygame.sprite.Sprite):
    def __init__(self, y, speed):
        super().__init__()
        self.image = car_img
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = 0  
        self.speed = speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.left > WIDTH:
            self.rect.right = -100  


class Log(pygame.sprite.Sprite):
    def __init__(self, y, speed, x=0):
        super().__init__()
        self.image = log_img
        self.rect = self.image.get_rect()
        self.rect.y = y + 5
        self.rect.x = x
        self.speed = speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.left > WIDTH:
            self.rect.right = 0

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

def spawn_level_objects(level):
    cars.empty()
    logs.empty()
    
    car_speed = 1.5 + (level * 0.8)
    log_speed = 0.8 + (level * 0.4)
    
    for area in AREA_SCHEMES[level]:
        if area["type"] == "road":
            num_cars = random.randint(2, 4)
            used_positions = set()
            
            for _ in range(num_cars):
                max_attempts = 100
                attempts = 0
                while attempts < max_attempts:
                    x_pos = random.randint(-200, WIDTH + 200)
                    y = random.randint(area["y"], area["y"] + area["height"] - 40)
                    
                    if all(abs(x_pos - pos[0]) > 150 and abs(y - pos[1]) > 45 for pos in used_positions):
                        used_positions.add((x_pos, y))
                        car = Car(y, car_speed)
                        car.rect.x = x_pos
                        cars.add(car)
                        break
                    attempts += 1
                        
        elif area["type"] == "river":
            used_positions = set()
            
            for _ in range(4):
                max_attempts = 100
                attempts = 0
                while attempts < max_attempts:
                    x_pos = random.randint(-100, WIDTH)
                    if all(abs(x_pos - pos) > new_width + 50 for pos in used_positions):
                        used_positions.add(x_pos)
                        logs.add(Log(area["y"], log_speed, x_pos))
                        break
                    attempts += 1


player = Player()
cars = pygame.sprite.Group()
logs = pygame.sprite.Group()
coins = pygame.sprite.Group()
current_level = 1

try:
    spawn_level_objects(current_level)
except Exception as e:
    print(f"Error spawning objects: {e}")
    pygame.quit()
    exit(1)

for _ in range(15):
    x = random.randint(0, WIDTH - 30)
    y = random.randint(0, HEIGHT - 30)
    coins.add(Coin(x, y))

clock = pygame.time.Clock()
game_font = pygame.font.SysFont('bahnschrift', 36)
large_font = pygame.font.SysFont('berlinsansfb', 52)
small_font = pygame.font.SysFont('berlinsansfb', 36)
elapsed_time = 0
game_over = False
game_won = False
level_complete = False
level_score = 0
total_score = 0
start_time = time.time()
score_added = False
game_started = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not game_started:
                if start_button.collidepoint(event.pos):
                    game_started = True
                    start_time = time.time()
            elif game_over and restart_button.collidepoint(event.pos):
                current_level = 1
                player.rect.bottom = HEIGHT - 10
                player.rect.centerx = WIDTH // 2
                level_score = 0
                total_score = 0
                start_time = time.time()
                elapsed_time = 0
                game_over = False
                game_won = False
                game_started = False
                spawn_level_objects(current_level)
                coins.empty()
                for _ in range(15):
                    x = random.randint(0, WIDTH - 30)
                    y = random.randint(0, HEIGHT - 30)
                    coins.add(Coin(x, y))
            elif level_complete and continue_button.collidepoint(event.pos):
                total_score += level_score
                level_score = 0
                current_level += 1
                player.rect.bottom = HEIGHT - 10
                player.rect.centerx = WIDTH // 2
                level_complete = False
                start_time = time.time() - elapsed_time
                spawn_level_objects(current_level)
                coins.empty()
                for _ in range(15):
                    x = random.randint(0, WIDTH - 30)
                    y = random.randint(0, HEIGHT - 30)
                    coins.add(Coin(x, y))
        elif event.type == pygame.KEYDOWN and game_started and not game_over and not game_won and not level_complete:
            if event.key == pygame.K_LEFT:
                player.move(-30, 0)
            elif event.key == pygame.K_RIGHT:
                player.move(30, 0)
            elif event.key == pygame.K_UP:
                player.move(0, -30)

    screen.fill(WHITE)

    if not game_started:
        img_width = grass_img.get_width()
        num_repeats_x = WIDTH // img_width + 1
        num_repeats_y = HEIGHT // grass_img.get_height() + 1
        for y in range(num_repeats_y):
            for x in range(num_repeats_x):
                screen.blit(grass_img, (x * img_width, y * grass_img.get_height()))
        
        road_y = HEIGHT // 3
        img_width = road_img.get_width()
        num_repeats = WIDTH // img_width + 1
        for i in range(num_repeats):
            screen.blit(road_img, (i * img_width, road_y))
        
        car_x = (pygame.time.get_ticks() // 5) % (WIDTH + 60) - 60
        screen.blit(car_img, (car_x, road_y + 30))
        
        screen.blit(keys_img, (WIDTH // 2 - keys_img.get_width() // 2, road_y + 100))
        
        screen.blit(title_img, (WIDTH // 2 - title_img.get_width() // 2, 100))

        button_color = (52, 76, 183)
        button_hover_color = (0, 9, 87)
        start_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT - 150, 200, 50)
        
        if start_button.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, button_hover_color, start_button, border_radius=10)
        else:
            pygame.draw.rect(screen, button_color, start_button, border_radius=10)
        
        start_text = game_font.render("Start Game", True, WHITE)
        screen.blit(start_text, 
                    (WIDTH // 2 - start_text.get_width() // 2, 
                    HEIGHT - 140))
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                game_started = True

    elif not game_over and not game_won and not level_complete:
        cars.update()
        logs.update()
        elapsed_time = int(time.time() - start_time)

        for area in AREA_SCHEMES[current_level]:
            if area["type"] == "grass":
                img_width = grass_img.get_width()
                num_repeats = WIDTH // img_width + 1
                for i in range(num_repeats):
                    screen.blit(grass_img, (i * img_width, area["y"]))
            elif area["type"] == "road":
                img_width = road_img.get_width()
                num_repeats = WIDTH // img_width + 1
                for i in range(num_repeats):
                    screen.blit(road_img, (i * img_width, area["y"]))
            elif area["type"] == "river":
                img_width = river_img.get_width()
                num_repeats = WIDTH // img_width + 1
                for i in range(num_repeats):
                    screen.blit(river_img, (i * img_width, area["y"]))


        cars.draw(screen)
        logs.draw(screen)
        coins.draw(screen)
        screen.blit(player.image, player.rect)

        coins_text = small_font.render(f"Coins: {level_score}", True, BLACK)
        time_text = small_font.render(f"Time: {elapsed_time}s", True, BLACK)
        level_text = small_font.render(f"Level: {current_level}", True, BLACK)
        screen.blit(coins_text, (10, 10))
        screen.blit(time_text, (WIDTH - 150, 10))
        screen.blit(level_text, (WIDTH // 2 - 50, 10))


        for car in cars:
            player_feet = pygame.Rect(
                player.rect.x,
                player.rect.bottom - 10,
                player.rect.width,
                10
            )
            if player_feet.colliderect(car.rect):
                game_over = True

        on_log = False
        player.update_step_size(AREA_SCHEMES[current_level], player.rect.bottom)

        for area in AREA_SCHEMES[current_level]:
            if area["type"] == "river":
                if area["y"] < player.rect.bottom < area["y"] + area["height"]:
                    log_collisions = pygame.sprite.spritecollide(player, logs, False)
                    if log_collisions:
                        on_log = True
                        player.rect.x += log_collisions[0].speed
                    else:
                        game_over = True
                elif player.rect.bottom <= area["y"]:
                    on_log = False

        collected_coins = pygame.sprite.spritecollide(player, coins, True)
        level_score += len(collected_coins)


        if player.rect.top <= 0:
            if current_level < 5: 
                level_complete = True
                player.rect.bottom = HEIGHT - 10
                player.rect.centerx = WIDTH // 2
                spawn_level_objects(current_level)
                coins.empty()
                for _ in range(15):
                    x = random.randint(0, WIDTH - 30)
                    y = random.randint(0, HEIGHT - 30)
                    coins.add(Coin(x, y))
            else:
                game_won = True


    if level_complete:
        img_width = grass_img.get_width()
        num_repeats_x = WIDTH // img_width + 1
        num_repeats_y = HEIGHT // grass_img.get_height() + 1
        for y in range(num_repeats_y):
            for x in range(num_repeats_x):
                screen.blit(grass_img, (x * img_width, y * grass_img.get_height()))
        
        screen.blit(level_up_img, 
                    (WIDTH // 2 - level_up_img.get_width() // 2, 
                    HEIGHT // 4 - level_up_img.get_height() // 2))
        
        
        
        level_text = large_font.render(f"Level {current_level} Complete!", True, BLACK)
        coins_text = game_font.render(f"Coins Collected: {level_score}", True, BLACK)
        
        shadow_offset = 2
        shadow_color = (100, 100, 100)
        
       
        screen.blit(level_text, 
                    (WIDTH // 2 - level_text.get_width() // 2, 
                    HEIGHT // 2 - 20))
        screen.blit(coins_text, 
                    (WIDTH // 2 - coins_text.get_width() // 2, 
                    HEIGHT // 2 + 30))
        
        button_color = (52, 76, 183)
        button_hover_color = (0, 9, 87)
        
        mouse_pos = pygame.mouse.get_pos()
        continue_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT * 3 // 4, 200, 50)
        
        if continue_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, button_hover_color, continue_button, border_radius=10)
        else:
            pygame.draw.rect(screen, button_color, continue_button, border_radius=10)
        
        continue_text = game_font.render("Continue", True, WHITE)
        screen.blit(continue_text, 
                    (WIDTH // 2 - continue_text.get_width() // 2, 
                    HEIGHT * 3 // 4 + 10))

    if game_over:
        screen.fill((139, 0, 0))  
        screen.blit(game_over_img, 
                    (WIDTH // 2 - game_over_img.get_width() // 2, 
                    HEIGHT // 4 - game_over_img.get_height() // 2))
        
        game_over_text = large_font.render(f"Level: {current_level} Score: {total_score}", True, BLACK)
        time_text = game_font.render(f"Time: {elapsed_time}s", True, BLACK)
        
        screen.blit(game_over_text, 
                    (WIDTH // 2 - game_over_text.get_width() // 2, 
                    HEIGHT // 2))
        screen.blit(time_text, 
                    (WIDTH // 2 - time_text.get_width() // 2, 
                    HEIGHT // 2 + 50))
        
        button_color = (0, 0, 0)
        button_hover_color = (100, 100, 100)
        restart_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT - 150, 200, 50)
        
        if restart_button.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, button_hover_color, restart_button, border_radius=10)
        else:
            pygame.draw.rect(screen, button_color, restart_button, border_radius=10)
        
        restart_text = game_font.render("Try Again", True, WHITE)
        screen.blit(restart_text, 
                    (WIDTH // 2 - restart_text.get_width() // 2, 
                    HEIGHT - 140))


    if game_won:
        screen.blit(confetti_img, (0, 0))
        
        trophy_y_offset = math.sin(pygame.time.get_ticks() * 0.004) * 10
        screen.blit(trophy_img, 
                    (WIDTH // 2 - trophy_img.get_width() // 2, 
                    HEIGHT // 4 - trophy_img.get_height() // 2 + trophy_y_offset))
        
        if not score_added:
            total_score += level_score
            score_added = True
        
        game_won_text = large_font.render("Congratulations!", True, (218, 165, 32))
        score_text = game_font.render(f"Final Score: {total_score}", True, BLACK)
        time_text = game_font.render(f"Total Time: {elapsed_time}s", True, BLACK)
        
        text_padding = 20
        
        s = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        
        congrats_bg = pygame.Rect(
            WIDTH // 2 - game_won_text.get_width() // 2 - text_padding,
            HEIGHT // 2 - text_padding,
            game_won_text.get_width() + text_padding * 2,
            game_won_text.get_height() + text_padding * 2
        )
        pygame.draw.rect(s, (246,235,241, 230), congrats_bg, border_radius=10)
        
        score_bg = pygame.Rect(
            WIDTH // 2 - score_text.get_width() // 2 - text_padding,
            HEIGHT // 2 + 50 - text_padding,
            score_text.get_width() + text_padding * 2,
            score_text.get_height() + text_padding * 2
        )
        pygame.draw.rect(s, (246,235,241, 230), score_bg, border_radius=10)
        
        time_bg = pygame.Rect(
            WIDTH // 2 - time_text.get_width() // 2 - text_padding,
            HEIGHT // 2 + 100 - text_padding,
            time_text.get_width() + text_padding * 2,
            time_text.get_height() + text_padding * 2
        )
        pygame.draw.rect(s, (246,235,241, 230), time_bg, border_radius=10)
        
        screen.blit(s, (0,0))
        
        screen.blit(game_won_text, 
                    (WIDTH // 2 - game_won_text.get_width() // 2, 
                    HEIGHT // 2))
        screen.blit(score_text, 
                    (WIDTH // 2 - score_text.get_width() // 2, 
                    HEIGHT // 2 + 50))
        screen.blit(time_text, 
                    (WIDTH // 2 - time_text.get_width() // 2, 
                    HEIGHT // 2 + 100))
        
        button_color = (52, 76, 183)
        button_hover_color = (0, 9, 87)
        restart_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT - 150, 200, 50)
        
        if restart_button.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, button_hover_color, restart_button, border_radius=10)
            pygame.draw.rect(screen, (255, 255, 255, 128), restart_button.inflate(4, 4), 
                            border_radius=10, width=2)
        else:
            pygame.draw.rect(screen, button_color, restart_button, border_radius=10)
        
        restart_text = game_font.render("Play Again", True, WHITE)
        screen.blit(restart_text, 
                    (WIDTH // 2 - restart_text.get_width() // 2, 
                    HEIGHT - 140))
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if restart_button.collidepoint(event.pos):
                current_level = 1
                player.rect.bottom = HEIGHT - 10
                player.rect.centerx = WIDTH // 2
                level_score = 0
                total_score = 0
                start_time = time.time()
                elapsed_time = 0
                game_over = False
                game_won = False
                game_started = False
                score_added = False
                
                spawn_level_objects(current_level)
                coins.empty()
                for _ in range(15):
                    x = random.randint(0, WIDTH - 30)
                    y = random.randint(0, HEIGHT - 30)
                    coins.add(Coin(x, y))



    pygame.display.flip()
    clock.tick(60)

pygame.quit()
