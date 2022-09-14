from turtle import *

# turtle and pen requirements
speed(5)
shape('turtle')
pencolor('green')
pensize(10)
setup(1000,1000)

# moving to starting point
penup()
goto(200,100)
pendown()

# draw the triangle
fillcolor('purple')
begin_fill()
right(60)
forward(100)
right(120)
forward(100)
right(120)
forward(100)
end_fill()

# turn turtle back to green
fillcolor('green')

# move to new location
penup()
goto(-200,-200)
pendown()

# Change turtle settings
pensize(5)
pencolor('red')
fillcolor('blue')

# draw square
begin_fill()
right(60)
forward(200)
right(90)
forward(200)
right(90)
forward(200)
right(90)
forward(200)
end_fill()

#  turn  turtle back to original and new settings
fillcolor('green')
pensize(2)
pencolor('orange')
fillcolor('black')

#draw rectangle
begin_fill()
penup()
goto(-250,150)
pendown()
right(90)
forward(50)
right(90)
forward(25)
right(90)
forward(50)
right(90)
forward(25)
end_fill()

# Finish the turtle at 0,0 original settings
penup()
pencolor('green')
fillcolor('green')
goto(0,0)



done()

