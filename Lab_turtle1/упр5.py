import turtle
turtle.shape("turtle")

x = 1
y = 10
turtle.speed(10)

while x <= 10:
    turtle.left(225)
    turtle.penup()
    turtle.forward((y**2/2)**0.5)
    turtle.left(135)
    turtle.pendown()
    turtle.forward(y*x)
    turtle.left(90)
    turtle.forward(y*x)
    turtle.left(90)
    turtle.forward(y*x)
    turtle.left(90)
    turtle.forward(y*x)
    turtle.left(90)
    x += 1
