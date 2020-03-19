import pygame
from pygame.sprite import Sprite # What is going on here?

class Bullet(Sprite):
    """A class to manage the bullets fired from the ship"""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship's current position"""
        super(Bullet, self).__init__() # What is going on here?
        self.screen = screen

        # Create a bullet rec at (0,0) and then set correct postion.
        self.rect = pygame.Rect(0,0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx # Explain centerx
        self.rect.top = ship.rect.top

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

        # Set color of bullet.
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen"""
        # Update the decimal position on the bullet.
        self.y -= self.speed_factor

        # Update the rec position.
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

        
