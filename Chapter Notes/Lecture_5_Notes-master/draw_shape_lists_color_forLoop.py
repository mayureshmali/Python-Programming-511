import turtle  # import module so you can work with it
WINDOW_WIDTH = 800  # size constants for easy changing
WINDOW_HEIGHT = 500

## 1
## I want a turtle that draws some shapes
## How about an octagon?

# fred.home()
# for side in range(8): 
#     fred.forward(50)
#     fred.left(360/8)    

## 2
## Now I want my turtle to draw 3 octagons! With color!
## Q: 2nd loop? Color goes where? 
# for shape in range(3): 
#     for side in range(8): 
#         fred.pendown()
#         fred.forward(50)
#         fred.left(360/8)
#         fred.penup()
#     fred.forward(150) 

## 3
## Now wrap it in a function
# def draw_oct (turtle): 
#     for shape in range(3): 
#         for side in range(8): 
#             turtle.pendown()
#             turtle.forward(50)
#             turtle.left(360/8)
#             turtle.penup()
#         turtle.forward(150) 

# draw_oct(fred)

## 4
## Add Color Function make them stop signs!
## No, make them 3 different colors...

def choose_color(index): 
    colors = ["red", "blue", "green"]
    return colors[index%3]


def draw_oct(turtle, num): 
    for shape in range(num): 
        turtle.pendown()
        turtle.begin_fill()
        turtle.color(choose_color(shape))
        for side in range(8): 
            turtle.pendown()
            turtle.forward(50)
            turtle.left(360/8)
        turtle.end_fill()
        turtle.penup()
        turtle.forward(150) 
    

def user_input(): 
    shape_num= int(input("How many Octagons do you want? "))
    turtle_name = input("What do you want to name your turtle? ")
    window = turtle.Screen()  # create a window (canvas) for the turtle to draw on
    window.title("Fred's Demo for IMT 511")  # the title to show at the top of the window
    window.setup(WINDOW_WIDTH, WINDOW_HEIGHT)  # set window size (width, height)
    window.setworldcoordinates(-50, -50, WINDOW_WIDTH, WINDOW_HEIGHT)  # coord system
    turtle_name = turtle.Turtle()
    turtle_name.speed("slow")  
    turtle_name.shape("turtle")
    draw_oct(turtle_name, shape_num)
    window.mainloop()

if __name__ == "__main__": 
    #execute this if run as a script
    user_input()

# ## Fully Baked
# def choose_color(index): 
#     colors_list = ["red", "green", "blue"] 
#     return colors_list[index%3]

# #print(choose_color(0))

# ##for loop and range example
# def draw_shape (turtle): 
#     turtle.penup()
#     turtle.goto(50,50)
#     turtle.pendown()
#     for i in range(5):
#         turtle.begin_fill()
#         turtle.color(choose_color(i))
#         num_sides = 5
#         for sid_num in range(num_sides): 
#             turtle.forward(100)
#             turtle.left(360/num_sides)     
#         turtle.end_fill()
#         turtle.penup()
#         turtle.forward(250)
#         turtle.pendown()

# draw_shape(turtle)



# Make turtle graphics appear and run; wait for the user to close the screen
# This MUST be the last statement executed in the script

