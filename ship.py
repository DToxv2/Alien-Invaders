import pygame

class Ship():

    def __init__(self, screen):
        self.screen = screen

        # Load Ship Image
        self.image = pygame.image.load('Images/galaga-ship-png-10.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        # Draw the ship at its current location
        self.screen.blit(self.image, self.rect)
