# introtocollision.py

import random
import pygame

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 800
HEIGHT = 600
TITLE = "Intro to Collision"


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Image
        self.image = pygame.image.load("./assets/mario.png")
        self.image = pygame.transform.scale(self.image, (38, 38))   # scale
        # self.image.set_colorkey((WHITE))      # set transparency

        # Rect
        self.rect = self.image.get_rect()

    def update(self):
        """Follow the mouse"""
        self.rect.center = pygame.mouse.get_pos()


class Treasure(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Image
        self.image = pygame.image.load("./assets/coin.png")

        # Rect
        self.rect = self.image.get_rect()
        self.rect.center = random_coords()      # random location

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./assets/8def693db9193b8.png")
        self.image = pygame.transform.scale(self.image, (150, 150))

        self.rect = self.image.get_rect()
        self.rect.center = random_coords()

        self.xvel = random.choice([-5, -3, 3, 5])       # 1 pixel per 1/60th second
        self.yvel = random.choice([-5, -3, 3, 5])

    def update(self):
        """Change the x coordinate based on the xvel"""
        self.rect.x += self.xvel
        self.rect.y += self.yvel

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.xvel *= -1
        if self.rect.left < 0:
            self.rect.left = 0
            self.xvel *= -1
        if self.rect.top < 0:
            self.rect.top = 0
            self.yvel *= -1
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.yvel *= -1


def random_coords() -> list:
    """Returns a random x, y coord between
    0 to WIDTH and 0 to HEIGHT respectively"""
    return random.randrange(0, WIDTH), random.randrange(0, HEIGHT)


def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)
    pygame.mouse.set_visible(False)     # make cursor invisible

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()
    player_health = 3
    num_treasure = 10
    num_enemy = 3
    score = 0
    font = pygame.font.Font("./assets/Roboto-Black.ttf", 50)

    coin_sound = pygame.mixer.Sound("./assets/coinsound.ogg")

    # Create sprite groups
    all_sprites_group = pygame.sprite.Group()
    treasure_sprites_group = pygame.sprite.Group()
    enemy_sprites_group = pygame.sprite.Group()
    player_sprites_group = pygame.sprite.Group()

    # Create sprites to fill groups
    # Create treasure sprites
    for i in range(num_treasure):
        treasure = Treasure()

        # Add it to BOTH lists: all_sprites_group and treasure_sprites_group
        all_sprites_group.add(treasure)
        treasure_sprites_group.add(treasure)

    player = Player()
    player_sprites_group.add(player)
    all_sprites_group.add(player)

    for i in range(num_enemy):
        enemy = Enemy()

        all_sprites_group.add(enemy)
        enemy_sprites_group.add(enemy)

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC
        all_sprites_group.update()

        # Deal with collision between player and treasure sprites
        #  PLAYER collides with any sprite from TREASURE_SPRITE_GROUP
        collided_treasure = pygame.sprite.spritecollide(
            player,
            treasure_sprites_group,
            dokill=True
        )

        collided_enemy = pygame.sprite.spritecollide(
            enemy,
            player_sprites_group,
            dokill=True
        )

        if len(collided_treasure) > 0:
            coin_sound.play()
            score += 1

        # Iterate through all collided treasure
        for treasure in collided_treasure:
            print(f"x: {treasure.rect.x}")
            print(f"y: {treasure.rect.y}")
            print(f'{score}')

            # Replace the treasure
            treasure = Treasure()
            all_sprites_group.add(treasure)
            treasure_sprites_group.add(treasure)

        # ----- RENDER
        screen.fill(BLACK)
        all_sprites_group.draw(screen)

        text = font.render(f"{score}", True, WHITE)
        screen.blit(text, (50, 50))

        # ----- UPDATE DISPLAY
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()