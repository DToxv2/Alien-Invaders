import pygame

from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load Alien Image and set rect.
        self.image = pygame.image.load('Images/Alien.png')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store Alien position.
        self.x = float(self.rect.x)

    def blitme(self):
        # Draw the alien at its current location.
        self.screen.blit(self.image, self.rect)

