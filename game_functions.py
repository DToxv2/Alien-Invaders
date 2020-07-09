import pygame, sys

def check_events(ship):
    # Keyboard and Mouse Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event,ship):
    if event.type == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.type == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event,ship):
    if event.type == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.type == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(ai_settings, screen, ship):
    # Redraw the screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Make the most recently drawn screen visible
    pygame.display.flip()