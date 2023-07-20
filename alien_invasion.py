""" Draw the ship to the screen"""
import sys
import pygame
from settings_01 import Settings
from ship_01 import Ship

""" Adding the attribute moving.right from Ship class to check_events method"""

class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()

        # Creating instance of settings
        self.settings = Settings()
      

        '''set screen co-ordinates 1200 and 800 pixels'''
        self.screen = pygame.display.set_mode(self.settings.screen_width,self.settings.screen_height)
        pygame.display.set_caption('Alien Invasion')

        # Create new instance of ship
        self.ship = Ship(self)


    def run_game(self):
        """ Set the main loop for the game"""
        while True:
                self._check_events()
                self._update_screen()
                
    def _check_events(self):
         """ Respond mouse and keyboard movements"""
         for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                          if event.key == pygame.K_RIGHT:
                                #Move the ship to the right
                                self.ship.moving_right = True
                    elif event.key == pygame.KEYUP:
                        if event.key == pygame.K_RIGHT:
                            self.ship.moving_right = False

    def _update_screen(self):
          # Updare images on the screen during each pass through the loop and flip to the new screen
                self.screen.fill(self.settings.bg_color)
                self.ship.blitme()

                # Make the recently drawn screen visible
                pygame.display.flip()
          
            


if __name__ == '__main__':
    # Create an instance and run the game
    ai= AlienInvasion()
    ai.run_game()
