# game will utilize graphics.py as opposed to turtle graphics
import turtle
import os

# screen set up
win = turtle.Screen()
win.bgcolor("black")
win.title("pup space game")

# draw a border
border_pen = turtle.Turtle()
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
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

player_Speed = 15


# move left
def move_left():
    x = player.xcor()
    x -= player_Speed
    player.setx(x)


win.listen()
win.onkeypress(move_left,"left")




delay = input("press enter to exit")