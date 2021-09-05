from turtle import *
setup(width=900, height=650)
speed (100)
bgcolor('black')
colors = ['pink', 'violet', 'magenta', 'red', 'white', 'orange']

for gio in range(240):
    color(colors[gio%6])
    width(gio/100+1)
    forward(gio)
    left(59)

forward(20)
penup()
color('white')
goto(-20,-300)
hideturtle()
