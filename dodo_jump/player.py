import pygame
import constants
from constants import Dir


class Player(pygame.sprite.Sprite):
    def __init__(
            self,
            position=constants.character_init_pos,
            filename=constants.character_image
    ):
        super().__init__()
        img = pygame.image.load(filename)
        self.image = pygame.Surface.convert_alpha(img)
        # self.image.fill(color)
        self.rect = self.image.get_rect(midbottom=position)
        self.group = pygame.sprite.GroupSingle()
        self.group.add(self)
        self.curr_velocity_y = 0
        self.x_dir = Dir.NONE
        self.prev_pos = pygame.Vector2(position)
        self.hasDied = False

        self.shootingActive = True
        self.isInvulnerable = False
        self.collisionsActive = True

    def equipPowerup(self):
        self.shootingActive = False
        self.isInvulnerable = True
        self.collisionsActive = False

    def removePowerup(self):
        self.shootingActive = True
        self.isInvulnerable = False
        self.collisionsActive = True

    def draw(self, screen):
        self.group.draw(screen)

    def canShoot(self):
        return self.shootingActive

    def checkCollisions(self, obj_manager):
        if not self.collisionsActive:
            return
        hits = pygame.sprite.groupcollide(obj_manager.group, self.group, False, False)
        for hit in hits:
            prev_rect = self.image.get_rect(midbottom=self.prev_pos)
            if self.curr_velocity_y >= 0 and hit.rect.midright[1] >= prev_rect.midbottom[1]:
                self.curr_velocity_y = -constants.jump_force
                hit.effect.applyEffectToPlayerOnTop(self)
            elif not prev_rect.colliderect(hit.rect):
                hit.effect.applyEffectToPlayerOnBottom(self)
            if hit.effect.disappear:
                obj_manager.remove(hit)

    # v = v0 + gt
    def moveY(self, dt, *, gravity=constants.gravity):
        self.prev_pos[1] = self.rect.midbottom[1]
        self.curr_velocity_y += gravity * dt
        self.rect.y += self.curr_velocity_y * dt

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
        if self.isInvulnerable:
            return
        self.hasDied = True
