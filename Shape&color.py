import turtle

screen = turtle.Screen()
t = turtle.Turtle()

shapes = ["turtle", "circle", "square", "triangle"]
current = 0
colors = ["red", "green", "blue"]

def red():
    t.color(colors[0])

def green():
    t.color(colors[1])

def blue():
    t.color(colors[2])


def change_shape():
    global current

    t.shape(shapes[current])
    current = current + 1

    if current == len(shapes):
        current = 0

screen.onkey(change_shape, "space")
screen.onkey(red, "r")
screen.onkey(green, "g")
screen.onkey(blue, "b")
screen.listen()


turtle.done()

