import pygame
from pygame.draw import *
from random import randint
import sys
pygame.font.init()
pygame.init()

color5 = (230, 176, 170) 
color2 = (165, 105, 189)
color3 = (155, 89, 182)
color4 = (162, 217, 206)
color1 = (249, 235, 234) #этот для фона
color6 = (242, 215, 213)
COLORS = [color1, color2, color3, color4, color5, color6]

FPS = 20
score = 0

width = 1000
height = 750
screen = pygame.display.set_mode((width, height))
screen.fill(color1)


class ball: #всё про шарик

    def __init__(self): #основные параметры шарика
        
        self.x = randint(50, 950)
        self.y = randint(50, 700)
        self.r = randint(10, 50)
        self.v_x = randint(-20, 20)
        self.v_y = randint(-20, 20)
        self.color = COLORS[randint(1, 5)]

    def draw(self, surface): #рисует шарик

        circle(surface, self.color, (self.x, self.y), self.r)

    def move(self): #двигает шарик

        self.x += self.v_x
        self.y += self.v_y

    def collision(self): #описывает отражение от стенок

        if self.x <= self.r or self.x >= width - self.r:
            self.v_x *= -1
            self.x += self.v_x
            self.y += self.v_y

        if self.y <= self.r or self.y >= height - self.r:
            self.v_y *= -1
            self.x += self.v_x
            self.y += self.v_y

    def event(self, event, score): #проверяет, попал ли клик в шарик

        pos_x, pos_y = event.pos
        dist = ((pos_x - self.x)**2 + (pos_y - self.y)**2)**(0.5)
        if dist <= self.r:
            score += 5
            
        return score

class triangle:

    def __init__(self): #основные парматеры треугольника 

        self.a = randint(20, 40) #сторона треугольника
        self.x = randint(40, 960)
        self.y = randint(40, 710)
        self.v_x = randint(-20, 20)
        self.v_y = randint(-20, 20)
        self.color = COLORS[randint(1, 5)]

    def draw(self, surface): #рисует треугольник

        polygon(surface, self.color, [(self.x, self.y), (self.x + self.a, self.y) , (self.x + self.a*(0.5), self.y + self.a*((0.75)**(0.5)))])

    def move(self): #двигает треугольник

        self.y += self.v_y
        self.x += self.v_x

    def collision(self): #описывает отражение от стенок

        if self.x <= 0 or self.x >= width - self.a:
            self.v_x *= -1
            self.x += self.v_x
            self.y += self.v_y

        if self.y <= 0 or self.y >= height - self.a*((0.75)**(0.5)):
            self.v_y *= -1
            self.x += self.v_x
            self.y += self.v_y

    def event(self, event, score): #проверяет, попал ли клик в треугольник

        pos_x, pos_y = event.pos
        if pos_y >= self.y and pos_y <= self.y + self.a*((0.75)**(0.5)):
            if pos_x >= (self.x + 0.5*self.a*(1 - ((self.y + self.a*((0.75)**(0.5)) - pos_y)/self.a*((0.75)**(0.5))))):
                if pos_x <= (self.x + self.a - 0.5*self.a*(1 - ((self.y + self.a*((0.75)**(0.5)) - pos_y)/self.a*((0.75)**(0.5))))):
                    score += 15
            
        return score


pool_ball = [ball() for i in range(8)]
pool_tri = [triangle() for i in range(5)]
ball = ball()
tri = triangle()

f1 = pygame.font.Font(None, 50)
text1 = f1.render('Score: ' + str(score), True, (255, 255, 255))
screen.blit(text1, (10, 10))					
        
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for ball in pool_ball:
                score = ball.event(event, score)
            for tri in pool_tri:
                score = tri.event(event, score)
    	  

    for i in range(8):
    	pool_ball[i].draw(screen)
    	pool_ball[i].collision()
    	pool_ball[i].move()
    for i in range(5):
    	pool_tri[i].draw(screen)
    	pool_tri[i].collision()
    	pool_tri[i].move()
	        
    pygame.display.update()
    screen.fill(color1)
    text1 = f1.render('Score: ' + str(score), True, (255, 255, 255))
    screen.blit(text1, (10, 10))

pygame.quit()
