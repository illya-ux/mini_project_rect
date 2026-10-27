import pygame
import datetime
from classes import *
from settings import *


pygame.init()

hero = Rectengle()

npc = NPC()

enemes = []

for i in range(2):
    enemy = NPC(3, i * 100 + 600, i * 100 + 200, (255, 0, 0), 100, 100)
    enemes.append(enemy)


def load_object(obj, filename):
    try:
        obj.load_pos(PATH + filename)
    except:
        with open(PATH + "log.txt", "a", encoding="utf-8") as file:
            current_time = str(datetime.datetime.now())
            file.write(
                current_time
                + " "
                + __file__
                + " ошибка работы с файлами "
                + filename
                + "\n"
            )


load_object(hero, "save.txt")
load_object(npc, "save_npc.txt")

for i in range(len(enemes)):
    load_object(enemes[i], "save_enemy_" + str(i) + ".txt")


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

    npc.update()
    for enemy in enemes:
        enemy.update()

    screen.fill(SCREEN_COLOR)

    hero.draw()

    npc.draw()

    for enemy in enemes:
        enemy.draw()

    pygame.display.update()
    clock.tick(FPS)

hero.save_pos(PATH + "save.txt")
npc.save_pos(PATH + "save_npc.txt")

for i in range(len(enemes)):
    enemes[i].save_pos(PATH + "save_enemy_" + str(i) + ".txt")

pygame.quit()
