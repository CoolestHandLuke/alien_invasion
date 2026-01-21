import pygame

class Alien(pygame.sprite.Sprite):


    def __init__(self, alien_type, x_pos, y_pos, move_direction):

        pygame.sprite.Sprite.__init__(self)


        self.image = pygame.image.load(alien_type["image"])
        self.rect = self.image.get_rect().move(x_pos, y_pos)
        self.speed = alien_type["speed"]
        self.direction = move_direction
        self.health = alien_type["health"]

    def update_health(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.kill()

    def get_rect(self):
        return self.rect
    
    def move(self):
        dy = 0
        dx = self.speed * self.direction
        if self.rect.x <= 0 or pygame.display.get_window_size()[0] <= (dx + self.rect.width + self.rect.x):
            self.direction = -self.direction
            dx = -dx
            dy = self.rect.height * 1.25
        self.rect = self.rect.move(dx, dy)