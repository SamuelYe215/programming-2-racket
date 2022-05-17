import pygame
import random


# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 800
HEIGHT = 600
TITLE = "Flappy Bird"

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        # Call superclass constructor
        super().__init__()

        self.image = pygame.image.load("./assets/Flappybird.png")
        # Transform the image to be smaller
        self.image = pygame.transform.scale(
            self.image,
            (100, 100),
        )
        self.rect = self.image.get_rect()
        self.rect.center = 250, 300

        self.change_y = 0

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .30

    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()
        self.rect.y += self.change_y

    def jump(self):
        """ Called when user hits 'jump' button. """
        self.change_y = -9

class Pipe(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Image
        self.image = pygame.image.load("./assets/pipe.png")
        self.image = pygame.transform.scale(
            self.image,
            (150, 500),
        )
        # Rect
        self.rect = self.image.get_rect()
        self.rect.center = 0, random_height()

        self.xvel = -3

    def update(self):
        """Change the ycoord by yvel"""
        self.rect.x += self.xvel

def random_height():
    y = (
        random.randrange(350, 600)
    )
    return y

def main():
    pygame.init()

    bird = Bird()

    player_sprites_group = pygame.sprite.Group()
    player_sprites_group.add(bird)
    obstacle_sprites_group = pygame.sprite.Group()


    for i in range(100):
        pipe = Pipe()
        toppipe = Pipe()
            # Random placement
        pipe.rect.center = 800 + 600 * i, random_height()
        toppipe.image = pygame.transform.rotate(pipe.image, 180)
        toppipe.rect.center = pipe.rect.centerx, pipe.rect.centery - 675


            # Add pipes to obstacle sprite group
        obstacle_sprites_group.add(pipe)
        obstacle_sprites_group.add(toppipe)

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                bird.jump()

        # ----- LOGIC
        player_sprites_group.update()
        obstacle_sprites_group.update()
        # ----- RENDER
        screen.fill(BLACK)
        player_sprites_group.draw(screen)
        obstacle_sprites_group.draw(screen)

        # ----- UPDATE DISPLAY
        pygame.display.flip()
        clock.tick(75)

    pygame.quit()


if __name__ == "__main__":
    main()