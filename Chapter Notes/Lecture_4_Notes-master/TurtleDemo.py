# A module for drawing a chart with the turtle
import turtle  # import module

# Define window size as constants
window = turtle.Screen()  # create a window for the turtle to draw on
window.title("Turtle Demo")  # the title to show at the top of the window
# WINDOW_WIDTH = 400  # size constants for easy changing
# WINDOW_HEIGHT = 300
WINDOW_WIDTH = 400  # size constants for easy changing
WINDOW_HEIGHT = 300
window.setup(WINDOW_WIDTH, WINDOW_HEIGHT)  # set window size (width, height)
window.setworldcoordinates(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)  # coord system
# Create the turtle
my_turtle = turtle.Turtle()
my_turtle.speed("slow")  # how fast the turtle should move

# #Draw a line...y-axis? 
# my_turtle.home()
# my_turtle.left(90)
# my_turtle.pendown()
# my_turtle.forward(WINDOW_HEIGHT - 50)
# #Draw a line...x-axis? 
# my_turtle.home()
# #my_turtle.left(90)
# my_turtle.pendown()
# my_turtle.forward(WINDOW_WIDTH - 50)

# ##Move the turtle to draw
# my_turtle.home()
# my_turtle.penup()       # do not draw while moving
# my_turtle.goto(30, 60)  # walk to coordinates
# my_turtle.pendown()     # start drawing again
# my_turtle.forward(80)   # move forward
# my_turtle.left(60)      # turn left
# my_turtle.forward(120)  # move forward
# my_turtle.right(120)    # turn left
# my_turtle.forward(120)  # move forward

# my_turtle.home()
# my_turtle.pendown()       # do not draw while moving
# my_turtle.left(90)      # turn left
# my_turtle.forward(100)  # move forward
# my_turtle.right(90)    # turn left
# my_turtle.forward(20)  # move forward
# my_turtle.right(90)  
# my_turtle.forward(100)  # move forward
# my_turtle.right(90)    # turn left
# my_turtle.forward(20)

filename = 'data/sample_data.txt'
with open(filename) as file: 
    count = 0
    for line in file: 
        my_turtle.color("purple")
        my_turtle.pendown()
        my_turtle.begin_fill()
        my_turtle.left(90)
        my_turtle.forward(100)
        my_turtle.right(90)
        my_turtle.forward(20)
        my_turtle.right(90)
        my_turtle.forward(100)
        my_turtle.right(90)
        my_turtle.forward(20)
        my_turtle.end_fill()
        my_turtle.penup()
        my_turtle.right(180)
        my_turtle.forward(20 + 10)

# Make turtle graphics appear and run; wait for the user to close the screen
# This MUST be the last statement executed in the script
window.mainloop()


# 1. Update Speed, Update width, height = 800, 500
# 1.1 Update Speed, update coord: -20, -20
# 2. Draw y
# 3. Draw x


