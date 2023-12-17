import movable_sprite
import pygame
import constants


class Projectile(movable_sprite.MovableSprite):
    def __init__(
            self,
            position
    ):
        super().__init__(position, filename=constants.projectile)
        self.rect = self.image.get_rect(midbottom=position)

    def move_with_respect_to_player(self, player_y_vel, dt=1):
        self.move((0, min(player_y_vel, constants.projectile_y_vel)), dt)


class ProjectileManager:
    def __init__(self):
        self.projs = []
        self.group = pygame.sprite.Group()

    def addProj(self, player):
        p = Projectile(player.rect.midtop)
        self.projs.append(p)
        self.group.add(p)

    def removeProj(self, p):
        self.projs.remove(p)
        self.group.remove(p)

    def draw(self, screen):
        self.group.draw(screen)

    def moveProj(self, char_y_velocity, dt):
        for p in self.projs:
            p.move_with_respect_to_player(char_y_velocity, dt)
        for p in self.projs:
            if p.rect.midbottom[1] < -20:
                self.removeProj(p)

    def checkCollision(self, movable_obj_manager):
        toRem = []
        hits = pygame.sprite.groupcollide(movable_obj_manager.group, self.group, False, False)
        for hit in hits:
            print("here", hits[hit])
            remProj = hit.effect.onProjectileHitIsProjConsumed(hit, movable_obj_manager)
            if remProj:
                toRem.append(hits[hit])
        for pL in toRem:
            for p in pL:
                self.removeProj(p)
