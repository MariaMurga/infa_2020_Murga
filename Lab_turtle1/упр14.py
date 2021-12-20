import turtle

turtle.shape('turtle')

def stars(n):
    turtle.left(180 - (180 / n))
    turtle.forward(200)
    
x = 1
while x <= 5:
    stars(5)
    x += 1

turtle.clear()

x = 1
while x <= 11:
    stars(11)
    x += 1
