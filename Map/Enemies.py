import turtle,random

def progression(pos,length,max_hp,cur_hp,color):
    if cur_hp <= 0:
        val = cur_hp
        cur_hp = 0
    turtle.penup()
    turtle.goto(pos)
    turtle.pendown()
    for i in range(2):
        turtle.fd(length)
        turtle.rt(90)
        turtle.fd(10)
        turtle.rt(90)
    turtle.penup()
    new = cur_hp/max_hp * length
    turtle.goto(pos)
    turtle.begin_fill()
    turtle.color(color)
    for i in range(2):
        turtle.fd(new)
        turtle.rt(90)
        turtle.fd(10)
        turtle.rt(90)
    turtle.end_fill()
    turtle.color("black")
    if cur_hp == 0:
        cur_hp = val
    turtle.update()

class Enemies:
    def __init__(self,level,x=50,y=0):
        self.max_hp = random.random()*level*20
        self.cur_hp = self.max_hp
        self.attack = int(random.random()*level*3)
        self.x = x
        self.y = y


class Trash(Enemies):
    def __init__(self,level,x,y):
        Enemies.__init__(self,level,x,y)
        self.color = "yellow"
        self.size = 20
        self.length = 20

    def draw(self):
        turtle.penup()
        turtle.goto(self.x,self.y)
        turtle.color(self.color)
        turtle.dot(self.size)
        pos = (self.x-(self.length//2),self.y + self.size*1.2)
        turtle.color("black")
        progression(pos,self.length,self.max_hp,self.cur_hp,"red")
        turtle.update()


class Boss(Enemies):
    def __init__(self,level,x=50,y=0):
        Enemies.__init__(self, level, x, y)
        self.max_hp = random.random()*level*100
        self.cur_hp = self.max_hp
        self.attack = int(random.random()*level*10)
        self.color = "pink"
        self.size = 50
        self.length = 50

    def draw(self):
        turtle.penup()
        turtle.goto(self.x,self.y)
        turtle.color(self.color)
        turtle.dot(self.size)
        pos = (self.x-(self.length//2),self.y + self.size*1.2)
        turtle.color("black")
        progression(pos,self.length,self.max_hp,self.cur_hp,"red")
        turtle.update()

    def __iter__(self):
        yield self


class Enemy_list:
    def __init__(self,level,num):
        interval = 300 //(num+2)
        y = 150
        self.lst = []
        self.level = level
        for i in range(num):
            y -= interval
            self.lst.append(Trash(level,50,y))

    def draw(self):
        for i in self.lst:
            i.draw()
        turtle.update()

    def __iter__(self):
        for i in self.lst:
            yield i

    def __len__(self):
        return len(self.lst)

class Opponent:
    def __init__(self,level):
        if random.random() > 0.25:
            num = int(random.random()/5 * level // 0.1)
            if num <= 1:
                num = 1
            if num >= 5:
                num = 5
            self.rival = Enemy_list(level,num)
        else:
            self.rival = Boss(level)

    def reset(self,level):
        if random.random() > 0.25:
            num = random.random()/2 * level // 0.1
            if num <= 1:
                num = 1
            self.rival = Enemy_list(level,num)
        else:
            self.rival = Boss(level)
