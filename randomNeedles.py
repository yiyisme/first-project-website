import math
import random
from graphics import *

# create the graphwin object
canvas = GraphWin("Random Graphics", 1000, 700)
canvas.setBackground("lightblue")
w, h = canvas.getWidth(), canvas.getHeight()

# line the horizzontal lines pingxingxian
width = 50
# width shi jiange
for i in range(h//width):
    line = Line(Point(0,i*width), Point(w, i*width))
    line.draw(canvas)
    

# function to draw random
def randomNeedles(n):
    # draw n random circles
    crossNeedle = 0
    for i in range(n):
        # make a random circle
        x0, y0 = random.randint(0,w), random.randint(0,h)
        direction = 2*math.pi*random.random()
        #方向算出来是0~2pi之间的一个数，*弧度制
        x1 = x0 + width * math.cos(direction)
        y1 = y0 + width * math.sin(direction)
        #（题目设定针的长度等于width）。圆周三角函数，焦点横坐标为cosθ，纵坐标为sinθ，再乘边长。
        needle = Line(Point(x0, y0), Point(x1, y1))
        eye = Circle(Point(x0, y0), 5)

        if y0//width != y1//width:
            #！=是不等于。看两个点的y坐标是否在同一个格里。比如y=30，30//50=0,在第0格里。
            #必须取整，因为小数总是不相等，无法判断是否越线
            #intersection
            needle.setOutline("red")
            eye.setOutline("red")
            needle.draw(canvas)
            eye.draw(canvas)
       
        else :
            needle.setOutline("black")
            eye.setOutline("black")
            needle.draw(canvas)
            eye.draw(canvas)
    

        if y0//width != y1//width:
            crossNeedle += 1

    P = crossNeedle / n
    approxPi = 2 / P

    print("crosslineNeedles：", crossNeedle)
    print("P:", P)
    print("approxPi:", approxPi)

        

       
 


        
