import math
import random
from graphics import *

# create the graphwin object
canvas = GraphWin("Random Graphics", 1000, 700)
canvas.setBackground("blue")
w, h = canvas.getWidth(), canvas.getHeight()

# function to draw random
def randomCircles(n):
    # draw n random circles
    for i in range(n):
        # make a random circle
        x, y = random.randint(0,w), random.randint(0,h)
        radius = random.randint(20,300)
        circle = Circle(Point(x,y), radius)
        
        # random color and make a color
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        circle.setFill(color_rgb(red, green, blue))

        circle.draw(canvas)
    #endfor
        
#random rectangles
def randomRectangles(n):
    # draw n random rect
    for i in range(n):
        # make a random rect
        topX, topY = random.randint(0,w), random.randint(0,h)
        bottomX, bottomY = random.randint(0,w), random.randint(0,h)
        rect = Rectangle(Point(topX, topY), Point(bottomX, bottomY))
        
        # random color and make a color
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        rect.setFill(color_rgb(red, green, blue))

        rect.draw(canvas)
    #endfor

def randomLines(n):
    # draw a random line
    for i in range(n):
        #make a random line
        firstX, firstY = random.randint(0, w), random.randint(0,h)
        lastX, lastY = random.randint(0, w), random.randint(0,h)
        line = Line(Point(firstX, firstY), Point(lastX, lastY))

        # random color and make a color
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        line.setFill(color_rgb(red, green, blue))
        #set width
        line.setWidth(random.randint(5, 20))

        line.draw(canvas)

        
