import pygame, random
class Exhaust(pygame.sprite.Sprite):

    def __init__(self, x_pos, y_pos):

        pygame.sprite.Sprite.__init__(self)

        self.image_options = ["exhaust01.png", "exhaust02.png", "exhaust03.png", "exhaust04.png", "exhaust05.png"]
        self.image_options_length = len(self.image_options)
        self.image = pygame.image.load("images/FX/" + self.image_options[2])  # Just start with the middle one
        self.rect = self.image.get_rect().move(x_pos, y_pos)


    def set_image(self):
        self.image = pygame.image.load("images/FX/" + self.image_options[random.randint(0, self.image_options_length - 1)])
        # TODO: Updat the location with the rect.
    

