import pygame
import random

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 800
HEIGHT = 600
TITLE = "DVD Screensaver"


class Dvdlogo(pygame.sprite.Sprite):
    def __init__(self):
        # Call superclass constructor
        super().__init__()

        self.image = pygame.image.load("./assets/image.png")
        # Transform the image to be smaller
        self.image = pygame.transform.scale(
            self.image,
            (200, 115),
        )
        # Default (x, y) is (0, 0)
        self.rect = self.image.get_rect()

        # Choose a random direction
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


def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()

    dvd_logo = Dvdlogo()
    # Set the coordinates of dvd_logo explicitly
    dvd_logo.rect.x = 100
    dvd_logo.rect.y = 100

    # Create an all_sprites_group object
    all_sprites_group = pygame.sprite.Group()

    # Add the Dvdlogo sprite to the all_sprites_group
    all_sprites_group.add(dvd_logo)

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC

        # Update all sprites
        all_sprites_group.update()
        print(dvd_logo.rect.x)

        # ----- RENDER
        screen.fill(WHITE)

        all_sprites_group.draw(screen)

        # ----- UPDATE DISPLAY
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()