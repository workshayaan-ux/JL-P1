import turtle
x = turtle.Turtle()
y = turtle.Screen()
x.speed(15)
move = True
def start():
    if move == True:
        x.forward(20)
        y.ontimer(start, 200)
def go_up():
    x.setheading(90)
def go_down():
    x.setheading(270)
def go_left():
    x.setheading(180)
def go_right():
    x.setheading(0)

def stop():
    global move
    move = False

y.listen()
y.onkey(start, "z")
y.onkey(go_down, "s")
y.onkey(go_up, "w")
y.onkey(go_left, "a")
y.onkey(go_right, "d")
y.onkeypress(go_down, "Down")
y.onkeypress(go_up, "Up")
y.onkeypress(go_left, "Left")
y.onkeypress(go_right, "Right")
y.onkey(stop, "0")
turtle.done()