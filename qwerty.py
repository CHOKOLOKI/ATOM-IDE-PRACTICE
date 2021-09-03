from turtle import *
bgcolor('black')
hideturtle()
speed(0)
for amen in range(120):
    color('green')
    circle(amen)
    color('cyan')
    circle(amen * 0.7)
    right(2.5)
    forward(2)
done()
