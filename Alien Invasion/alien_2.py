import pygame
from pygame.sprite import Sprite


class Alien2(Sprite):

    def __init__(self, ai_game):
        """Initialize the special alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the special alien image and set its rect attribute.
        self.image = pygame.image.load('Artwork/Alien_2.bmp')
        self.rect = self.image.get_rect()

        # Start each new special alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the special alien's exact horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        """Move the special alien right."""
        self.x += self.settings.special_alien_speed
        self.rect.x = self.x
