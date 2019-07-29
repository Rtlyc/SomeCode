import turtle,random,time

global left,right,up,down,score,move
left,right,up,down = False,False,False,False
score = 0
move = False

class Square:
    def __init__(self):
        self.number = None
        self.loc = -1

    def __repr__(self):
        return "number: "+str(self.number)+"  loc: "+str(self.loc)

def draw_square(pos,size,color):
    turtle.pensize(3)
    turtle.penup()
    turtle.goto(pos)
    turtle.color(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.fd(size)
        turtle.rt(90)
    turtle.end_fill()
    turtle.color("black")
    turtle.pendown()
    for i in range(4):
        turtle.fd(size)
        turtle.rt(90)

def write_num(pos,pensize,content):
    turtle.penup()
    turtle.goto(pos)
    turtle.color("black")
    turtle.write(content, align="center", font=("Arial", pensize, "normal"))
    
dic = {None:"white",2:"bisque",4:"navajowhite",8:"lightsalmon",16:"sandybrown",32:"coral"
       ,64:"red",128:"orange",256:"goldenrod",512:"cornsilk",1024:"gold",2048:"purple"}
class Board:
    def __init__(self):
        self.lst = []
        k = 0
        for i in range(4):
            ls = []
            for j in range(4):
                c = Square()
                ls.append(c)
                c.loc = k
                k += 1
            self.lst.append(ls)
        

    def draw(self):
        write_num((-250,250),15,str(score))        
        for y in range(4):
            for x in range(4):
                pos = (-200+x*100,200-y*100)
                center = (pos[0]+50,pos[1]-50)
                k = self.lst[y][x]
                draw_square(pos,100,dic[k.number])
                if k.number != None:
                    write_num(center,30,str(k.number))
                turtle.update()

    def random_create(self):
        lst = []
        for i in range(4):
            for j in range(4):
                if self.lst[i][j].number == None:
                    lst.append(self.lst[i][j])
        try:
            k = random.choice(lst)
            k.number = 2
        except:
            pass

    def right(self):
        global right,score
        right = False
        for m in range(4):
            line = self.lst[m]
            for k in range(3,-1,-1):
                if line[k].number != None:
                    try:
                        s = k - 1
                        while line[s].number == None and s > 0:
                            s -= 1
                        if line[k].number == line[s].number and s >= 0:
                            line[k].number *= 2
                            line[s].number = None
                            score += line[k].number
                    except:
                        pass
                    
                    try:
                        while line[k+1].number == None:
                            line[k+1].number = line[k].number
                            line[k].number = None
                            k += 1
                    except:
                        pass

    def left(self):
        global left,score,move
        left = False
        for m in range(4):
            line = self.lst[m]
            for k in range(4):
                if line[k].number != None:
                    try:
                        s = k + 1
                        while line[s].number == None:
                            s += 1
                        if line[k].number == line[s].number:
                            line[k].number *= 2
                            line[s].number = None
                            score += line[k].number
                            move = True
                    except:
                        pass
                    
                    try:
                        while line[k-1].number == None and k > 0:
                            line[k-1].number = line[k].number
                            line[k].number = None
                            k -= 1
                            move = True
                    except:
                        pass


    def up(self):
        global up,score,move
        up = False
        for m in range(4):
            ls = [self.lst[0][m],self.lst[1][m],self.lst[2][m],self.lst[3][m]]
            for i in range(4):
                if ls[i].number != None:
                    try:
                        s = i + 1
                        while ls[s].number == None:
                            s += 1
                        if ls[i].number == ls[s].number:
                            ls[i].number *= 2
                            ls[s].number = None
                            score += ls[i].number
                            move = True
                    except:
                        pass
                    try:
                        while ls[i-1].number == None and i > 0:
                            ls[i-1].number = ls[i].number
                            ls[i].number = None
                            i -= 1
                            move = True
                    except:
                        pass




    def down(self):
        global down,score,move
        down = False
        for m in range(4):
            ls = [self.lst[0][m],self.lst[1][m],self.lst[2][m],self.lst[3][m]]
            for i in range(3,-1,-1):
                if ls[i].number != None:
                    try:
                        s = i - 1
                        while ls[s].number == None and s > 0:
                            s -= 1
                        if ls[i].number == ls[s].number and s >= 0:
                            ls[i].number *= 2
                            ls[s].number = None
                            score += ls[i].number
                            move = True
                    except:
                        pass
                    try:
                        while ls[i+1].number == None:
                            ls[i+1].number = ls[i].number
                            ls[i].number = None
                            i += 1
                            move = True
                    except:
                        pass
                          

def my_left():
    global left
    left = True

def my_right():
    global right
    right = True

def my_up():
    global up
    up = True

def my_down():
    global down
    down = True


def main():
    global left,right,up,down,score,move
    b = Board()
    turtle.hideturtle()
    turtle.onkey(my_left,"Left")
    turtle.onkey(my_right,"Right")
    turtle.onkey(my_up,"Up")
    turtle.onkey(my_down,"Down")
    turtle.listen()
    turtle.tracer(0,0)
    b.random_create()
    while True:
        if move:
            b.random_create()
            move = False
            turtle.clear()
        if right:
            b.right()
        if left:
            b.left()
        if down:
            b.down()
        if up:
            b.up()
        b.draw()

        
        
    
    
    
main()
        
        
