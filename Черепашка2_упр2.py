import turtle

turtle.shape('turtle')

a = 25

numbrs = [
	[(0, 0), (a, 0), (a, -2*a), (0, -2*a), (0, 0)],
	[(0, -a), (a, 0), (a, -2*a)],
	[(0,0), (a, 0), (a, -a), (0, -2*a), (a, -2*a)],
	[(0, 0), (a, 0), (0, -a), (a, -a), (0, -2*a)],
	[(0,0), (0, -a), (a, -a), (a, 0), (a, -2*a)],
	[(a, 0), (0,0), (0, -a), (a, -a), (a, -2*a), (0, -2*a)],
	[(a, 0), (0, -a), (a, -a), (a, -2*a), (0, -2*a), (0, -a)],
	[(0, 0), (a, 0), (0, -a), (0, -2*a)],
	[(0, -a), (0, 0), (a, 0), (a, -2*a), (0, -2*a), (0, -a), (a, -a)],
	[(0, -2*a), (a, -a), (a, 0), (0, 0), (0, -a), (a, -a)],
]

x = 0
y = 0

def numbr(n, X): 	
	num = numbrs[n]
	l = len(num)
	turtle.penup()
	x, y = num[0]
    
	turtle.goto(x + X, y)
	turtle.pendown()
	for k in range (1, l, 1):
		x, y = num[k]
		turtle.goto(x + X, y)

numbr(1, 0)
numbr(4, 2*a)
numbr(1, 4*a)
numbr(7, 6*a)
numbr(0, 8*a)
numbr(0, 10*a)
