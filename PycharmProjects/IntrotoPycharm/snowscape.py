# snowscape.py

import random
import pygame

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 800
HEIGHT = 600
TITLE = "Snowscape"


class Snow(pygame.sprite.Sprite):
    def __init__(self, width: int):
        """
        :param width: width of snow in px
        """
        super().__init__()

        self.image = pygame.Surface([width, width])

        # fill that image with an actual shape
        pygame.draw.circle(
            self.image,
            WHITE,
            (width // 2, width // 2),   # draw in the middle
            width // 2
        )
        self.image.set_colorkey(BLACK)  # transparency

        self.rect = self.image.get_rect()

        self.yvel = 3

    def update(self):
        """Change the ycoord by yvel"""
        self.rect.y += self.yvel

        # Recycle snow -> reset its position to the top
        if self.rect.y > HEIGHT:
            self.rect.x = random.randrange(0, WIDTH)
            self.rect.y = random.randrange(-50, -10)



def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()

    num_snow = 100

    # Create a snow sprites group
    snow_sprites = pygame.sprite.Group()
    # snow_sprites_farther = pygame.sprite.Group()

    # Create num_snow snowflakes
    for i in range(num_snow):
        snow = Snow(10)

        # Random placement
        snow.rect.center = random_coords()

        # Add the snow object to the snow sprites group
        snow_sprites.add(snow)

        # Create smaller snow
        snow = Snow(random.choice([2, 5]))
        snow.rect.center = random_coords()
        snow.yvel = random.choice([1, 2])
        snow_sprites.add(snow)

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC
        snow_sprites.update()

        # ----- RENDER
        screen.fill(BLACK)

        # Draw all the sprite groups
        snow_sprites.draw(screen)

        # ----- UPDATE DISPLAY
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


def random_coords():
    x, y = (
        random.randrange(0, WIDTH),
        random.randrange(0, HEIGHT)
    )
    return x, y


if __name__ == "__main__":
    main()