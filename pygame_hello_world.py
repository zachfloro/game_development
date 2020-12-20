'''
Simple Game to say Hello World!

Based on tutorial provided at https://realpython.com/pygame-a-primer/
'''

import pygame
pygame.init()

screen = pygame.display.set_mode([1000, 1000])

running = True
while running:

    # Check if the user closed the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background with white
    screen.fill((255,255,255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0,0,255), (500, 500), 75)

    # Flip the display
    pygame.display.flip()

pygame.quit()