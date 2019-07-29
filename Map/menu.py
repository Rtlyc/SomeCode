import turtle,random,math,time

def square(pos,color,size):
    turtle.penup()
    turtle.goto(pos)
    turtle.color(color)
    for i in range(4):
        turtle.fd(size)
        turtle.rt(90)


class Block:
    def __init__(self,loc = None):
        self.visit = False
        self.loc = loc
        self.path = False
        if random.random()>0.5:
            self.fight = True
        else:
            self.fight = False

    def update(self):
        if self.fight:
            pass
        else:
            pass

    def __repr__(self):
        return "loc: "+ str(self.loc)+" visit: "+ str(self.visit) +" fight: "+str(self.fight)

class Map:
    def __init__(self):
        self.lst = []
        self.grey = []
        self.blue = []
        for j in range(4):
            lst = []
            for i in range(4):
                k = Block(i+j*4)
                lst.append(k)
            self.lst.append(lst)

    def draw(self):
        for i in range(4):
            for j in range(4):
                pos = (-200+100*j,150-75*i)
                turtle.begin_fill()
                cur = self.lst[i][j]
                if cur.visit:
                    square(pos,"grey",60)
                elif cur.path:
                    square(pos,"blue",60)
                else:
                    square(pos,"green",60)
                turtle.end_fill()
                turtle.color("black")
                turtle.write(str(cur))
                turtle.update()

    def loc_to_block(self,loc):
        if not 0 <= loc <= 15:
            return
        x = loc % 4
        y = loc // 4
        return self.lst[y][x]

    def surroundings(self,block):
        loc = block.loc
        lst = []
        sur = (-1,1,-4,4)
        for i in range(2):
            try:
                k = self.loc_to_block(loc + sur[i])
                if k:
                    if not (k.loc // 4 == circle.loc // 4):
                        raise IndexError
                    lst.append(k)
            except:
                pass
        for i in range(2,4):
            try:
                k = self.loc_to_block(loc + sur[i])
                if k:
                    lst.append(k)
            except:
                pass
        for i in lst:
            if not i.visit:
                i.path = True

    def is_visited(self):
        self.grey = []
        self.blue = []
        for i in range(4):
            for j in range(4):
                block = self[i][j]
                if block.visit:
                    self.grey.append(block)
                elif block.path:
                    self.blue.append(block)
        return

    def __getitem__(self, item):
        return self.lst[item]

    def __iter__(self):
        for i in range(4):
            for j in range(4):
                yield self[i][j]

class Circle:
    def __init__(self):
        self.loc = 0

    def draw(self):
        x = self.loc % 4
        y = self.loc // 4
        loc = (-170+100*x,120-75*y)
        turtle.goto(loc)
        turtle.color("white")
        turtle.dot(30)
        turtle.color("black")

def map_move():
    global circle,m,into,direct
    if direct:
        try:
            if direct == "Left":
                k = m.loc_to_block(circle.loc-1)
                if not (k.loc //4 == circle.loc//4):
                    raise IndexError
                if k.visit or k.path:
                    circle.loc -= 1
            elif direct == "Right":
                k = m.loc_to_block(circle.loc + 1)
                if not (k.loc //4 == circle.loc//4):
                    raise IndexError
                if k.visit or k.path:
                    circle.loc += 1
            elif direct == "Up":
                k = m.loc_to_block(circle.loc - 4)
                if k.visit or k.path:
                    circle.loc -= 4
            elif direct == "Down":
                k = m.loc_to_block(circle.loc + 4)
                if k.visit or k.path:
                    circle.loc += 4
            direct = None
        except:
            direct = None
            return
    into = False


def my_up():
    global direct
    direct = "Up"

def my_down():
    global direct
    direct = "Down"

def my_space():
    global into,m
    into = not into
    m.surroundings(m.loc_to_block(circle.loc))
    k = m.loc_to_block(circle.loc)
    k.visit = True

def my_left():
    global direct
    direct = "Left"

def my_right():
    global direct
    direct = "Right"

def scene1():
    map_move()
    m.draw()
    circle.draw()

def main():
    global circle,m,direct,into
    into = False
    direct = None
    turtle.onkey(my_down,"Down")
    turtle.onkey(my_up,"Up")
    turtle.onkey(my_right,"Right")
    turtle.onkey(my_left,"Left")
    turtle.onkey(my_space,"space")
    turtle.listen()
    circle = Circle()
    turtle.tracer(0,0)
    turtle.update()
    turtle.hideturtle()
    m = Map()

    while True:
        map_move()
        m.draw()
        circle.draw()
        turtle.update()
        time.sleep(0.25)
    turtle.done()

main()
