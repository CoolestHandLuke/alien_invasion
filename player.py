import pygame
from bullet import Bullet

class Player(pygame.sprite.Sprite):

    def __init__(self, x_pos, y_pos):

        pygame.sprite.Sprite.__init__(self)

        self.image_options = ["player_b_l1.png", "player_b_l2.png", "player_b_m.png", "player_b_r2.png", "player_b_r1.png"]
        self.image_tracker = 2
        self.image_options_length = len(self.image_options)
        self.image = pygame.image.load("images/Player/" + self.image_options[self.image_tracker])  # Default position is the middle, no lean
        self.rect = self.image.get_rect().move(x_pos, y_pos)
        self.width = self.rect.width
        self.height = self.rect.height
        self.time_since_last_shot = 0
        self.bullet_name = 'plasma'
        self.bullet_size = "01"
        self.shooting_speed = 0.1

    def get_image(self):
        return self.image
    
    def set_image(self, direction, player_idle):
        if player_idle and self.image_tracker == 2:
            return
        new_image_tracker = self.image_tracker + direction
        if new_image_tracker >= 0 and new_image_tracker < self.image_options_length:
            self.image_tracker = new_image_tracker
            self.image = pygame.image.load("images/Player/" + self.image_options[self.image_tracker])

    def get_rect(self):
        return self.rect
    
    def set_rect(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update_rect(self, dx, dy):
        self.rect = self.rect.move(dx, dy)

    def get_height(self):
        return self.rect.height

    def set_bullet_type(self, type):
        self.bullet_type = type

    def fire_bullet(self):
        image_name = "images/FX/" + self.bullet_name + self.bullet_size + ".png"
        return Bullet(image_name, self.rect.x + self.width / 2 - 4, self.rect.y, 0, 50, -1)
    
    def get_shooting_speed(self):
        return self.shooting_speed
    
    def set_shooting_speed(self, shooting_speed):
        self.shooting_speed = shooting_speed