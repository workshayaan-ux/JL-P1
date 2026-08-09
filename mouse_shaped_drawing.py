import turtle
z = turtle.Turtle()
d = turtle.Screen()
z.speed(15)

def follow(x, y):
    d.tracer(0) 
    z.goto (x, y)
    d.tracer(1)
def clack(x, y):
    d.tracer(0)
    z.goto(x, y)
d.listen()
z.ondrag(follow)
d.onclick(clack)

turtle.done()