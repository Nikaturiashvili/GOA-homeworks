print("nika turiashvili")

from turtle import *


#we want to paint a house

#step 1:  draw a square
speed(30)


width(7)



color("blue")

forward(200)



left(90) 



forward(200)



left(90)



forward(200)

left(90)


forward(200)


left(90)



forward(70)


color("yellow")



#drawing a door

left(90)


forward(120)



right(90)


forward(60)


right(90)


forward(120)



penup()



goto(200, 200)



pendown()




color("red")

begin_fill()
right(150)

forward(200)

left(120) 



forward(200)

end_fill()

#draw a window
penup()
goto(180, 180)
pendown()
color("green")
left(30)
forward(50)
right(90)
forward(40)
right(90)
forward(50)
right(90)
forward(40)
left(180)
forward(20)
left(90)
forward(50)
right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(40)

penup()
goto(40,130)
pendown()
forward(20)
left(180)
forward(40)
right(90)
forward(50)
right(90)
forward(40)
right(90)
forward(50)
right(90)
forward(20)
right(90)
forward(50)
left(90)
forward(20)
left(90)
forward(25)
left(90)
forward(40)
exitonclick()


