from random import randint
import turtle

n = 20
dt = 0.05
Vx = []
Vy = []
X = []
Y = []
d = 20

#границы
turtle.penup()
turtle.goto(-300, -300)
turtle.pendown()
turtle.goto(-300, +300)
turtle.goto(+300, +300)
turtle.goto(+300, -300)
turtle.goto(-300, -300)

pool = [turtle.Turtle(shape='circle') for i in range(n)]

for i in range(len(pool)):
    pool[i].penup()
    pool[i].speed(0)
    X.append(randint(-300, 300))
    Y.append(randint(-300, 300))
    Vx.append(randint(-150, 150))
    Vy.append(randint(-150, 150))
    pool[i].goto(X[i], Y[i])
    
#ЗСЭ + ЗСИ + считаем массы частиц одинаковыми => при столкновении частицы обмеиваются скоростями
while 1 < 2:
    for j in range(len(pool)):
        #стенки
        if (abs(300 - Y[j]) < d) and (Vy[j] > 0):
            Vy[j] = -Vy[j]
        
        elif (abs(-300 - Y[j]) < d) and (Vy[j] < 0):
            Vy[j] = -Vy[j]
       
        elif (abs(300 - X[j]) < d) and (Vx[j] > 0):
            Vx[j] = -Vx[j]
        
        elif (abs(-300 - X[j]) < d) and (Vx[j] < 0):
            Vx[j] = -Vx[j]

        #другие частицы
        for i in range(len(pool)):
            if (i > j) or (i < j):
                if (abs(X[i] - X[j]) < d) and (abs(Y[i] - Y[j]) < d):
                    a = Vx[i]
                    b = Vy[i]
                    Vx[i] = Vx[j]
                    Vy[i] = Vy[j]
                    Vx[j] = a
                    Vy[j] = b

        
        X[j] += Vx[j] * dt
        Y[j] += Vy[j] * dt
        pool[j].goto(X[j], Y[j])

