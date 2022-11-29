#===============================================================================
# Program Name: Squares
# Name: Keegan Bramlet
# Date: 11/28/22
# Purpose of a Program: draw the sqaure patter using turtle
#===============================================================================

import turtle

def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

    t.penup()
    t.goto(-sz/2, -sz/2)
    t.pendown()

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")

drawSquare(alex, 20)
drawSquare(alex, 40)
drawSquare(alex, 60)
drawSquare(alex, 80)
drawSquare(alex, 100)

wn.exitonclick()
