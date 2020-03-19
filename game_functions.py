import sys
import pygame
from bullets import Bullets


def check_keydown_events(event, ship):
    """Repsonds to key presses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False }

def check_events(ship):
    """Respond to key presses and mouse events."""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Checks if key is pressed down    
            elif event.type == pygame.KEYDOWN:
                # Call to the keydown function above
                check_keydown_events(event, ship)
            # Checks if key is not pressed    
            elif event.type == pygame.KEYUP:
                # Call to the keyup function above
                check_keyup_events(event, ship)

            

def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Make the most recently drawn screen visible
    pygame.display.flip()