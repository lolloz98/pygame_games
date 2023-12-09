import pygame


class Food(pygame.sprite.Sprite):
    def __init__(self, w=20, h=20, x=200, y=100):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill('#FF0000')
        self.rect = self.image.get_rect(topleft=(x, y))


