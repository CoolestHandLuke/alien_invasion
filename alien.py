import pygame

class Alien(pygame.sprite.Sprite):


    def __init__(self, x_pos, y_pos):

        pygame.sprite.Sprite.__init__(self)


        self.image = pygame.image.load("images/Aliens/enemy_1_r_m.png")
        self.rect = self.image.get_rect().move(x_pos, y_pos)