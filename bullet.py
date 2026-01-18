import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, image_name, initial_x_pos, initial_y_pos, x_speed, y_speed, direction):

        pygame.sprite.Sprite.__init__(self)

        # Additonal attributes are: Size, damage, speed, color?
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect().move(initial_x_pos, initial_y_pos)
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.direction = direction
        self.damage = 50

    def get_rect(self):
        return self.rect
    
    def get_damage(self):
        return self.damage
        
    def update_rect(self):
        dx = self.x_speed * self.direction
        dy = self.y_speed * self.direction
        self.rect = self.rect.move(dx, dy)
        