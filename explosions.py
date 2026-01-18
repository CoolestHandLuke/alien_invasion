import pygame

class Explosion(pygame.sprite.Sprite):

    def __init__(self, x_pos, y_pos):

        pygame.sprite.Sprite.__init__(self)

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.exp_index = 0
        self.explosions_list = ["images/Explosions/explosion_1_01.png", 
                                "images/Explosions/explosion_1_02.png",
                                "images/Explosions/explosion_1_03.png",
                                "images/Explosions/explosion_1_04.png",
                                "images/Explosions/explosion_1_05.png",
                                "images/Explosions/explosion_1_06.png",
                                "images/Explosions/explosion_1_07.png",
                                "images/Explosions/explosion_1_08.png",
                                "images/Explosions/explosion_1_09.png",
                                "images/Explosions/explosion_1_10.png",
                                "images/Explosions/explosion_1_11.png"]
        self.image = pygame.image.load(self.explosions_list[self.exp_index])
        self.rect = self.image.get_rect().move(self.x_pos, self.y_pos)
    
    def update_image(self):
        self.exp_index += 1
        if self.exp_index < len(self.explosions_list):
            self.image = pygame.image.load(self.explosions_list[self.exp_index])
            return True
        return False
