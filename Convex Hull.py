import turtle
import math

"""
Convex Hull(Jarvis March Algorithm)
input a coordinate each line, until -1
an example of input:
0 0
60 30
20 80
-30 60
30 10
-20 15
13 40
52 -3
43 43
-30 30
25 6
-15 46
70 32
-1 100
-1
"""
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.out = False
        self.pos = (x,y)
        self.slope = 0

    def __repr__(self):
        return "Point: x:" + str(self.x) + " y:"+ str(self.y)

class Point_lst:
    def __init__(self):
        self.lst = []
        self.solve = []

    def add(self,point):
        self.lst.append(point)

    def __str__(self):
        return self.lst

    def draw_points(self):
        for point in self.lst:
            turtle.penup()
            turtle.goto(point.pos)
            turtle.dot(5)
            #turtle.write(point.pos)

    def outline(self):
        #find out the leftest and the lowest points
        #admit all the points with largest or smallest values are out points
        global low,left
        sortingx = sorted(self.lst, key = lambda x:x.x)
        sortingy = sorted(self.lst, key = lambda y:y.y)
        max_x = sortingx[-1].x
        min_x = sortingx[0].x
        max_y = sortingy[-1].y
        min_y = sortingy[0].y
        low = sortingy[0]
        left = sortingx[0]
        lsx = [max_x,min_x]
        lsy = [max_y,min_y]
        for i in self.lst:
            if i.x in lsx or i.y in lsy:
                i.out = True

    def physics(self):
        #global variable 'left', the leftest point
        #In this method, it determines if the point is out by setting point.out = True
        #Start from the mostleft point –– current, from its point of view, it searches
        #the most left point, and current becomes this point, and keep searching the most-left
        #point, until the next point is the start point(left)
        current = left
        self.solve = [] #reset solve_lst
        while True:
            Next = left
            for point in self.lst:
                if point == current:
                    continue
                v = self.cross_product(current,Next,point)
                if v > 0:# meaning the point is on the left of line(current,Next)
                    Next = point
                    self.solve = [point] # reset the solve_lst as [point]
                elif v == 0:# meaning current,next,point are on the same line
                    # if Next is farther from current than point, add point in solve_lst
                    # otherwise, the Next = point, so the current point will jump to the farther one later
                    if self.distance(current,Next) > self.distance(current,point):
                        self.solve.append(point)
                    else:
                        self.solve.append(Next)
                        Next = point
            #after comparing all the points above, we get the leftest point of current
            for point in self.solve:
                point.out = True
            if Next == left: # if Next point is the start point, the loop breaks
                break
            current = Next   # otherwise, the current point jumps to next point     

    def update(self):#determine the order of the solve_lst by comparing the slope
        #In this method, there is a global variable called 'low', which is the lowest of all points
        self.solve = [] #regard it as an empty list
        for point in self.lst:
            if point.out:
                self.solve.append(point)#if point.out==True, add in solve_lst
        pos = []
        neg = []
        up = []
        for i in self.solve:
            i.slope = self.slope(i,low) #calculate all the slope
            if i is low: # pass the same point
                continue
            #regard low as the origin
            if i.x < low.x:# in the second quadrant
                neg.append(i)
            elif i.x > low.x:# in the first quadrant
                pos.append(i)
            else:
                up.append(i)
        pos = sorted(pos,key = lambda x:x.slope)
        neg = sorted(neg,key = lambda x:x.slope)     
        self.solve =[low] + pos + up + neg #solve_lst is in order          
        
    def slope(self,dot1,dot2):
        if dot1.x == dot2.x:
            return "up"
        return (dot1.y - dot2.y) / (dot1.x - dot2.x)

    def distance(self,point1,point2):# a method to find the distance between two points
        return math.sqrt((point1.x-point2.x) ** 2 + (point1.y-point2.y) ** 2)

    def cross_product(self,point1,point2,point3):#cross product of two vectors
        x1 = point2.x - point1.x
        x2 = point3.x - point1.x
        y1 = point2.y - point1.y
        y2 = point3.y - point1.y
        return x1 * y2 - x2 * y1
        #if the result is less than 0, it means the point3 is on the right of the line(point1,point2)
        #on the other hand, point3 is on the left of the line(point1,point2)

    def draw_outline(self):#connect all the points by sequence
        for i in range(len(self.solve)):
            if i != len(self.solve)-1:
                line(self.solve[i].pos,self.solve[i+1].pos)
        line(self.solve[-1].pos,self.solve[0].pos)

def line(pos1,pos2):#a function to draw a line
    turtle.penup()
    turtle.goto(pos1)
    turtle.pendown()
    turtle.goto(pos2)
    turtle.penup()

def main():
    lst = Point_lst()
    a = input().split()
    while a != ["-1"]:#input until -1
        point = Point(int(a[0]),int(a[1]))
        lst.add(point)
        a = input().split()
    lst.draw_points()
    lst.outline()
    lst.physics()
    lst.update()
    lst.draw_outline()
main()
