'''
This game is based on tutorial code provided by https://realpython.com/pygame-a-primer/
'''

import pygame

# Import pygame.locals for easier access to key coordinates
from pygame.locals import RLEACCEL, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT
from rp_classes import *

pygame.init()

# Setup the clock for a decent framerate
clock = pygame.time.Clock()

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen object using constants defined above
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a custom event for adding a new enemy and a cloud
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

# Instantiate player
player = Player(SCREEN_HEIGHT, SCREEN_WIDTH)

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

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

        # Add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy(SCREEN_HEIGHT, SCREEN_WIDTH)
            enemies.add(new_enemy)
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        # Add a new cloud?
        elif event.type == ADDCLOUD:
            # Create the new cloud and add it to sprite groups
            new_cloud = Cloud(SCREEN_HEIGHT, SCREEN_WIDTH)
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    # Get all the keys currently pressed
    pressed_keys = pygame.key.get_pressed()

    # Update the player sprite based on your keypresses
    player.update(pressed_keys)

    # Update enemy and cloud positions
    enemies.update()
    clouds.update()

    # Fill the screen with sky blue
    screen.fill((135, 206, 250))
    
    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        # If so, then remove the player and stop the loop
        player.kill()
        running = False

    # Flip everything to the display
    pygame.display.update()

    # Ensure the program maintains a rate of 30 frames per second
    clock.tick(30)