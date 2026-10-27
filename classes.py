import pygame
from settings import *


pygame.init()

# ----------------- eкран -----------------
screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))


class Rectengle:
    def __init__(self, speed_rect=5, x=700, y=400, color=(0, 0, 0), width=80, heigh=80):
        self._rect = pygame.Rect(x, y, width, heigh)
        self.color = color
        self.speed_rect = speed_rect

    def save_pos(self, save_position):
        with open(save_position, "w", encoding="utf-8") as file:
            file.write(str(self._rect.x) + "\n")
            file.write(str(self._rect.y) + "\n")

    def load_pos(self, load_position):
        with open(load_position, "r", encoding="utf-8") as file:
            self._rect.x = int(file.readline())
            self._rect.y = int(file.readline())

    def go_left(self):
        self._rect.x -= self.speed_rect
        if self._rect.x < 0:
            self._rect.x = 0

    def go_right(self):
        self._rect.x += self.speed_rect

    def go_duwn(self):
        self._rect.y += self.speed_rect

    def go_up(self):
        self._rect.y -= self.speed_rect
        if self._rect.y < 0:
            self._rect.y = 0

    def update(self, keys):
        keys = keys

        if keys[pygame.K_a]:
            self.go_left()
        if keys[pygame.K_d]:
            self.go_right()
        if keys[pygame.K_w]:
            self.go_up()
        if keys[pygame.K_s]:
            self.go_duwn()

    def draw(self):
        pygame.draw.rect(screen, self.color, self._rect)


class NPC(Rectengle):
    def __init__(
        self, speed_rect=3, x=500, y=600, color=(0, 0, 255), width=90, heigh=90
    ):
        super().__init__(speed_rect, x, y, color, width, heigh)
        self.direction = DIR_RIGHT

    def update(self):
        old_pos = self._rect.copy()

        if self.direction == DIR_RIGHT:
            self.go_right()
        else:
            self.go_left()

        if self._rect.x <= 0 or self._rect.right >= SCREEN_WIDHT:
            self._rect = old_pos
            self.direction *= DIR_LEFT
