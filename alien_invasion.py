import pygame, sys

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption('Alien Invasion')
    bg_color = (230, 230, 230)

    # Main Game Loop
    while True:

        # Keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen
        screen.fill(bg_color)

        # Make the most recently drawn screen visible
        pygame.display.flip()

run_game()