import player
import constants
import pygame


class Effect:
    def applyEffectToPlayerOnBottom(self, character: player.Player):
        pass

    def applyEffectToPlayerOnTop(self, character: player.Player):
        pass

    def applyEffectToTile(self, obj, dt):
        pass


class MoveXEffect(Effect):
    def applyEffectToTile(self, obj, dt):
        obj.move(pygame.Vector2(constants.moving_tile_vel[0], 0), dt)
        if obj.rect.midleft[0] > constants.screen_size[0]:
            obj.rect.midbottom = (0, obj.rect.midbottom[1])
        if obj.rect.midright[0] < 0:
            obj.rect.midbottom = (constants.screen_size[0], obj.midbottom[1])


class MoveBackAndForth(Effect):
    def __init__(self, vel=constants.moving_tile_vel, stop=(200, 200), init_dir=(1, -1)):
        self.dir = pygame.Vector2(init_dir)
        self.velocity = pygame.Vector2(vel)
        self.stop = pygame.Vector2(stop)
        self.moved = pygame.Vector2(0, 0)

    def applyEffectToTile(self, obj, dt):
        movement = (self.dir.elementwise() * self.velocity).elementwise() * dt
        self.moved += movement.elementwise()
        obj.move(movement)

        def back_on_stop(m, s):
            if m < -s:
                return -s + 0.01
            if m > s:
                return s - 0.01
            return m

        if obj.rect.midright[0] > constants.screen_size[0] \
                or obj.rect.midleft[0] < 0 \
                or abs(self.moved.x) > self.stop.x:
            self.dir.x = -self.dir.x
            self.moved.x = back_on_stop(self.moved.x, self.stop.x)
        if abs(self.moved.y) > self.stop.y:
            self.dir.y = -self.dir.y
            self.moved.y = back_on_stop(self.moved.y, self.stop.y)


def moveBackAndForthX(vel=constants.moving_tile_vel[0], stop=(200, 200)):
    return MoveBackAndForth((vel, 0), stop)


def moveBackAndForthY(vel=constants.moving_tile_vel[1], stop=(200, 200)):
    return MoveBackAndForth((0, vel), stop)


class JumpHighEffect(Effect):
    def __init__(self, jump=constants.jump_force):
        self.jump = jump

    def applyEffectToPlayerOnTop(self, character: player.Player):
        character.curr_velocity_y -= self.jump


class BasicEnemy(Effect):
    def applyEffectToPlayerOnBottom(self, character: player.Player):
        character.die()

