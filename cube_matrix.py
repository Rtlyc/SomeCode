import math
from numpy import *
import turtle

V = [[1,0,0],
     [0,1,0]]

A = [-1,-1,-1]
B = [1,-1,-1]
C = [1,1,-1]
D = [-1,1,-1]
a = [-1,-1,1]
b = [1,-1,1]
c = [1,1,1]
d = [-1,1,1]
points = [A,B,C,D,a,b,c,d]

def transfer(coordinate):
    ls = []
    for i in coordinate:
        ls.append([i])
    return ls

def line(a,b):
    turtle.penup()
    turtle.goto(a)
    turtle.pendown()
    turtle.goto(b)
    turtle.penup()

turtle.tracer(0,0)
turtle.hideturtle()
turtle.pencolor("purple")
turtle.pensize(3)
angle = 0
size = 100
while True:
    angle += 6
    RotationZ = [[math.cos(math.radians(angle)),math.sin(math.radians(angle)),0],
             [-math.sin(math.radians(angle)),math.cos(math.radians(angle)),0],
             [0,0,1]]
    RotationX = [[1,0,0],
             [0,math.cos(math.radians(angle)),math.sin(math.radians(angle))],
             [0,-math.sin(math.radians(angle)),math.cos(math.radians(angle))]]
    RotationY = [[math.cos(math.radians(angle)),0,-math.sin(math.radians(angle))],
             [0,1,0],
             [math.sin(math.radians(angle)),0,math.cos(math.radians(angle))]]
    turtle.clear()
    pos = []
    for i in points:
        rotated = mat(RotationZ) * mat(transfer(i))
        rotated = mat(RotationX) * rotated
        rotated = mat(RotationY) * rotated
        twod = mat(V) * rotated
        x = twod[0].tolist()[0][0]*size
        y = twod[1].tolist()[0][0]*size
        pos.append((x,y))
    for i in pos:
        turtle.penup()
        turtle.goto(i)
        #turtle.dot(5)
        for j in range(0,4):
            line(pos[j],pos[(j+1)%4])
            line(pos[j+4],pos[(j+1)%4+4])
            line(pos[j],pos[j+4])
        turtle.update()
    


