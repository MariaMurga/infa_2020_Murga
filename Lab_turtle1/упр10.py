import turtle

turtle.shape('turtle')

x = 1
n = 7

def flower(x, n):
    while x <= n:
        turtle.circle(50)
        turtle.left(360. / n)
        x += 1

flower(x, n)
