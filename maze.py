import turtle
import random

class Dot:
    def __init__(self, value):
        self.value = value
        self.size = 15
        self.loc = -1
        self.track = False
        if value == 0:
            self.color = "grey"
        else:
            self.color = "yellow"

    def __str__(self):
        return "value: "+ str(self.value) + ", color: " + str(self.color) + ", loc:" + str(self.loc)
    
    def change_to_red(self):
        self.color = "red"

    def change_to_blue(self):
        self.color = "blue"

    def change_to_grey(self):
        self.color = "grey"

class Board:
    def __init__(self,size):
        self.num = size * 2 + 1
        big_lst = []
        self.solve_lst = []
        for j in range(self.num):
            small_lst = []
            if j % 2 == 0:
                for i in range(self.num):
                    small_lst.append(Dot(0))
            else:
                for i in range(self.num):
                    if i % 2 == 0:
                        small_lst.append(Dot(0))
                    else:
                        small_lst.append(Dot(1))
            big_lst.append(small_lst)
        self.lst = big_lst
        no = 0
        for y in range(self.num):
            for x in range(self.num):
                self.lst[y][x].loc = no
                no += 1

    def draw(self):#画地图
        for y in range(self.num):
            for x in range(self.num):
                if self.lst[y][x].color == "red":
                    pos = (x * self.lst[y][x].size-300,y * self.lst[y][x].size-300)
                    square(pos,self.lst[y][x].size,"white")
                elif self.lst[y][x].color == "grey":
                    pos = (x * self.lst[y][x].size-300,y * self.lst[y][x].size-300)
                    square(pos,self.lst[y][x].size,"black")
                #turtle.write(self.lst[y][x].loc)#
                if self.Up(self.lst[y][x]) == start_point:
                    square(pos,self.lst[y][x].size,"white")
                elif self.Down(self.lst[y][x]) == end_point:
                    square(pos,self.lst[y][x].size,"white")
                if answer:
                    if self.lst[y][x] in self.solve_lst:
                        pos = (x * self.lst[y][x].size-300,y * self.lst[y][x].size-300)
                        square(pos,self.lst[y][x].size,"purple")
                    if self.Up(self.lst[y][x]) == start_point:
                        square(pos,self.lst[y][x].size,"purple")
                    elif self.Down(self.lst[y][x]) == end_point:
                        square(pos,self.lst[y][x].size,"purple")


    def num_to_dot(self,num):#数字转换为Dot
        for i in self.lst:
            for j in i:
                if j.loc == num:
                    return j
        return -1

    def Up(self,dot):#找到dot的向上一位dot
        return self.num_to_dot(dot.loc + self.num)

    def Right(self,dot):#找到dot的向右一位dot
        return self.num_to_dot(dot.loc + 1)

    def Left(self,dot):#找到dot的向左一位dot
        return self.num_to_dot(dot.loc - 1)

    def Down(self,dot):#找到dot的向下一位dot
        return self.num_to_dot(dot.loc - self.num)

    def is_border(self,dot):#判断dot是否为边界
        x = list(range(0,self.num))
        for i in self.lst[-1]:
            x.append(i.loc)
        for i in range(self.num,self.num*(self.num-1)):
            if i % self.num == 0 or (i+1) % self.num == 0:
                x.append(i)
        return dot.loc in x

    def surroundings(self,dot):#周围四个dot
        return self.Up(dot),self.Down(dot),self.Left(dot),self.Right(dot)

    def all_blue(self):
        lst = []
        for i in self.lst:
            for j in i:
                if j.color == "blue":
                    lst.append(j)
        return lst

    def physics(self):
        global start_point,end_point,trace
        #1.随机取第二行黄色
        #2.黄-》红 周围三个 灰-》蓝
        #3.随机所有蓝色，确定旁边红色的1，做反向操作确定dot，如果为黄色1继续
        #4.黄-》红 灰0 -》红 周围三个 灰色-》蓝，蓝-》灰
        #5。没有蓝色就终止
        
        #1.随机取第二行黄色
        trace = []
        ls1 = []
        for i in self.lst[1]:
            if i.color == "yellow":
                ls1.append(i)
        dot = random.choice(ls1)

        #2.黄-》红 周围三个 灰-》蓝
        dot.change_to_red()
        ls2 = [self.Up(dot),self.Left(dot),self.Right(dot)]
        for i in ls2:
            if not self.is_border(i):
                i.change_to_blue()

        #3.随机所有蓝色
        blue_lst = self.all_blue()
        dot_pre = dot
        print("start_point",dot_pre)
        while blue_lst != []:
            dot0 = random.choice(blue_lst)
            for i in self.surroundings(dot0):
                if i.color == "red":
                    dot_pre = i
            dot1 = self.num_to_dot(2*dot0.loc - dot_pre.loc)
            if dot1 != -1:
                if dot1.color == "yellow":#判断跳级为正确
                    dot1.change_to_red()
                    dot0.change_to_red()
                    for i in self.surroundings(dot1):
                        if self.is_border(i):
                            continue
                        elif i.color == "grey":
                            i.change_to_blue()
                        elif i.color == "blue":
                            i.change_to_grey()
                blue_lst = self.all_blue()
                trace.append(dot0)
                trace.append(dot1)
            if self.is_border(self.Up(dot1)):
                end_point = dot1
        print("end_point",end_point)
        start_point = dot
        start_point.track = True
        self.solve_lst.append(start_point)

    def solve(self,dot):
        dot.track = True
        if dot.loc == end_point.loc:
            self.solve_lst.append(dot)
            return True
        for i in self.surroundings(dot):
            if i.track:
                continue
            if i.color == "red":
                i.track = True
                if self.solve(i) == True:
                    self.solve_lst.append(i)
                    return True
        return False
                
        
def square(pos,size,color):
    turtle.penup()
    turtle.goto(pos)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.fd(size)
        turtle.lt(90)
    turtle.color(color)
    turtle.end_fill()
    turtle.color("black")
    turtle.penup()

def my_space():
    global answer
    answer = not answer
    print(answer)

def main():
    global answer
    answer = False
    turtle.onkey(my_space,"space")
    turtle.listen()
    turtle.tracer(0,0)
    turtle.hideturtle()
    b = Board(20)
    b.physics()
    while True:
        turtle.clear()
        b.draw()
        if answer:
            b.solve(start_point)
        turtle.update()
        
main()


    

