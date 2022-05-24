# Intro to Pygame

import pygame

pygame.init()

# Constants
BLACK   = (  0,  0,  0)
WHITE   = (255,255,255)
RED     = (255,  0,  0)
GREEN     = (  0, 250, 0)
BLUE   = (  0,  0,255)
WINDOW_TITLE = "Game"

def main():
    # Create a window
    screen_size = (800, 600)
    screen = pygame.display.set_mode(screen_size)

    # Set title
    pygame.display.set_caption(WINDOW_TITLE)

    done = False

    clock = pygame.time.Clock()

    # ---- MAIN PROGRAM LOOP ----
    while not done:
        # --- Event Handler ---
        for event in pygame.event.get():   # list of events
            if event.type == pygame.QUIT:
                # When the user clicks the red quit button
                done = True
            # elif event.type == pygame.KEYDOWN:
            #     print("A key has bee pressed down.")
            # elif event.type == pygame.KEYUP:
            #     print("A key has been let go of.")
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     print("A mouse button has been pressed.")
        # --- Environment logic ---

        # --- Render the Environment ---

        # Fill screen with background colour
        screen.fill(WHITE)

        # Draw a rectangle
        # rect -> [x, y, width, height]
        # pygame.draw.rect(screen, GREEN, [0, 0, 400, 200])
        #
        # # Draw a line
        # pygame.draw.line(screen, BLACK, (0,0), screen_size)

        # Draw a series of lines
        # for delta_Y in range(30, 230, 10):
        #     pygame.draw.line(screen, BLUE, (0, 10+delta_Y), (100, 100+delta_Y))

        pygame.draw.circle(screen, GREEN, (400, 300), 300)
        pygame.draw.circle(screen, BLACK, (500, 200), 50)
        pygame.draw.circle(screen, BLACK, (300, 200), 50)
        pygame.draw.ellipse(screen, BLACK, (270, 350, 300, 100))
        # --- Flip the display ---
        # Updates the screen with what we've drawn
        pygame.display.flip()

        # --- Tick the clock ---
        clock.tick(75)
if __name__ == "__main__":
    main()