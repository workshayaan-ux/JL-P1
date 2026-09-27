import pgzrun
import random
msg = ""
WIDTH = 600
HEIGHT = 400
sh = Actor("skeletal horse")

def draw():
    screen.fill("black")
    sh.draw()
    screen.draw.text(msg, (300,200))
def update():
    if keyboard.left:
        sh.x -= 25
    if keyboard.right:
        sh.x += 25
    if keyboard.up:
        sh.y -= 25
    if keyboard.down:
        sh.y += 25
def raandom():
    sh.x = random.randint(0, 450)
    sh.y = random.randint(0, 250)
def on_mouse_down(pos):
    global msg
    if sh.collidepoint(pos):
        raandom()
        msg = "bomboclat"
    else:
        msg = "megaknight"

pgzrun.go()