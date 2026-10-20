import pygame
import datetime
from classes import *
from settings import *


pygame.init()

hero = Rectengle()

npc = Rectengle(3, 500, 600, (0, 0, 255), 90, 90)

enemes = []

for i in range(2):
    enemy = Rectengle(3, i * 100 + 600, i * 100 + 200, (255, 0, 0), 100, 100)
    enemes.append(enemy)

try:
    hero.load_pos(PATH + "save.txt")
except:
    with open(PATH + "log.txt", "a", encoding="utf-8") as file:
        current_time = str(datetime.datetime.now())
        file.write(current_time + " " + __file__ + " ошибка работы с файлами\n")


clock = pygame.time.Clock()

game = True

while game:
    for event in pygame.event.get():
        if (
            event.type == pygame.QUIT
            or event.type == pygame.KEYDOWN
            and event.key == pygame.K_q
        ):
            game = False
    keys = pygame.key.get_pressed()
    hero.update(keys)

    screen.fill(SCREEN_COLOR)

    hero.draw()

    npc.draw()

    for enemy in enemes:
        enemy.draw()

    pygame.display.update()
    clock.tick(FPS)

hero.save_pos(PATH + "save.txt")
