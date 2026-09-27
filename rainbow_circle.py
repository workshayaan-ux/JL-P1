import pgzrun

WIDTH = 600
HEIGHT = 400

def draw():
    screen.clear()

    colors = [
        "violet",
        "indigo",
        "blue",
        "green",
        "yellow",
        "orange",
        "red"
    ]

    center = (WIDTH // 2, HEIGHT // 2)
    radius = 200

    for color in colors:
        screen.draw.filled_circle(center, radius, color)
        radius = radius-25

pgzrun.go()