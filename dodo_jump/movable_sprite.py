import pygame
import constants
import effects


class MovableSprite(pygame.sprite.Sprite):
    def __init__(
            self,
            position,
            effect=effects.Effect(),
            dimensions=constants.tile_basic_size,
            color=constants.tile_basic_color
    ):
        super().__init__()
        self.image = pygame.Surface(dimensions)
        self.rect = self.image.get_rect(midtop=position)
        self.effect = effect
        self.image.fill(color)
        self.effect.init_pos = pygame.Vector2(position)

    def move(self, direction, dt=1):
        # For sure there is a better way to handle movement...
        # For now it's good enough :)
        self.rect.midbottom = (
            self.rect.midbottom[0] + direction[0] * dt,
            self.rect.midbottom[1] + direction[1] * dt
        )