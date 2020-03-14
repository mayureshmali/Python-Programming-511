# A module for drawing a chart with the turtle
import turtle  # import module
# os module provides a portable way of using operating system dependent functionality
import os      # import module       
from turtle import *


def draw_axes(path):
    """ Function: Draws the x and y axis based on the data file
    Arguments accpeted: path of the data file to be visualized
    Return: None
    """    
    draw_y_axis()  
    draw_y_axis_ticks() 
    draw_y_axis_labels(get_max_value(path))
    draw_x_Axis(count_observations(path),get_labels(path))


x_origin=80
y_origin=60
chart_height=450
def draw_y_axis():
    """ Function: draw_y_axis() to draw the y axis with origin(80,50) and chart height = 450 pixels
    Arguments accpeted: None
    Return: None
    """
    turtle.penup()
    turtle.goto(x_origin,y_origin)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(chart_height)

def draw_y_axis_ticks():
    """ Function: draw_y_axis_ticks() to draw 10 evenly spaced y-axis ticks at regular intervals
    Arguments accpeted: None
    Return: None
    """
    turtle.penup()
    turtle.goto(x_origin,y_origin)
    for i in range(0,11):
    #for 10 evenly spaced intervals we loop from 0 to 11
        turtle.left(90)
        turtle.pendown()
        turtle.forward(10)
        turtle.penup()
        turtle.backward(10)
        turtle.right(90)
        turtle.forward(chart_height/10)  

def draw_y_axis_labels(max_val):
    """ 
    Function: draw_y_axis_labels(arg1) to draw y-axis labels by 
    dynamically calculating the y axis height to only the maximum value in data file 
    Arguments accpeted: max_val from function get_max_value()
    Return: None
    """
    turtle.penup()
    turtle.goto(x_origin,y_origin-5)
    for i in range(0,11):
        turtle.left(90)
        turtle.forward(40)
        turtle.pendown()
        turtle.write(round(i*(max_val/10),2),move=False, align="left", font=("Arial", 8, "normal"))
        turtle.penup()
        turtle.backward(40)
        turtle.right(90)
        turtle.forward(chart_height/10)  

chart_width=800
def draw_x_Axis(count1,label):
    """ 
    Function: draw_x_Axis(arg1,arg2) to draw x-axis and its labels by 
    dynamically calculating the x axis length to number of observations in data file
    Arguments accpeted: max_val from function get_max_value()
    Return: None
    """
    turtle.penup()
    turtle.goto(x_origin,y_origin)
    turtle.right(90)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(10)
    turtle.penup()
    turtle.backward(10)
    turtle.left(90)
    for i in range(0,count1):
        turtle.pendown()
        turtle.forward(chart_width/(count1))
        turtle.right(90)
        turtle.forward(10)
        turtle.penup()
        turtle.forward(20)
        turtle.pendown()
        turtle.write(label[i])
        turtle.penup()
        turtle.backward(30)
        turtle.left(90)
        
    turtle.pendown()
    turtle.forward(chart_width/(count1))
    turtle.penup()

def get_max_value(path1):
    """ 
    Function: get_max_value(arg1)calculates maximum value of feature of interest in a data file.
    Arguments accpeted: path of data file entered by user input
    Return: maximum numeric value of first feature in data file
    """
    maxval = 0
    step = 3
    with open('Output.txt',"w") as f2:
        with open(path1,"r") as file:
            for lineno, line in enumerate(file):
                if lineno % step == 1:
                    f2.write(line)
                
        
            
    with open('Output.txt') as f3:
        for line in f3:
            if maxval <= int(line.strip()): # converted a string into an int
                 maxval = int(line.strip()) # made that int into maxval

    if os.path.exists("Output.txt"):
        os.remove("Output.txt")
    return maxval

def count_observations(path2):
    """ 
    Function: count_observations(arg1) calculates number of observations in a data file.
    Arguments accpeted: path of data file entered by user input
    Return: count of no. of observations in the file 
    """
    num_lines = 0
    with open(path2, 'r') as f:
            for line in f:
                num_lines += 1
    count=int((num_lines/3))
    return count 

def get_labels(path3):
    """ 
    Function: get_labels(arg1) stores label names of observations in a list called labels[]
    Arguments accpeted: path of data file entered by user input
    Return: label list
    """
    step=3
    with open('Output1.txt',"w") as f4:
        with open(path3, "r") as file1:
            for lineno, line in enumerate(file1):
                    if lineno % step == 0:
                        f4.write(line)
    
    labels=[]
    with open('Output1.txt') as f5:
        labels = [line.rstrip('\n') for line in open('Output1.txt')]
        #for line in f5:
        #    labels.append(line.rstrip().split(','))
    if os.path.exists("Output1.txt"):
        os.remove("Output1.txt")
    return(labels)
    
def choose_color(userinput1):
    """ 
    Function: choose_color(arg1) used to select the color theme type as entered by user for the bar graph
    Arguments accpeted: User input as typed by user either the string "Dark" or "Light" on what the user wants.
    Return: True if user types 'Dark' theme. Returns false if user types 'Light' as the theme.
    """
    if userinput1=="Dark":
        return True
    elif userinput1=="Light":
        return False


def draw_rectangle(height,clr,max_val1,bar_width1,bar_height1):
    """ 
    Function: draw_rectangle(arg1,arg2,arg3,arg4,arg5) used to draw a single bar graph block based on the input parameters
    Arguments accpeted: 
    arg1- a list of UW points scored against the various teams which wil be used to set the height of every bar
    arg2- list of color palette based on choice of theme by user.
    arg3- maximum value in data file as returned by get_max_value() function 
    arg4- A number that represents width of each single bar
    arg5- Represents the height of each bar scaled according to the chart_height.
    
    The bar graphs are plotted in interative fashion in a loop for every 1st feature value present in data file.
    """
    height2=height*(bar_height1/(max_val1/10))
    turtle.begin_fill()
    turtle.color(clr)
    turtle.setheading(90)
    turtle.forward(height2)
    turtle.write(str(height))
    turtle.right(90)
    turtle.forward((bar_width1)/2)
    turtle.right(90)
    turtle.forward(height2)
    turtle.left(90)
    turtle.end_fill()
    turtle.forward(bar_width1*0.5)

def draw_bars(path4, chart_width1, count_1,chart_height1,choose_color):
    """ 
    Function: draw_rectangle(arg1,arg2,arg3,arg4,arg5) used to draw a single bar graph block based on the input parameters
    Arguments accpeted: 
    arg1- path of data file as input by user in the interactive command line prompt
    arg2- width of the chart
    arg3- number of observations as returned by count_observations() function
    arg4- height of chart
    arg5- accepts the user choice for type of color palette for the bat graph - Dark/Light
    
    The bar graphs are plotted in interative fashion in a loop for every 1st feature value present in data file.
    """
    turtle.goto(x_origin,y_origin)
    step=3
    with open('Output2.txt',"w") as f6:
        with open(path4, "r") as file3:
            for lineno, line in enumerate(file3):
                if lineno % step == 1:
                    f6.write(line)
    UWscores=[]
    with open('Output2.txt') as f7:
        UWscores = [line.rstrip('\n') for line in open('Output2.txt')]
    for i in range(0, len(UWscores)): 
        UWscores[i] = int(UWscores[i]) 
    
    if os.path.exists("Output2.txt"):
        os.remove("Output2.txt")
    
    #colors = ["red","green","blue","orange","brown","yellow","pink","violet","purple","teal","Aqua","Navy Blue","Lime","black","grey"]        
    darkcolors=["navy","darkcyan","crimson","brown","orange","red","slateblue","purple","violet","blue","dodgerblue","indigo","forestgreen","gray","darkorchid"]
    lightcolors=["gold","springgreen","plum","lightpink","aqua","yellow","orange","lavenderblush","bisque","paleturquoise","wheat","salmon","lightgreen","skyblue","lightcoral"]
    bar_width=(chart_width/count_1)
    turtle.forward(bar_width*0.75)
    bar_height= (chart_height/10)
    if(choose_color):
        colors=darkcolors
    else:
            colors = lightcolors
    idx=0
    for value in UWscores:
        draw_rectangle(value, colors[idx],get_max_value(path),bar_width,bar_height)
        idx = idx + 1


path = input("Enter the path of text file to visualize; eg. data/textfile.txt --->")
#path = "data/huskies2016.txt"
name= input("What should the chart be named? ")
userinput1 = input("Choose and please enter a theme type --> 'Dark'/'Light':")


# Define window size as constants
window = turtle.Screen()  # create a window for the turtle to draw on
window.title(name)  # the title to show at the top of the window
WINDOW_WIDTH = 1200  # size constants for easy changing
WINDOW_HEIGHT = 600
window.setup(WINDOW_WIDTH, WINDOW_HEIGHT)  # specify window size (width, height)
window.setworldcoordinates(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)  # coordinate system: origin at lower-left

# Create the turtle
my_turtle = turtle.Turtle()
my_turtle.speed("fastest")  # how fast the turtle should move

# Move the turtle to draw
#my_turtle.penup()       # do not draw while moving
#my_turtle.goto(30, 60)  # walk to coordinates
#my_turtle.pendown()     # start drawing again
#my_turtle.forward(80)   # move forward
#my_turtle.left(60)      # turn left
#my_turtle.forward(120)  # move forward
#my_turtle.right(120)    # turn left
#my_turtle.forward(120)  # move forward


draw_axes(path)  #Call the draw_axes() to draw x and y axis with ticks and labels from data file.

get_labels(path) #Get labels from data file into a list   

#Call the draw_bars() to draw the bar graph
draw_bars(path, chart_width, count_observations(path),chart_height,choose_color(userinput1)) 

# Make the turtle graphics appear and run, waiting for the user to close the screen
# This MUST be the last statement executed in the script
window.mainloop()
