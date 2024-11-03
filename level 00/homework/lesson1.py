from turtle import *

speed(10)
width(6)

color("red")
begin_fill()
forward(200) # draw square
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()


# draw door
color("black")

begin_fill()
forward(75)
left(90)
forward(110)
right(90)
forward(60)
right(90)
forward(110)
end_fill()

penup()
goto(200,200)
pendown()

color("green")
begin_fill()


#saxuravi
right(90)
right(60)
forward(120) 
left(60)
forward(80)
left(60)
forward(120)
end_fill()

#saxlis garegani nawili
color("black")
begin_fill()
left(30)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)

#fanjara 
penup()
goto(20,180)
pendown()

color("blue")
begin_fill()
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
end_fill()

penup()
goto(180,180)
pendown()

color("blue")
begin_fill()

forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
end_fill()

exitonclick()