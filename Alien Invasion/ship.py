import pygame

class Ship():

    def __init__(self, screen):
        self.screen = screen

        # Originele afbeelding was te groot. Import hem, daarna schaalt pygame hem kleiner naar 50x50 pixels
        self.originele_afbeelding = pygame.image.load('Artwork/Ship.bmp')
        self.image = pygame.transform.scale(self.originele_afbeelding, (50,50))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):

        self.screen.blit(self.image, self.rect)