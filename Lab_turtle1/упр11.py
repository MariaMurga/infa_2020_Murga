import turtle

turtle.shape('turtle')
turtle.left(90)

def btrfl(n):
    turtle.circle(n)
    turtle.circle(-n)

x = 1
n = 25

while x <= 16:
    btrfl(n)
    n += 5
    x += 1
