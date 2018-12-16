# game will utilize graphics.py as opposed to turtle graphics
from turtle import *
from random import *
from math import *
import os

# screen set up
win = Screen()
win.bgcolor("black")
win.title("pup space game")

# draw a border
border_pen = Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pensize(5)
border_pen.pendown()
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# create the character object
player = Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)


player_Speed = 15


# enemy
colors = ["red", "purple", "green", "yellow"]
shapes = ["circle", "square", "rectangle", "turtle", "classic"]
enemy = Turtle()
enemy.color(choice(colors))
enemy.shape(choice(shapes))
enemy.penup()
enemy.speed(0)
enemy.setposition(-200,273)
enemy_speed = 5


# missle
bullet = Turtle()
bullet.color("red", "yellow")
bullet.shape("arrow")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bullet_speed = 20


# bullet stages: ready and fire
bullet_state = "ready"

# move left
def move_left():
    x = player.xcor()
    x -= player_Speed
    if x < -285:
        x = -285
    player.setx(x)


def move_right():
    x = player.xcor()
    x += player_Speed
    if x > 285:
        x = 285
    player.setx(x)


def move_up():
    y = player.ycor()
    y += player_Speed
    if y > 273:
        y = 273
    player.sety(y)


def move_down():
    y = player.ycor()
    y -= player_Speed
    if y < -273:
        y = -273
    player.sety(y)


def player_fire():
    global bullet_state

    if bullet_state == "ready":
     bullet_state = "fire"
     x = player.xcor()
     y = player.ycor() + 5
     bullet.setposition(x,y)
     bullet.showturtle()


def isCollision(t1, t2):
    distance = sqrt(pow(t1.xcor()-t2.xcor(),2)+pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False



win.listen()
win.onkey(move_left,"Left")
win.onkey(move_right,"Right")
win.onkey(move_up,"Up")
win.onkey(move_down,"Down")
win.onkey(player_fire, "space")

while True:

    # moving enemy
    x = enemy.xcor()
    x += enemy_speed
    enemy.setx(x)

    if enemy.xcor() > 285:
        y = enemy.ycor()
        y -= 40
        enemy_speed *= -1
        enemy.sety(y)

    if enemy.xcor() < -280:
        y = enemy.ycor()
        y -= 40
        enemy_speed *= -1
        enemy.sety(y)

    # if bullet_state == "fire":
    y = bullet.ycor()
    y += bullet_speed
    bullet.sety(y)

    if bullet.ycor() > 280:
        bullet.hideturtle()
        bullet_state = "ready"


    # check for collision
    if isCollision(bullet, enemy):
       # reset bullet
       bullet.hideturtle()
       bullet_state = "ready"
       bullet.setposition(0, -400)
       # reset enemy that was hit
       enemy.setposition(-200,250)


    if isCollision(player, enemy):
        player.hideturtle()
        enemy.hideturtle()
        print("game over")
        break


# mainloop()

delay = input("press enter to exit")