import pygame
import constants
from enum import Enum


class Dir(Enum):
    LEFT = -1
    RIGHT = 1
    NONE = 0


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
        self.x_dir = Dir.NONE

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

    def changeInDir(self, dir, pygameEvent):
        if pygameEvent == pygame.KEYDOWN:
            self.x_dir = dir
        else:
            # we only care about the unpressing of the last button
            if dir == self.x_dir:
                self.x_dir = Dir.NONE

    def isDead(self):
        return self.rect.midtop[1] > constants.screen_size[1]

    def moveX(self, dt):
        self.rect.midbottom = (
        self.rect.midbottom[0] + self.x_dir.value * constants.character_x_vel * dt, self.rect.midbottom[1])
        if self.rect.midleft[0] > constants.screen_size[0]:
            self.rect.midbottom = (0, self.rect.midbottom[1])
        if self.rect.midright[0] < 0:
            self.rect.midbottom = (constants.screen_size[0], self.rect.midbottom[1])
