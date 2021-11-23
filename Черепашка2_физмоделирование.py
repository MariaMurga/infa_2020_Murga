import turtle
import math

turtle.hideturtle()
turtle.shape('turtle') #мне смешно сделать прыгающую черепашку вместо точки, извинибте
turtle.shapesize(1)

Vx = 20
Vy = 100 
g = -25
dt = 0.05
y0 = 2

turtle.penup()

x = -200
y = 0
turtle.goto(x,y)

turtle.pendown()
turtle.showturtle()

while 1 < 2:
	if (abs(y) < y0) and (Vy < 0):
		Vy *= (-0.75)
		Vx *= (0.75) 
	x += Vx * dt
	y += Vy * dt + (g * ((dt) ** 2)) / 2
	Vy += g * dt
	turtle.goto(x, y)
