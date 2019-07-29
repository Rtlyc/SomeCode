import turtle,random,time
from Queue import Queue

def square(pos,size,color):
    turtle.penup()
    turtle.goto(pos)
    turtle.color(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.fd(size)
        turtle.rt(90)
    turtle.end_fill()

def my_space():
    global b,start
    b.up()
    start = True
    
def frame():
    turtle.penup()
    turtle.pensize(2)
    turtle.color("black")
    turtle.goto(-200,300)
    turtle.pendown()
    for i in range(2):
        turtle.fd(400)
        turtle.rt(90)
        turtle.fd(600)
        turtle.rt(90)
    turtle.penup()
    turtle.goto(0,250)
    turtle.color("darkorange")
    turtle.write(str(score), align="center", font=("Arial", 30, "normal"))

    
class Bird:
    def __init__(self):
        self.size = 30
        self.x = -100
        self.y = 0
        self.t = 0

    def up(self):
        self.y += 50
        self.t = 2

    def draw(self):
        square((self.x,self.y),self.size,"red")
        turtle.update()

    def physics(self):
        if self.t < 15:
            self.t += 1
        self.y -= self.t * 0.8
        
class Tube:
    def __init__(self):
        self.x = 180
        self.y = random.randrange(-150,200,10)
        self.side = 60

class Tube_lst:
    def __init__(self):
        self.q = Queue()
        self.q.enqueue(Tube())
        self.t = 0

    def physics(self):
        if len(self.q) != 0:
            first = self.q.first()
            if first.x <= -200:
                self.q.dequeue()
        self.t += 1
        if self.t % 80 == 0: #过50s加一个tube
            self.q.enqueue(Tube())
        for tube in self.q:
            if tube:
                tube.x -= speed


    def draw(self):
        turtle.color("green")
        for tube in self.q:
            if tube:
                if tube.x <= 200 - tube.side:
                    l = tube.side
                elif 200 >= tube.x > 200 - tube.side:
                    l = 200 - tube.x
                else:
                    continue
                up = (tube.x,tube.y)
                down = (tube.x,tube.y-120) # 空间为120
                turtle.penup()
                turtle.goto(up)
                turtle.pendown()
                turtle.begin_fill()
                turtle.goto(tube.x,300)
                turtle.fd(l) # 宽度为50
                turtle.goto(tube.x+l,tube.y)
                turtle.goto(up)
                turtle.end_fill()

                #画下面的
                turtle.penup()
                turtle.goto(down)
                turtle.pendown()
                turtle.begin_fill()
                turtle.fd(l) # 宽度50
                turtle.goto(tube.x+l,-300)
                turtle.goto(tube.x,-300)
                turtle.goto(down)
                turtle.end_fill()
                turtle.update()
                
def physics():
    global gameover,score
    if not -270 <= b.y <= 300:
        gameover = True
    for tube in lst.q:
        if tube:
            if b.x - tube.side < tube.x <= b.size + b.x:
                if not (tube.y-90<= b.y <= tube.y):
                    gameover = True
            elif  0 <= b.x-tube.x-tube.side < speed:
                score += 1

def main():
    global b,gameover,lst,score,speed,start
    start = False
    speed = 10
    score = 0
    gameover = False
    turtle.hideturtle()
    turtle.onkey(my_space,"space")
    turtle.listen()
    turtle.tracer(0,0)
    b = Bird()
    lst = Tube_lst()
    while not gameover:
        turtle.clear()
        frame()
        if start:
            b.physics()
            lst.physics()
            lst.draw()
            physics()
        b.draw()
        time.sleep(0.05)
        
main()

        
