# ----------------------------------------------------
# Программист: Илья Филатов
# Версия: 1.0
# Последнее обновление: 19.11.2018
# Файл: cyber_punk.py
# ----------------------------------------------------

import random
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
gun_x = 312
gun_y = 300
score = 0
level = 1
# Шаг перемещения пистолета
step = 25
# fon = 240, 240, 250
x_pos = gun_x
y_pos = gun_y
flag = 1
# flag - переменная ,маркер выхода
gun = 'left'
screen = display.set_mode((x_scr, y_scr))
# Создаем окно разрешением xscr х yscr
background = image.load('/Users/ilafilatov/Desktop/Project_X/data/background-2.jpg')
screen.blit(background, (0, 0))
# грузим фоновый рисунок и помещаем его на screen
key.set_repeat()



def boom():
    # звук выстрела
    file = os.path.join('data', '/Users/ilafilatov/Documents/data/vistrel.wav')
    sound = mixer.Sound(file)
    sound.play()

class Sprite:
    def __init__(self, gun_x, gun_y, filename):
        self.x = gun_x
        self.y = gun_y
        pik = image.load(filename)
        pik = pik.convert()
        self.bitmap = pik
        self.bitmap.set_colorkey((0, 0, 0))

    def set(self, xpos, ypos):
        # установить спрайт по координатам
        self.x = xpos
        self.y = ypos

    def render(self):
        # отрисовать спрайт
        screen.blit(self.bitmap, (self.x, self.y))


# ------------------------------------------------------------
pstr1 = Sprite(gun_x, gun_y,
               '/Users/ilafilatov/Desktop/Project_X/data/cyber_right.png')
pstr2 = Sprite(gun_x, gun_y,
               '/Users/ilafilatov/Desktop/Project_X/data/cyber_right.png')
pstr3 = Sprite(gun_x, gun_y,
               '/Users/ilafilatov/Desktop/Project_X/data/cyber_right.png')
pstl1 = Sprite(gun_x, gun_y,
               '/Users/ilafilatov/Desktop/Project_X/data/cyber_left.png')
pstl2 = Sprite(gun_x, gun_y,
               '/Users/ilafilatov/Desktop/Project_X/data/cyber_left.png')
pstl3 = Sprite(gun_x, gun_y,
               '/Users/ilafilatov/Desktop/Project_X/data/cyber_left.png')


# это спрайты пистолета

# --------------------------------------------------------------

class Pistol(Sprite):
    def __init__(self, gun_x, gun_y, naprav):
        global pst1, pst2, pst3
        self.x = gun_x
        self.y = gun_y
        if naprav == 'right':
            # Дуло смотрит вправо
            pst1 = pstr1
            pst2 = pstr2
            pst3 = pstr3
            pst1 = Sprite.__init__(self, gun_x, gun_y,
                                   '/Users/ilafilatov/Desktop/Project_X/data/cyber_right.png')
        else:
            # Дуло смотрит влево
            pst1 = pstl1
            pst2 = pstl2
            pst3 = pstl3
            pst1 = Sprite.__init__(self, gun_x, gun_y,
                                   '/Users/ilafilatov/Desktop/Project_X/data/cyber_left.png')
        # в зависимости от 'naprav

    def put(self, gun_x, gun_y):
        # установить по координатам
        self.x = gun_x
        self.y = gun_y
        self.render()


# ----------------------------------------------------------------
class Vrag(Sprite):
    def __init__(self, gun_x, gun_y, naprav):
        global vrg
        self.x = gun_x
        self.y = gun_y
        if naprav == 'left':
            vrg = Sprite.__init__(self, gun_x, gun_y,
                                  '/Users/ilafilatov/Desktop/Project_X/data/putin.png')
        else:

            vrg = Sprite.__init__(self, gun_x, gun_y,
                                  '/Users/ilafilatov/Desktop/Project_X/data/putin.png')

    def put(self, gun_x, gun_y):
        # отрисовываем противника
        global flag
        if 0 < gun_x < pr + 1:
            # проверка на границы окна,если ботинок в пределах границ он отрисовывается.
            self.x = gun_x
            self.y = gun_y
            self.render()
            # Проверка достижения середины
            if (flag > 0) and (182 < gun_x < 500):
                flag = 0


# -------------------------------------------------------------------
def bah(gun_x, gun_y):
    # процедура выстрела
    global vlx, vly, score
    pst2.set(gun_x, gun_y)
    pst2.render()
    for i in range(6):
        vlx[i] = vlx[i] + 1
        vrx[i] = vrx[i] - 1
        vrgl[i].put(vlx[i], vly[i])
        vrgr[i].put(vrx[i], vry[i])
        if 0 < vlx[i]:
            if (dulo == 'left') and ((vly[i] - 20) < gun_y < (vly[i] + 60)):
                score = score + 1
                vlx[i] = - random.randrange(50, 300, 25)
        if vrx[i] < pr:
            if (dulo == 'right') and ((vry[i] - 20) < gun_y < (vry[i] + 60)):
                score = score + 1
                vrx[i] = pr + random.randrange(50, 300, 25)
    # проверка поподания в противника в цикле если дуло влево проверяются правые/ вправо левые
    # при выстреле все противники все равно смещаются на пиксел к центру
    # это защита от постоянно нажатого пробела
    # вместо убитого противника за пределами экрана генерируется новый по случайному X.
    display.update()
    pst3.set(gun_x, gun_y)
    pst3.render()
    boom()
    # звук выстрела
    display.update()


# -------------------------------------------------------------------
while 1:
    # основной цикл программы
    score = 0
    # счет
    level = 1
    # уровень
    flag = 1
    # эта переменная предназначена для выхода из циклов при flag=0
    speed = 1
    dulo = 'left'

    gun_x = 312
    gun_y = 300
    # Координаты пистолета
    # -----------------------------------------------
    vlx = [0, -200, 0, -400, -150, 0]
    vly = vry = [100, 200, 300, 400, 500, 600]
    pr = x_scr - 118
    vrx = [pr + 100, pr, pr + 300, pr, pr + 200, pr]
    # начальные координаты 6-ти противников
    vrgl = []
    vrgr = []
    # создаем 2  списка для противников справа и слева
    for i in range(6):
        # заполняем списки в цикле
        vrgl.append(Vrag(vlx[i], vly[i], 'left'))
        vrgr.append(Vrag(vrx[i], vry[i], 'right'))

    pest = Pistol(gun_x, gun_y, dulo)
    # определяем пистолет(дуло вправо/влево)
    screen.blit(background, (0, 0))
    pest.put(gun_x, gun_y)
    display.flip()
    # заливаем экран обоями, ставим пистолет по координатам и отрисовываем все это на дисплее
    # --------------------------------------------------------------------------------------------------------------------
    while 1:
        # основной цикл игры
        for i in range(6):
            # смещение всех противников на пиксел к центру и их отрисовка
            vlx[i] = vlx[i] + 1
            vrx[i] = vrx[i] - 1
            vrgl[i].put(vlx[i], vly[i])
            vrgr[i].put(vrx[i], vry[i])
        pest.put(gun_x, gun_y)
        # устанавливаем пистолет
        display.flip()
        screen.blit(background, (0, 0))
        Font = font.Font(None, 32)
        rez = score // 100
        # rez  = счет нацело поделить на сто
        level = 1 + rez
        # уровень до 100 очков 1-ый, дальше за каждые 100 добавляется 1
        textimg = Font.render(str(level), 1, (255, 0, 0), (0, 255, 255))
        screen.blit(textimg, (700, 9))
        # печатаем уровень
        textimg = Font.render(str(score), 1, (255, 0, 0), (0, 255, 255))
        screen.blit(textimg, (500, 9))
        # печатаем счет(кол-во убитых ботинок)
        if flag == 0:
            break
        # выход из основного игрового цикла
        for event in pygame.event.get():
            # опрос клавиатуры, мыши
            if event.type == QUIT:
                sys.exit()
            # выход по нажатию креста на рамке окна
            if event.type == KEYDOWN:
                # если нажата клавиша то

                if event.key == K_ESCAPE:
                    flag = 0
                # по esc выход из игрового цикла через установку flag в  0
                if event.key == K_DOWN:
                    gun_y = gun_y + step
                    if gun_y >= (y_scr - 100):
                        gun_y = gun_y - step
                # перемещение пистолета вниз если не достигнута нижняя граница
                if event.key == K_UP:
                    gun_y = gun_y - step
                    if gun_y <= 0:
                        gun_y = gun_y + step
                    # перемещение пистолета вверх если не достигнута верхняя граница
                if event.key == K_LEFT:
                    dulo = 'left'
                    pest.__init__(gun_x, gun_y, 'left')
                # дуло влево
                if event.key == K_RIGHT:
                    dulo = 'right'
                    pest.__init__(gun_x, gun_y, dulo)
                # дуло вправо
                if event.key == K_SPACE:
                    bah(gun_x, gun_y)
            # выстрел
    # -------------------------конец основного цикла--------------------------------
    flag = 1
    boom()
    boom()
    boom()
    # большой бум символизирующий конец игры !
    Font = font.Font(None, 72)
    # определяем фонт
    textimg = Font.render('                               ', 1, (0, 255, 255),
                          (255, 0, 0))
    screen.blit(textimg, (180, 250))
    textimg = Font.render('  GAME  OVER  !!! ', 1, (0, 255, 255), (255, 0, 0))
    screen.blit(textimg, (180, 300))
    textimg = Font.render('                               ', 1, (0, 255, 255),
                          (255, 0, 0))
    screen.blit(textimg, (180, 350))
    Font = font.Font(None, 36)
    textimg = Font.render(
        '-----------------------------------------------------', 1,
        (0, 255, 255), (255, 0, 0))
    screen.blit(textimg, (180, 575))

    textimg = Font.render('    Space - New Game     Esc - Exit    ', 1,
                          (0, 255, 255), (255, 0, 0))
    screen.blit(textimg, (180, 600))
    textimg = Font.render(
        '-----------------------------------------------------', 1,
        (0, 255, 255), (255, 0, 0))
    screen.blit(textimg, (180, 625))
    display.flip()
    # пишем на экране Game Over и прочую инфу
    while 1:
        # этот цикл на окончание программы
        for event in pygame.event.get():

            if event.type == QUIT:
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    flag = 0
                # по Space выход из внутреннего цикла через break
                if event.key == K_ESCAPE:
                    sys.exit()
                # по Esc выходим из программы
        if flag == 0:
            break
        # по break мы выходим из этого цикла и попадаем в начало основного цикла программы

