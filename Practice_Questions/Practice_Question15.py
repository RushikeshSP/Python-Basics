# 15)	Python – Draw Star Using Turtle Graphics.


# import for turtle
import turtle
 
# Starting a Working Screen
ws = turtle.Screen()
 
# initializing a turtle instance
geekyTurtle = turtle.Turtle()
 
# executing loop 5 times for a star
for i in range(5):
 
        # moving turtle 100 units forward
        geekyTurtle.forward(100)
 
        # rotating turtle 144 degree right
        geekyTurtle.right(144)








        

'''
#import turtle
import turtle

# set screen
Screen = turtle.Turtle()

# decide colors
cir = ['red', 'green', 'blue', 'yellow', 'purple']

# decide pensize
turtle.pensize(4)

# Draw star pattern
turtle.penup()
turtle.setpos(-90, 30)
turtle.pendown()
for i in range(5):
    turtle.pencolor(cir[i])
    turtle.forward(200)
    turtle.right(144)

turtle.penup()
turtle.setpos(80, -140)
turtle.pendown()

# choose pen color
turtle.pencolor("Black")
turtle.done()
'''