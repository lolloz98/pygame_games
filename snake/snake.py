import pygame


class Snake:
    def __init__(self, x=200, y=100, w=20, h=20):
        self.parts = [Head(x, y, w, h)]
        self.head = pygame.sprite.GroupSingle()
        self.head.add(self.parts[0])
        self.body = pygame.sprite.Group()
        self.speed = w
        self.motion = (0, 0)
        self.appliedMotion = (0, 0)
        self.needToAdd = False

    def changeMotionToUp(self):
        if self.appliedMotion[1] <= 0:
            self.motion = (0, -self.speed)

    def changeMotionToDown(self):
        if self.appliedMotion[1] >= 0:
            self.motion = (0, self.speed)

    def changeMotionToLeft(self):
        if self.appliedMotion[0] <= 0:
            self.motion = (-self.speed, 0)

    def changeMotionToRight(self):
        if self.appliedMotion[0] >= 0:
            self.motion = (self.speed, 0)

    def setNeedToAdd(self):
        self.needToAdd = True

    def applyAdd(self):
        if self.needToAdd:
            self.parts.append(
                Body(
                    self.parts[-1].rect.x - self.appliedMotion[0],
                    self.parts[-1].rect.y - self.appliedMotion[1]
                )
            )
            self.body.add(self.parts[-1])
            self.needToAdd = False

    def applyMotion(self, max_x, max_y):
        x, y = self.motion
        if x == y and y == 0:
            return
        ix = self.parts[0].rect.x
        iy = self.parts[0].rect.y
        px = ix
        py = iy
        for i in range(1, len(self.parts)):
            self.parts[i].rect.x, px = px, self.parts[i].rect.x
            self.parts[i].rect.y, py = py, self.parts[i].rect.y
        self.parts[0].rect.x = (ix + x) % max_x
        self.parts[0].rect.y = (iy + y) % max_y
        self.appliedMotion = self.motion

    def draw(self, screen):
        self.head.draw(screen)
        self.body.draw(screen)


class Head(pygame.sprite.Sprite):
    def __init__(self, x=200, y=100, w=20, h=20):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill('#00FF00')
        self.rect = self.image.get_rect(topleft=(x, y))


class Body(pygame.sprite.Sprite):
    def __init__(self, x, y, w=20, h=20):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill('#00A000')
        self.rect = self.image.get_rect(topleft=(x, y))
