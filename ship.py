import pygame
"""Allowing continous movement across right"""
class Ship:
    """A class to manage the ship"""

    def __init__(self,ai_game):
        """Initialize the ship and get its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Start each ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
       
        #Movement Flag
        self.moving_right = False
       

    def update(self):
        """Update ths ship's position based on movement flag."""
        if self.moving_right:
            self.rect.x += 1

      


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)