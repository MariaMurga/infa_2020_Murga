import pygame
from pygame.draw import *
import random
import math

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 700))

#фон
rect(screen, (92,255,253), (0, 0, 500, 320))
rect(screen, (62,255,53), (0, 320, 500, 380))
for i in range(1, 100, 1):
    r = 92 + 1.6*i
    g = 255 - 0.2*i
    b = 253 - 2*i
    radius = 171 - 1.6*i
    circle(screen, (r, g, b), (380, 100), radius)

def draw_unicorn(x, y, dx, z):
    #единорог задается координатами левого верхнего угла прямоугольника,
    #описанного вокруг эллипса его туловища (правого верхнего в случае
    #отзеркаленного единорога), большой осью эллипса его туловища, и
    #параметром z, z либо 1 либо -1,при z = -1 единорога надо отзеркалить
    
    k = dx/190 #коэффициент подобия между нашим единорогом и эталонным (эталонный в упр2)

    #хвост
    color = [[244,164,170], [245,218,117], [209,245,117], [144,208,208], [224,165,228],
          [176,110,180], [219,152,133]]

    for i in range(25):
        X = random.uniform(x + k*z*(-30), x + k*z*20)
        Y = random.uniform(y + k*15, y + k*115)
        dY = random.uniform(15*k, 30*k)
        dX = random.uniform(35*k*z, 50*k*z)

        n = random.randint(0,6)

        ellipse(screen, color[n], (X, Y, dX, dY))

    #туловище
    ellipse(screen, (254,254,254), (x, y, dx*z, 90*k))
    ellipse(screen, (254,254,254), (x + k*z*115, y + k*(-72), 73*k*z, 40*k))
    ellipse(screen, (254,254,254), (x + k*z*143, y + k*(-57), 78*k*z, 30*k))
    rect(screen, (254,254,254), (x + k*z*(108 + ((z-1)/(2*z))*65), y + k*(-50), 65*k, 85*k))

    rect(screen, (254,254,254), (x + k*z*(16 + ((z-1)/(2*z))*16), y + k*30, 16*k, 120*k))
    rect(screen, (254,254,254), (x + k*z*(125 + ((z-1)/(2*z))*17), y + k*40, 17*k, 120*k))
    rect(screen, (254,254,254), (x + k*z*(53 + ((z-1)/(2*z))*15), y + k*30, 15*k, 112*k))
    rect(screen, (254,254,254), (x + k*z*(161 + ((z-1)/(2*z))*15), y + k*30, 15*k, 118*k))

    polygon(screen, (244,164,170), [(x + k*z*137, y + k*(-71)), (x + k*z*156, y + k*(-152)), (x + k*z*155, y + k*(-69))])
    ellipse(screen, (221,92,240), (x + k*z*153, y + k*(-58), 17*k*z, 15*k))
    circle(screen, (0, 0, 0), (x + k*z*165, y + k*(-51)), 4*k)
    polygon(screen, (255,255,255), [(x + k*z*157, y + k*(-58)), (x + k*z*163, y + k*(-54)), (x + k*z*162, y + k*(-52)), (x + k*z*159, y + k*(-53))])

    #грива
    for i in range(20):
        X = random.uniform(x + k*z*85, x + k*z*120)
        Y = random.uniform(y + k*(-80), y + k*15)
        dY = random.uniform(10*k, 25*k)
        dX = random.uniform(30*k*z, 45*k*z)

        n = random.randint(0,6)

        ellipse(screen, color[n], (X, Y, dX, dY))

draw_unicorn(502, 435, 125, -1)
draw_unicorn(265, 330, 85, 1)
draw_unicorn(480, 310, 45, -1)
draw_unicorn(165, 520, 176, 1)

def draw_leaf(x, y, a, e):
    #элемент кроны задается длиной горизонтальной оси и отношением е
    #вертикальной оси к горизонтальной, координатами левого верхнего угла
    #прямоугольника, описанного вокруг эллипса

    p = random.randint(0, 2) #количество плодов на элементе кроны

    rect(screen, (240, 240, 240), (x + a/2 - 10, y + a*e/2, 20, a*e/2 + 50))
    ellipse(screen, (62,255,53), (x, y, a, a*e))
    ellipse(screen, (30,139,0), (x + 2, y + 2, a - 4, a*e - 4))

    for i in range(p):
        X = random.uniform(x + a/2 - 30, x + a/2 + 30)
        Y = random.uniform(y + a*e/2 - 20, y + a*e/2)
        A = random.randint(25, 35)
        E = random.uniform(0.5, 1.5)
        ellipse(screen, (62,255,53), (X, Y, A, A*E))
        ellipse(screen, (251,206,177), (X + 2, Y + 2, A - 4, A*E - 4))


draw_leaf(60, 10, 150, 1.1)
draw_leaf(13, 105, 255, 0.45)
draw_leaf(-10, 122, 85, 1.9)
draw_leaf(62, 195, 148, 0.71)
draw_leaf(-25, 225, 135, 0.85)
draw_leaf(125, 260, 105, 0.72)
draw_leaf(95, 307, 173, 0.32)
draw_leaf(125, 340, 105, 0.5)
draw_leaf(-10, 315, 95, 1.2)
draw_leaf(67, 318, 100, 1.1)
draw_leaf(36, 381, 160, 0.5)
draw_leaf(69, 441, 98, 0.76)
draw_leaf(6, 441, 100, 1.1)
draw_leaf(-20, 499, 160, 0.5)
draw_leaf(10, 551, 98, 0.76)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
