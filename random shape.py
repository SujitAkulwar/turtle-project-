import turtle
import math

a=turtle.Turtle()

a.getscreen().bgcolor("#444444")
a.color("red","yellow")
a.speed(10)
a.begin_fill()



for j in range(10):
    a.left(36)
    for i in range(5):
        a.forward(200)
        a.left(216)



a.end_fill()
turtle.done()