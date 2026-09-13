import pgzrun
WIDTH = HEIGHT = 400
def draw():
    screen.fill("white")
    rectangle = Rect((100, 300), (200, 100))
    screen.draw.filled_rect(rectangle, "yellow")
    s1 = Rect((50, 100), (50, 50))
    screen.draw.filled_rect(s1, "blue")
    s2 = Rect((300, 100), (50, 50))
    screen.draw.filled_rect(s2, "blue")
    screen.draw.filled_circle((200, 200), (50), "red")
    screen.draw.text("!@#$%^&*", (115, 325), color = "black", fontsize = 50)
pgzrun.go()
