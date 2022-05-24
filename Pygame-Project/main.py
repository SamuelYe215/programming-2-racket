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
        self.rect.center = 250, 100
        self.rect = self.rect.inflate(-50, -50)

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
        self.rect = self.rect.inflate(-40, -50)
        self.rect.center = 0, random_height()

        self.xvel = -3

    def update(self):
        """Change the xcoord by xvel"""
        self.rect.x += self.xvel

class BG(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()

        self.image = pygame.image.load("./assets/bg.png")
        self.image = pygame.transform.scale(self.image, (800, 600))

        self.rect = self.image.get_rect()

class Srect(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Image
        self.image = pygame.image.load("./assets/Srect.png")
        self.image = pygame.transform.scale(
            self.image,
            (10, 500),
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
        random.randrange(450, 800)
    )
    return y

def main():
    pygame.init()

    bird = Bird()

    bg = BG()

    player_sprites_group = pygame.sprite.Group()

    player_sprites_group.add(bird)

    obstacle_sprites_group = pygame.sprite.Group()

    bg_sprites_group = pygame.sprite.Group()

    srect_sprites_group = pygame.sprite.Group()

    bg_sprites_group.add(bg)


    for i in range(100):
        pipe = Pipe()
        toppipe = Pipe()
        srect = Srect()
            # Random placement
        pipe.rect.center = 800 + 600 * i, random_height()
        toppipe.image = pygame.transform.rotate(pipe.image, 180)
        toppipe.rect.center = pipe.rect.centerx, pipe.rect.centery - 700
        srect.rect.center = pipe.rect.centerx + 20, pipe.rect.centery - 325


            # Add pipes to obstacle sprite group
        obstacle_sprites_group.add(pipe)
        obstacle_sprites_group.add(toppipe)
        srect_sprites_group.add(srect)

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()
    score = 0
    font = pygame.font.Font("./assets/Roboto-2/Roboto-Black.ttf", 50)
    font2 = pygame.font.Font("./assets/Roboto-2/Roboto-Black.ttf", 25)

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            bird.jump()

        # ----- LOGIC
        player_sprites_group.update()

        obstacle_sprites_group.update()

        srect_sprites_group.update()

        collided_enemy = pygame.sprite.spritecollide(
            bird,
            obstacle_sprites_group,
            dokill=False
        )

        collided_score = pygame.sprite.spritecollide(
            bird,
            srect_sprites_group,
            dokill=True
        )

        if len(collided_enemy) > 0:
            pygame.sprite.Sprite.kill(bird)
            bird.rect.centery = 10000

        if len(collided_score) > 0:
            score += 1

        # ----- RENDER
        screen.fill(BLACK)

        srect_sprites_group.draw(screen)
        bg_sprites_group.draw(screen)
        player_sprites_group.draw(screen)
        obstacle_sprites_group.draw(screen)

        text = font.render(f"{score}", True, WHITE)
        screen.blit(text, (100, 50))
        instructions = font2.render("Click to fly", True, WHITE)
        screen.blit(instructions, (625, 30))

        # ----- UPDATE DISPLAY
        pygame.display.flip()
        clock.tick(75)

    pygame.quit()


if __name__ == "__main__":
    main()