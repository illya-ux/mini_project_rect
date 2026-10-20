import pygame
import datetime
from classes import *
from settings import *


pygame.init()

hero = Rectengle()

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

    pygame.display.update()
    clock.tick(FPS)

hero.save_pos(PATH + "save.txt")
