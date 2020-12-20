'''
This game is based on tutorial code provided by https://realpython.com/pygame-a-primer/
'''

import pygame

# Import pygame.locals for easier access to key coordinates
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT

pygame.init()

# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75,25))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen object using constants defined above
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Instantiate player
player = Player()

# Variable to keep the main loop running
running = True

# Game Loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        #Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the escape key? if so, stop
            if event.key == K_ESCAPE:
                running = False
        # Did the user click the window close button? if so, stop
        elif event.type == QUIT:
            running = False

    # Fill the screen with white
    screen.fill((0,0,0))
    
    # Draw the player on the screen
    screen.blit(player.surf, player.rect)

    pygame.display.flip()