# ----------------------------------------------------
# Программист: Илья Филатов
# Версия: 1.0
# Последнее обновление: 19.11.2018
# Файл: cyber_punk.py
# ----------------------------------------------------

<<<<<<< HEAD
=======

>>>>>>> 377502196e9e480f526621d5e93e15051aab7476
import os.path
from pygame import *
import pygame.time

mixer = pygame.mixer
time = pygame.time
Font = None
init()
# Размер окна
x_scr = 800
y_scr = 800
# Координаты пистолета
zx = 312
zy = 300
score = 0
level = 1
# Шаг перемещения пистолета
step = 25
# fon = 240, 240, 250
x_pos = zx
y_pos = zy
flag = 1
# flag - переменная ,маркер выхода
temp = 100
# задержка 100=0,1секунды
gun = 'left'
screen = display.set_mode((x_scr, y_scr))
# Создаем окно разрешением xscr х yscr
background = image.load('/Users/ilafilatov/Desktop/Project_X/data/background-2.jpg')
screen.blit(background, (0, 0))
# грузим фоновый рисунок и помещаем его на screen
key.set_repeat()


# Уменьшаем время отклика клавиатуры

def boom():
    # звук выстрела
    file = os.path.join('data', '/Users/ilafilatov/Documents/data/vistrel.wav')
    sound = mixer.Sound(file)
    sound.play()
