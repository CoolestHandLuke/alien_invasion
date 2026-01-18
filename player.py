import pygame
from bullet import Bullet

class Player(pygame.sprite.Sprite):

    def __init__(self, x_pos, y_pos):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/Player/player_b_m.png")
        self.rect = self.image.get_rect().move(x_pos, y_pos)
        self.width = self.rect.width
        self.height = self.rect.height
        self.time_since_last_shot = 0
        self.bullet_image = pygame.image.load("images/FX/vulcan_1.png")

    def get_surface(self):
        return self.image

    def get_rect(self):
        return self.rect
    
    def set_rect(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update_rect(self, dx, dy):
        self.rect = self.rect.move(dx, dy)

    def fire_bullet(self):
        return Bullet("images/FX/vulcan_1.png", self.rect.x + self.width / 2 - 4, self.rect.y, 0, 50, -1)