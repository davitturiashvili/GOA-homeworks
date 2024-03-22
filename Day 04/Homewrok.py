from turtle import *

#we want to paint a grass
speed(30)
width(7)
penup()
goto(-100000, 0)
pendown()

begin_fill()
color("green")
forward(200000)
end_fill()

penup()
goto(0, 0)
pendown()

from turtle import *

#we want to paint a house

#step 1: draw a square
width(7)
color("red")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door

forward(70)
color("purple")
begin_fill()
left(90)
forward(100)    #height of the door
right(90)
forward(50)
right(90)
forward(100)
end_fill()

penup()
goto(200, 200)
pendown()

color("green")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup ()
goto(180, 160)
pendown()

#drawing a window
color("yellow")
right(60)
forward(50)
left(90)
forward(40)
right(-90)
forward(50)
left(90)
forward(40)
left(90)
forward(25)
left(90)
forward(40)
right(-90)
forward(25)
left(90)
forward(20)
left(90)
forward(50)
#end of a window

penup()
goto(60, 160)
pendown()

#drawing a window1
forward(40)
left(90)
forward(40)
left(90)
forward(40)
right(-90)
forward(40)
left(90)
forward(20)
left(90)
forward(40)
right(-90)
forward(20)
left(90)
forward(20)
right(-90)
forward(40)
#end of a window1

penup()
goto(-350, 300)
pendown()

#draw a sun
color("yellow")
begin_fill()
forward(150)
right(90)
forward(100)
right(90)
forward(200)
right(-243)
forward(110)
end_fill()

exitonclick()