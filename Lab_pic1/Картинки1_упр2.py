import pygame
from pygame.draw import *
import random

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 700))

#фон
rect(screen, (92,255,253), (0, 0, 500, 320))
rect(screen, (64,253,43), (0, 320, 500, 380))
circle(screen, (253,218,28), (480, 55), 70)

#дерево
ellipse(screen, (24,154,41), (9, 90, 140, 160))
ellipse(screen, (24,154,41), (-30, 190, 230, 120))
rect(screen, (241, 241, 241), (71, 290, 23, 190))
ellipse(screen, (24,154,41), (12, 285, 145, 110))

circle(screen, (251,206,177), (105, 132), 17)
circle(screen, (251,206,177), (5, 251), 17)
circle(screen, (251,206,177), (173, 255), 17)
circle(screen, (251,206,177), (120, 377), 17)

#хвост единорога
color = [[244,164,170], [245,218,117], [209,245,117], [144,208,208], [224,165,228],
          [176,110,180], [219,152,133]]

for i in range(25):
    x = random.randint(200, 250)
    y = random.randint(480, 580)
    dy = random.randint(15, 30)
    dx = random.randint(35, 50)

    n = random.randint(0,6)

    ellipse(screen, color[n], (x, y, dx, dy))

#единорог
ellipse(screen, (254,254,254), (230, 465, 190, 90))
ellipse(screen, (254,254,254), (345, 393, 73, 40))
ellipse(screen, (254,254,254), (373, 408, 78, 30))
rect(screen, (254,254,254), (338, 415, 65, 85))

rect(screen, (254,254,254), (246, 495, 16, 120))
rect(screen, (254,254,254), (355, 505, 17, 120))
rect(screen, (254,254,254), (283, 495, 15, 112))
rect(screen, (254,254,254), (391, 495, 15, 118))

polygon(screen, (244,164,170), [(367, 394), (386, 313), (385, 396)])
ellipse(screen, (221,92,240), (383, 407, 17, 15))
circle(screen, (0, 0, 0), (395, 414), 4)
polygon(screen, (255,255,255), [(387, 407), (393, 411), (392, 413), (389, 412)])

#грива
for i in range(20):
    x = random.randint(315, 350)
    y = random.randint(385, 480)
    dy = random.randint(10, 25)
    dx = random.randint(30, 45)

    n = random.randint(0,6)

    ellipse(screen, color[n], (x, y, dx, dy))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

