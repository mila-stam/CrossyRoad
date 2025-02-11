import pygame
import random
import time

# Initialize Pygame
# pygame.init()
pygame.display.init()
pygame.font.init()

# Set up the display
WIDTH, HEIGHT = 1000, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Crossy Road Clone")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Define three different area schemes
AREA_SCHEMES = {
    1: [  # Level 1 - Beginner
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
    2: [  # Level 2 - Easy
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
    3: [  # Level 3 - Medium
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
    4: [  # Level 4 - Hard
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
    5: [  # Level 5 - Expert
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

# Load images
car_img = pygame.image.load('car-toy.png').convert_alpha()
car_img = pygame.transform.scale(car_img, (60, 40))

coin_img = pygame.image.load('money_3213537.png').convert_alpha()
coin_img = pygame.transform.scale(coin_img, (30, 30))

player_img = pygame.image.load('monster_4701936.png').convert_alpha()
player_img = pygame.transform.scale(player_img, (40, 40))

log_img = pygame.image.load('picture2.png').convert_alpha()
original_size = log_img.get_rect().size
scale_factor = 40 / original_size[1]
new_width = int(original_size[0] * scale_factor)
log_img = pygame.transform.scale(log_img, (new_width, 40))
level_up_img = pygame.image.load('level up.png').convert_alpha()
level_up_img = pygame.transform.scale(level_up_img, (400, 350))
# Add after other image loading
grass_img = pygame.image.load('grass03.png').convert_alpha()
road_img = pygame.image.load('crossy-road.png').convert_alpha()
river_img = pygame.image.load('crossy-river.png').convert_alpha()

# Scale images to match area heights while maintaining aspect ratio
def scale_terrain_image(image, desired_height):
    original_size = image.get_rect().size
    scale_factor = desired_height / original_size[1]
    new_width = int(original_size[0] * scale_factor)
    return pygame.transform.scale(image, (new_width, desired_height))

# Scale images
grass_img = scale_terrain_image(grass_img, 50)  # grass areas are 50px high
road_img = scale_terrain_image(road_img, 100)   # road areas are 100px high
river_img = scale_terrain_image(river_img, 50)  # river areas are 50px high


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT - 10
        self.rect.centerx = WIDTH // 2

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        self.rect.clamp_ip(screen.get_rect())

class Car(pygame.sprite.Sprite):
    def __init__(self, y, speed):
        super().__init__()
        self.image = car_img
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = 0  # This will be set in spawn_level_objects
        self.speed = speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.left > WIDTH:
            self.rect.right = -100  # Reset further back for more spacing


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
            # Random number of cars (2 to 4) for each road
            num_cars = random.randint(2, 4)
            used_positions = set()
            
            # Distribute cars across the road width
            for _ in range(num_cars):
                max_attempts = 100
                attempts = 0
                while attempts < max_attempts:
                    # Random x position across entire width plus buffer
                    x_pos = random.randint(-200, WIDTH + 200)
                    y = random.randint(area["y"], area["y"] + area["height"] - 40)
                    
                    # Check if position is far enough from other cars
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


# Game setup
player = Player()
cars = pygame.sprite.Group()
logs = pygame.sprite.Group()
coins = pygame.sprite.Group()
current_level = 1


# Initial spawn
# spawn_level_objects(current_level)
try:
    spawn_level_objects(current_level)
except Exception as e:
    print(f"Error spawning objects: {e}")
    pygame.quit()
    exit(1)

# Spawn coins
for _ in range(15):
    x = random.randint(0, WIDTH - 30)
    y = random.randint(0, HEIGHT - 30)
    coins.add(Coin(x, y))

# Game variables
clock = pygame.time.Clock()
game_font = pygame.font.Font('freesansbold.ttf', 36)  # Main game font
large_font = pygame.font.Font('freesansbold.ttf', 48)  # For level completion
small_font = pygame.font.Font('freesansbold.ttf', 24)  # For smaller textstart_time = time.time()
elapsed_time = 0
game_over = False
game_won = False
level_complete = False
# Add to game variables
level_score = 0
total_score = 0
start_time = time.time()
score_added = False

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and not game_over and not game_won:
            if event.key == pygame.K_LEFT:
                player.move(-30, 0)
            elif event.key == pygame.K_RIGHT:
                player.move(30, 0)
            elif event.key == pygame.K_UP:
                player.move(0, -30)
        elif event.type == pygame.MOUSEBUTTONDOWN and (game_over or game_won):
            if restart_button.collidepoint(event.pos):
                current_level = 1
                player.rect.bottom = HEIGHT - 10
                player.rect.centerx = WIDTH // 2
                total_score = 0
                level_score = 0
                start_time = time.time()
                elapsed_time = 0
                game_over = False
                game_won = False
                spawn_level_objects(current_level)
                coins.empty()
                for _ in range(15):
                    x = random.randint(0, WIDTH - 30)
                    y = random.randint(0, HEIGHT - 30)
                    coins.add(Coin(x, y))
        elif event.type == pygame.MOUSEBUTTONDOWN and level_complete:
            if continue_button.collidepoint(event.pos):
                total_score += level_score
                level_score=0
                current_level += 1
                player.rect.bottom = HEIGHT - 10
                player.rect.centerx = WIDTH // 2
                level_complete = False
                spawn_level_objects(current_level)
                coins.empty()
                for _ in range(15):
                    x = random.randint(0, WIDTH - 30)
                    y = random.randint(0, HEIGHT - 30)
                    coins.add(Coin(x, y))     


    if not game_over and not game_won:
        cars.update()
        logs.update()
        elapsed_time = int(time.time() - start_time)

        # Car collision check
        for car in cars:
            player_feet = pygame.Rect(
                player.rect.x,
                player.rect.bottom - 10,
                player.rect.width,
                10
            )
            if player_feet.colliderect(car.rect):
                game_over = True

        # River collision logic
        on_log = False
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
                # current_level += 1
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


    # Draw everything
    screen.fill(WHITE)

    if not game_over and not game_won:
        for area in AREA_SCHEMES[current_level]:
            # Calculate how many times to repeat the image
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

    if level_complete:
        # Draw repeating grass background
        img_width = grass_img.get_width()
        num_repeats_x = WIDTH // img_width + 1
        num_repeats_y = HEIGHT // grass_img.get_height() + 1
        for y in range(num_repeats_y):
            for x in range(num_repeats_x):
                screen.blit(grass_img, (x * img_width, y * grass_img.get_height()))
        
        # Draw level up image centered at top
        screen.blit(level_up_img, 
                    (WIDTH // 2 - level_up_img.get_width() // 2, 
                    HEIGHT // 4 - level_up_img.get_height() // 2))
        
        
        
        # Level completion text
        level_text = large_font.render(f"Level {current_level} Complete!", True, BLACK)
        coins_text = game_font.render(f"Coins Collected: {level_score}", True, BLACK)
        
        # Draw text with shadow effect
        shadow_offset = 2
        shadow_color = (100, 100, 100)
        
       
        # Draw text
        screen.blit(level_text, 
                    (WIDTH // 2 - level_text.get_width() // 2, 
                    HEIGHT // 2 - 20))
        screen.blit(coins_text, 
                    (WIDTH // 2 - coins_text.get_width() // 2, 
                    HEIGHT // 2 + 30))
        
        # Create a nicer looking button
        button_color = (52, 76, 183)
        button_hover_color = (0, 9, 87)
        
        # Check if mouse is over button
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
        screen.fill(RED)
        game_over_text = large_font.render(f"Game Over! Level: {current_level} Score: {total_score} Time: {elapsed_time}s", True, WHITE)
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50))
        restart_button = pygame.draw.rect(screen, GREEN, (WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50))
        restart_text = game_font.render("Click to restart", True, BLACK)
        screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 60))

    if game_won:
        screen.fill(GREEN)
        # Only add level_score to total_score once
        if not score_added:
            total_score += level_score
            score_added = True
            
        game_won_text = large_font.render(f"You won! Final Score: {total_score} Time: {elapsed_time}s", True, BLACK)
        screen.blit(game_won_text, (WIDTH // 2 - game_won_text.get_width() // 2, HEIGHT // 2 - 50))
        restart_button = pygame.draw.rect(screen, BLUE, (WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50))
        restart_text = game_font.render("Play Again", True, WHITE)
        screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 60))
        
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
                score_added = False  # Reset the flag when restarting
                spawn_level_objects(current_level)
                coins.empty()
                for _ in range(15):
                    x = random.randint(0, WIDTH - 30)
                    y = random.randint(0, HEIGHT - 30)
                    coins.add(Coin(x, y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
