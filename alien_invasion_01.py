import sys
import pygame

""" Created a Pygame window and responding to user input """
class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
      

        '''set screen co-ordinates 1200 and 800 pixels'''
        self.screen = pygame.display.set_mode(1200,800)
        pygame.display.set_caption('Alien Invasion')


    def run_game(self):
        """ Set the main loop for the game"""
        while True:
                """ Watch for mouse and keyboard movements"""
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
            


                # Make the recently drawn screen visible
                pygame.display.flip()
            


if __name__ == '__main__':
    # Create an instance and run the game
    ai= AlienInvasion()
    ai.run_game()
