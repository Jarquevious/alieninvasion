import sys 
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # Initialize game and create a screen object. 
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    pygame.event.get()
    bg_color = (230,230,0)
    
    # Make a ship, group to store bullets, and a group of aliens. 
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()

    # Create a fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
       gf.check_events(ai_settings, screen, ship, bullets)
       ship.update()
       gf.update_bullets(bullets)
       gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()

if __name__ == '__main__':
    main()
