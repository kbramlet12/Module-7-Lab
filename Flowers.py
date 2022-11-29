#===============================================================================
# Program Flower
# Name: Keegan Bramlet
# Date: 11/28/22
# Purpose of a Program: draw the flower pattern using turtle
#===============================================================================
import turtle
from turtle import *

def flower(t, sz):
    for i in range(10):
        for p in range(6):
            t.forward(sz)
            t.left(300)
        t.left(36)

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("pink")

flower(alex, 90)

wn.exitonclick()
