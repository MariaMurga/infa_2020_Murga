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
g = 2
Tick = FPS

grey = (45, 45, 45)
black = (10, 10, 10)
blue = (44, 223, 255)
light_red = (255, 20, 20)
red = (220, 0, 0)
white = (255, 255, 255)
light_grey = (200, 200, 200)

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
    
def new_bullet(vx, vy, x, y, color):
    '''
    создаёт новый снаряд пушки
    '''
    bullet = Bomb(vx, vy, x, y, black)
    pool_bullet.append(bullet)

def new_bomb(x, y):
    '''
    создаёт новую бомбу,
    её сбрасывает самолёт
    '''
    bomb = Bomb(randint(-5, 5), 0, x, y, red)
    pool_enemy.append(bomb)


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

        self.color = black

    def targetting(self, event):
        # прицеливает пушку по месту положения курсора

        if event:
            try:
                self.an = math.atan((self.y - event.pos[1]) / (event.pos[0] - self.x))
            except:
                ZeroDivisionError

    def draw(self, surface):
        # рисует танк

        pygame.draw.rect(screen, black, (self.x - 20, self.y, 40, 20) )
        barrel(self.x, self.y, self.f2_power, 10, self.an, screen, self.color)

    def fire2_start(self):
         # начинает процесс зарядки

        self.on = 1
        self.color = light_red

    def power_up(self):
        # продолжает процесс зарядки

        if (self.on and self.f2_power <= 100):
            self.f2_power += 2

    def fire2_end(self):
        # процесс зарядки оканчивается выстрелом,состояние пушки возвращается к исходному

        new_bullet(self.f2_power * math.cos(self.an), - self.f2_power * math.sin(self.an),
                 self.x, self.y, black)
        self.f2_power = 10
        self.color = black
        self.on = 0

    def move_up_start(self):
        # начинает двигать танк вверх при нажатии на w

        self.w = 1

    def move_left_start(self):
        # начинает двигать танк влево при нажатии на a

        self.a = 1

    def move_down_start(self):
        # начинает двигать танк вниз при нажатии на s

        self.s = 1

    def move_right_start(self):
        # начинает двигать танк вправо при нажатии на d

        self.d = 1

    def moving_up(self):
        # двигает танк вверх при нажатии на w

        if (self.w == 1):
            self.y -= 1

    def moving_left(self):
        # двигает танк влево при нажатии на а

        if self.a:
            self.x -= 1

    def moving_down(self):
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

    def move_left_stop(self):
        # прекращает движение по a

        self.a = 0

    def move_down_stop(self):
        # прекращает движение по s

        self.s = 0

    def move_right_stop(self):
        # прекращает движение по d

        self.d = 0

class Ball:
    
    def __init__(self):
        # инициализация

        self.vx = randint(-5, 5)
        self.vy = randint(-5, 5)
        self.x = randint(WIDTH/2, WIDTH)
        self.y = randint(0, HEIGHT)
        self.r = 10
        self.color = blue

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

    def hit(self, pool_bullet):
          # проверяет, попал ли снаряд в цель

          for i, el in enumerate(pool_bullet):
              if (self.x - el.x)**2 + (self.y - el.y)**2 < (2*self.r)**2:
                  return True

class Bomb:
    
    def __init__(self, vx, vy, x, y, color):
        # инициализация

        self.vx = vx
        self.vy = vy
        self.x = x
        self.y = y
        self.r = 10
        self.color = color
        
        self.live = 3 # жизни цели

    def draw(self, surface):
        # рисует цель

        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def move(self):
        # описывает движение цели

        self.x += self.vx
        self.y += self.vy
        self.vy += g

    def hit_a_tank(self, x, y):
          # проверяет, попала ли бомба в танк/попал ли танк в самолёт

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
            return False

class Plane:
    def __init__(self, vx, vy, x, y, color):
        # иициализация
        
        self.vx = vx
        self.vy = vy
        self.x = x
        self.y = y
        self.color = color

        self.live = 3
        self.r = 10

    def draw(self, surface):
        # рисует самолет(прямоугольник)

        pygame.draw.polygon(screen, self.color, [(self.x + 3 * self.r, self.y + self.r),
                                                 (self.x - 3 * self.r, self.y + self.r),
                                                 (self.x - 3 * self.r, self.y - self.r),
                                                 (self.x + 3 * self.r, self.y - self.r)])

    def create_bomb(self):
        # метод вызывает функцию создания бомбы

        new_bomb(self.x, self.y)

    def move(self):
        # движение самолета 

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
plane = Plane(15, 0, randint(0, WIDTH), randint(50, 150), light_grey)

Finished = False

while not Finished:

    clock.tick(FPS)

    screen.fill(grey)
    gun.draw(screen)

    score_text = font1.render('Your score: ' + str(score), False, white)
    screen.blit(score_text, (30, 10))

    for i, el in enumerate(pool_bullet):
        # движение снарядов танка
        el.move()
        el.draw(screen)

    if score < 15:
        # если очков меньше 5 то на экране только цели первого уровня
        for i, el in enumerate(pool_ball):
            el.move()
            el.draw(screen)

        for i, el in enumerate(pool_ball):
            if el.hit(pool_bullet):
                pool_ball.pop(i)
                score += 5

        level_text = font1.render('Level 1', False, white)
        screen.blit(level_text, (560, 10))

    if score >= 15:
        '''
        когда поражены все цели первого уровня,
        на экране генерится самолёт и начинает скидывать бомбы,
        они уменьшают хп.
        Бомбы скидываются раз в 1 секунду (за 30 Tick, где начальное Tick = FPS)
        '''

        plane.draw(screen)
        plane.move()
        Tick -= 1

        if Tick == 0:
            plane.create_bomb()
            Tick = FPS

        for i, el in enumerate(pool_enemy):
            el.draw(screen)
            el.move()

        for i, el in enumerate(pool_enemy):
            if el.hit_a_tank(gun.x, gun.y):
                gun.live -= 1
                pool_enemy.pop(i)

        for i, el in enumerate(pool_bullet):
            if el.hit_a_tank(plane.x, plane.y):
                plane.live -= 1
                print(1)
                pool_bullet.pop(i)
                score += 10

        level_text = font1.render('Level 2', False, white)
        screen.blit(level_text, (560, 10))

    gun.power_up()
    gun.moving_up()
    gun.moving_down()
    gun.moving_left()
    gun.moving_right()

    for event in pygame.event.get(): # обработка команд танку
        if event.type == pygame.QUIT:
            Finished = True
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start()

        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end()

        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

        if event.type == pygame.KEYDOWN:
            if event.unicode == 'w':
                gun.move_up_start()

            elif event.unicode == 's':
                gun.move_down_start()

            elif event.unicode == 'd':
                gun.move_right_start()

            elif event.unicode == 'a':
                gun.move_left_start()

        if event.type == pygame.KEYUP:
            if event.unicode == 'w':
                gun.move_up_stop()

            elif event.unicode == 's':
                gun.move_down_stop()

            elif event.unicode == 'd':
                gun.move_right_stop()

            elif event.unicode == 'a':
                gun.move_left_stop()

    if gun.live == 0:  # итоги игры
        print("You died sorry bro I don't make the rules")
        Finished = True

    if plane.live == 0:
        print("You won!!!! Now you're the Fattest Doggo")
        Finished = True

    pygame.display.update()

pygame.quit()


    
    

    


    
















    
