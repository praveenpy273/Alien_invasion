""" Adding the ship image"""
import pygame

class Ship_01:
    """A class to manage the ship"""

    def __init__(self,ai_game):
        """Initialize the ship and get its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()#accssing screen's rect attribute

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()# to access ship surface's rect attribute

        #Start each ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
  
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)