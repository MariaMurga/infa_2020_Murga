import pygame
import math 
from random import choice
from random import randint

pygame.font.init()

pygame.init()
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

FPS = 30
g = 1
Tick = FPS

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, BLACK, WHITE, GREY]

font1 = pygame.font.Font(None, 50)

pool_bullet = [] # массив снярядов (своих)
pool_ball = [] # массив целей (1lvl)
pool_enemy = [] # массив бомб (2lvl)

score = 0 


def barrel(x, y, a, b, an, screen, color):
    '''
    отрисовывает прямоугольный ствол пушки.
    учитывает угол поворота an ствола
    '''
    cos = math.cos(an)
    sin = math.sin(an)
    pygame.draw.polygon(screen, color, [(x, y), (x + a*cos, y - a*sin),
                                        (x + a*cos - b*sin, y - a*sin - b*cos),
                                        (x - b*sin, y - b*cos)])

'''def new_ball(vx, vy, x, y, color, time):
    
    создаёт новую цель-шарик
   
    ball = Ball(vx, vy, x, y, color, time)
    Targets1.append(ball)
    
def new_bullet(vx, vy, x, y, color, time):
    
    создаёт новый снаряд пушки
   
    bullet = Bomb(vx, vy, x, y, color, time)
    Bullets.append(bullet)
    
def new_bomb(x, y):
    
    создаёт новую бомбу,
    когда её сбрасывает самолёт
   
    bomb = Bomb(randint(-5, 5), 0, x, y, GREEN, 500)
    Targets2.append(bomb)

def new_plane():
    
    создаёт самолёт
    
    plane = Plane(15, 0, randint(0, WIDTH), randint(50, 150), BLUE, 999)
    Targets2.append(plane)'''


class Gun:

    def __init__(self):
        '''
        инициализация пушки
        x, y -- координаты нижней вершины ствола
        an -- угол наклона ствола
        f2_power -- заряд пушки
        on -- равняется 1 при зарядке пушки
           -- равняется 0 при бездействии пушки
        live -- жизни пушки (и игрока)
        w, a, s, d -- движение танка
        '''

        self.x = 20
        self.y = 450
        self.an = 1
        self.f2_power = 10
        self.on = 0
        self.live = 3

        self.w = 0
        self.a = 0
        self.s = 0
        self.d = 0

        self.color = BLACK

    '''def targetting(self, event):
        # прицеливает пушку по месту положения курсора

        if event:
            try:
                self.an = math.atan((self.y - event.pos[1]) / (event.pos[0] - self.x))
            except:
                ZeroDivisionError'''

    def draw(self, surface):
        # рисует танк

        pygame.draw.rect(screen, GREEN, (self.x - 20, self.y, 40, 20) )
        barrel(self.x, self.y, self.f2_power, 10, self.an, screen, self.color)

    '''def fire2_start(self):
         # начинает процесс зарядки

        self.on = 1
        self.color = RED

    def power_up(self):
        # продолжает процесс зарядки

        if (self.on and self.f2_power <= 100):
            self.f2_power += 2

    def fire2_end(self):
        # процесс зарядки оканчивается выстрелом,состояние пушки возвращается к исходному

        new_bullet(self.f2_power * math.cos(self.an), - self.f2_power * math.sin(self.an),
                 self.x, self.y, BLACK, 1000 )
        self.f2_power = 10
        self.color = GREY
        self.on = 0

    def move_up_start(self):
        # начинает двигать танк вверх при нажатии на w

        self.w = 1

    def move_down_start(self):
        # начинает двигать танк влево при нажатии на a

        self.a = 1

    def move_left_start(self):
        # начинает двигать танк вниз при нажатии на s

        self.s = 1

    def move_right_start(self):
        # начинает двигать танк вправо при нажатии на d

        self.d = 1

    def moving_up(self):
        # двигает танк вверх при нажатии на w

        if self.w:
            self.y -= 1

    def moving_down(self):
        # двигает танк влево при нажатии на а

        if self.a:
            self.x -= 1

    def moving_left(self):
        # двигает танк вниз при нажатии на s

        if self.s:
            self.y += 1

    def moving_right(self):
        # двигает танк вправо при нажатии на d

        if self.d:
            self.x += 1

    def move_up_stop(self):
        # прекращает движение по w

        self.w = 0

    def move_down_stop(self):
        # прекращает движение по a

        self.a = 0

    def move_left_stop(self):
        # прекращает движение по s

        self.s = 0

    def move_right_stop(self):
        # прекращает движение по d

        self.d = 0'''

class Ball:
    
    def __init__(self):
        # инициализация

        self.vx = randint(-5, 5)
        self.vy = randint(-5, 5)
        self.x = randint(WIDTH/2, WIDTH)
        self.y = randint(0, HEIGHT)
        self.r = 10
        self.color = RED
        self.time = 999
        self.death = 1 # параметр, обнуляющийся в случае смерти цели
        self.live = 3 # жизни цели

    def draw(self, surface):
        # рисует цель

        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def move(self):
        # описывает движение цели, в том числе соударения о стенки

        if (self.vx + self.x + self.r >= WIDTH):
            self.vx = - 0.8 * self.vx

        if (self.vx + self.x + self.r <= 0):
            self.vx = - 0.8 * self.vx

        if (self.vy + self.y + self.r >= HEIGHT):
            self.vy = - 0.8 * self.vy

        if (self.vy + self.y + self.r <= 0):
            self.vy = - self.vy

        self.x += self.vx
        self.y += self.vy

    '''def alive(self):
        # проверяет, жива ли цель

        if self.time > 0:
            self.time -= 1

        else:
            self.death = 1
            return self.death'''

    '''def hit_a_tank(self, x, y):
          # проверяет, попала ли цель в танк

        if ((self.x + self.r > x - 20 and self.x + self.r < x + 20) and
            (self.y + self.r > y and self.y + self.r < y + 20)):
            return True

        elif ((self.x + self.r > x - 20 and self.x + self.r < x + 20) and
              (self.y - self.r > y and self.y - self.r < y + 20)):
            return True

        elif ((self.x - self.r > x - 20 and self.x - self.r < x + 20) and
              (self.y + self.r > y and self.y + self.r < y + 20)):
            return True

        elif ((self.x - self.r > x - 20 and self.x - self.r < x + 20) and
              (self.y - self.r > y and self.y - self.r < y + 20)):
            return True

        else:
            return False'''
        

class Bomb:
    
    def __init__(self, vx, vy, x, y, color, time):
        # инициализация

        self.vx = vx
        self.vy = vy
        self.x = x
        self.y = y
        self.r = 10
        self.color = color
        self.time = time
        self.death = 1 # параметр, обнуляющийся в случае смерти цели
        self.live = 3 # жизни цели

    def draw(self, surface):
        # рисует цель

        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def move(self):
        # описывает движение цели

        self.x += self.vx
        self.y += self.vy
        self.vy += g

    def alive(self):
        # проверяет, жива ли цель

        if self.time > 0:
            self.time -= 1

        else:
            self.death = 1
            return self.death

    '''def hit_a_tank(self, x, y):
          # проверяет, попала ли цель в танк

        if ((self.x + self.r > x - 20 and self.x + self.r < x + 20) and
            (self.y + self.r > y and self.y + self.r < y + 20)):
            return True

        elif ((self.x + self.r > x - 20 and self.x + self.r < x + 20) and
              (self.y - self.r > y and self.y - self.r < y + 20)):
            return True

        elif ((self.x - self.r > x - 20 and self.x - self.r < x + 20) and
              (self.y + self.r > y and self.y + self.r < y + 20)):
            return True

        elif ((self.x - self.r > x - 20 and self.x - self.r < x + 20) and
              (self.y - self.r > y and self.y - self.r < y + 20)):
            return True

        else:
            return False'''



class Plane:
    def __init__(self, vx, vy, x, y, color, time):
        '''
        инициализация пушки
        x, y -- координаты нижней вершины ствола
        an -- угол наклона ствола
        f2_power -- заряд пушки
        on -- равняется 1 при зарядке пушки
           -- равняется 0 при бездействии пушки
        live -- жизни пушки (и игрока)
        w, a, s, d -- движение танка
        '''
        self.vx = vx
        self.vy = vy
        self.x = x
        self.y = y
        self.color = color
        self.time = time

        self.death = 1
        self.live = 3
        self.r = 15

    def draw(self, surface):
        # рисует самолет(прямоугольник)

        pygame.draw.polygon(screen, self.color, [(self.x + 2 * self.r, self.y + self.r),
                                                 (self.x - 2 * self.r, self.y + self.r),
                                                 (self.x - 2 * self.r, self.y - self.r),
                                                 (self.x + 2 * self.r, self.y - self.r)])

    '''def create_bomb(self):
        # метод вызывает функцию создания бомбы

        new_bomb(self.x, self.y)'''

    def move(self):
        # движение самолета без гравитации

        if (self.vx + self.x + self.r >= WIDTH):
            self.vx = - 0.8 * self.vx

        if (self.vx + self.x + self.r <= 0):
            self.vx = - 0.8 * self.vx

        if (self.vy + self.y + self.r >= HEIGHT):
            self.vy = - 0.8 * self.vy

        if (self.vy + self.y + self.r <= 0):
            self.vy = - self.vy

        self.x += self.vx
        self.y += self.vy

gun = Gun()
pool_ball = [Ball() for i in range(3)]
plane = Plane(15, 0, randint(0, WIDTH), randint(50, 150), BLUE, 999)

Finished = False

while not Finished:

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    screen.fill(WHITE)
    gun.draw(screen)
    plane.draw(screen)

    score_text = font1.render('Your score: ' + str(score), False, BLACK)
    screen.blit(score_text, (40, 10))

    for i in range(2):
        # движение снарядов танка

        pool_ball[i].draw(screen)
        pool_ball[i].move()

    pygame.display.update()

pygame.quit()


    
    

    


    
















    
