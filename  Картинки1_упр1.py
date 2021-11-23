import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))

rect(screen, (210, 210, 210), (0, 0, 500, 500))

circle(screen, (0, 0, 0), (250, 250), 150)
circle(screen, (251,249,112), (250, 250), 149)

circle(screen, (0, 0, 0), (190, 230), 40)
circle(screen, (255,0,0), (190, 230), 39)
circle(screen, (0, 0, 0), (190, 230), 15)

circle(screen, (0, 0, 0), (310, 230), 30)
circle(screen, (255,0,0), (310, 230), 29)
circle(screen, (0, 0, 0), (310, 230), 10)

polygon(screen, (0, 0, 0), [(150, 160), (145,155), (240, 195), (245, 200)])
polygon(screen, (0, 0, 0), [(350, 170), (345,165), (270, 195), (275, 200)])

rect(screen, (0, 0, 0), (166, 310, 150, 10))
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
