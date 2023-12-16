import pygame
import constants
from constants import Dir


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
        self.prev_pos = pygame.Vector2(position)
        self.hasDied = False

    def draw(self, screen):
        self.group.draw(screen)

    # v = v0 + gt
    def moveY(self, dt, collider_group, *, gravity=constants.gravity):
        hits = pygame.sprite.groupcollide(collider_group, self.group, False, False)

        def actuallyMoveY():
            self.prev_pos[1] = self.rect.midbottom[1]
            self.curr_velocity_y += gravity * dt
            self.rect.y += self.curr_velocity_y * dt
        if not hits:
            actuallyMoveY()
            return

        # only one object max in hits
        if self.curr_velocity_y >= 0:
            for hit in hits:
                # act only if prev was below player and was not already hit
                prev_pos_rect = self.image.get_rect(midbottom=self.prev_pos)

                if not prev_pos_rect.colliderect(hit.rect):
                    if self.rect.midbottom[1] > hit.rect.midbottom[1]:
                        hit.effect.applyEffectToPlayerOnBottom(self)
                        return
                    # self.rect.midbottom = (self.rect.midbottom[0], hit.rect.y)
                    self.curr_velocity_y = -constants.jump_force
                    hit.effect.applyEffectToPlayerOnTop(self)
        else:
            for hit in hits:
                if self.rect.midbottom[1] > hit.rect.midbottom[1]:
                    hit.effect.applyEffectToPlayerOnBottom(self)

        actuallyMoveY()

    def changeInDir(self, dir, pygameEvent):
        if pygameEvent == pygame.KEYDOWN:
            self.x_dir = dir
        else:
            # we only care about the unpressing of the last button
            if dir == self.x_dir:
                self.x_dir = Dir.NONE

    def isDead(self):
        return self.hasDied or self.rect.midtop[1] > constants.screen_size[1]

    def moveX(self, dt):
        self.prev_pos[0] = self.rect.midbottom[0]
        # For sure there is a better way to handle movement...
        # For now it's good enough :)
        self.rect.midbottom = (
        self.rect.midbottom[0] + self.x_dir.value * constants.character_x_vel * dt, self.rect.midbottom[1])
        if self.rect.midleft[0] > constants.screen_size[0]:
            self.rect.midbottom = (0, self.rect.midbottom[1])
        if self.rect.midright[0] < 0:
            self.rect.midbottom = (constants.screen_size[0], self.rect.midbottom[1])

    def die(self):
        self.hasDied = True
