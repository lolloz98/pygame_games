import player
import constants
import pygame


class Effect:
    def __init__(self):
        self.disappear = False

    def applyEffectToPlayerOnBottom(self, character: player.Player):
        pass

    def applyEffectToPlayerOnTop(self, character: player.Player):
        pass

    def applyEffectToTile(self, obj, dt):
        pass

    def onProjectileHitIsProjConsumed(self, obj, obj_manager):
        return False

    def applyEachFrame(self, obj, character: player.Player, dt):
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
        super().__init__()
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
        super().__init__()
        self.jump = jump

    def applyEffectToPlayerOnTop(self, character: player.Player):
        character.curr_velocity_y -= self.jump


class DisappearingObj(Effect):
    def applyEffectToPlayerOnTop(self, character: player.Player):
        self.disappear = True


class BasicEnemy(DisappearingObj):
    def applyEffectToPlayerOnBottom(self, character: player.Player):
        character.die()

    def onProjectileHitIsProjConsumed(self, obj, obj_manager):
        obj_manager.remove(obj)
        return True


class WindPowerup(Effect):
    def __init__(
            self,
            active_player_vel_y=constants.wings_y_vel,
            active_image_file_name=constants.wings_active,
            ttl=constants.wings_ttl
    ):
        super().__init__()
        self.active = False
        self.swapped_imgs = False
        self.ttl = ttl
        self.active_player_vel_y = active_player_vel_y
        self.active_img = pygame.Surface.convert_alpha(pygame.image.load(active_image_file_name))

    def applyEffectToPlayerOnBottom(self, character: player.Player):
        self.onCollision(character)

    def applyEffectToPlayerOnTop(self, character: player.Player):
        self.onCollision(character)

    def onCollision(self, character: player.Player):
        self.active = True
        character.equipPowerup()

    def applyEachFrame(self, obj, character: player.Player, dt):
        if not self.active:
            return
        if not self.swapped_imgs:
            self.swapped_imgs = True
            obj.image = self.active_img
            obj.rect = self.active_img.get_rect(midbottom=character.rect.midbottom)

        self.ttl -= dt
        obj.rect.midbottom = character.rect.midbottom
        character.curr_velocity_y = self.active_player_vel_y
        if self.ttl < 0:
            self.active = False
            self.disappear = True
            character.removePowerup()
