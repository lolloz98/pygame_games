import pygame
import constants


class Player(pygame.sprite.Sprite):
    def __init__(
            self,
            position=constants.character_init_pos,
            dimensions=constants.character_size,
            color=constants.character_color
    ):
        super().__init__()
        self.image = pygame.Surface(dimensions)
        self.image.fill(color)
        self.rect = self.image.get_rect(midbottom=position)
        self.group = pygame.sprite.GroupSingle()
        self.group.add(self)
        self.curr_velocity_y = 0

    def draw(self, screen):
        self.group.draw(screen)

    # v = v0 + gt
    def moveY(self, dt, collider_group, *, gravity=constants.gravity):
        self.curr_velocity_y += gravity * dt
        hits = pygame.sprite.groupcollide(collider_group, self.group, False, False)

        # only one tile max in hits
        if hits and self.curr_velocity_y >= 0:
            for hit in hits:
                self.rect.midbottom = (self.rect.midbottom[0], hit.rect.y)
                self.curr_velocity_y = -constants.jump_force
        else:
            self.rect.y += self.curr_velocity_y * dt
