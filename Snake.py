import turtle
import time
import random
import math

class Object:
    def __init__(self):
        self.x = random.randint(-350,350)
        self.y = random.randint(-335,335)
        self.size = random.randint(10,20)
        self.borntime = t

class Enemies_list:
    def __init__(self):
        self.lst = []

    def add(self,enemy):
        self.lst.append(enemy)

    def remove(self,enemy):
        if not self.lst == []:
            self.lst.remove(enemy)

    def update(self):#更新敌人
        r = random.random()
        chance = math.pow(t,0.2)
        for enemy in self.lst:
            if t - enemy.borntime >= 300:
                self.remove(enemy)
        o = Object()
        if r < 0.01 * chance:
            self.add(o)

    def draw(self):
        for i in self.lst:
            turtle.penup()
            turtle.goto(i.x,i.y)
            turtle.color("red")
            turtle.dot(i.size)
            turtle.color("black")

class Foods_list:
    def __init__(self):
        self.lst = []

    def add(self,food):
        self.lst.append(food)


    def eat(self,food):
        self.lst.remove(food)

    def update(self): #更新食物
        r = random.random()
        for food in self.lst:
            if t - food.borntime >= 300:
                self.eat(food)
        o = Object()
        if r > 0.95:
            self.add(o)

    def draw(self):
        for i in self.lst:
            turtle.penup()
            turtle.goto(i.x,i.y)
            turtle.color("green")
            turtle.dot(i.size)
            turtle.color("black")



class Snake:
    # Snake head(x,y) there is a list to hold all the bodies part
    #global t
    def __init__(self):
        self.headx = 0
        self.heady = 0
        self.size = 20
        self.direction = "Right"
        self.body = [(self.headx,self.heady)]
        self.velocity = 3

    def add(self):#增加身体长度
        if self.direction == "Right":   
            position = (self.last_body()[0]-self.velocity,self.last_body()[1])
        elif self.direction == "Left":   
            position = (self.last_body()[0]+self.velocity,self.last_body()[1])
        elif self.direction == "Up":   
            position = (self.last_body()[0],self.last_body()[1]-self.velocity)
        elif self.direction == "Down":
            position = (self.last_body()[0],self.last_body()[1]+self.velocity)
        self.body.append(position)

        
    def direction_change(self,direction):#更改方向
        limit = [("Left","Right"),("Up","Down")]
        for i in limit:
            if (self.direction in i) and (direction not in i):      
                self.direction = direction
        return self.direction

    def last_body(self):#给出最后一项
        return self.body[-1]

    def update_velocities(self):
        self.velocity = math.pow(t,0.3)
        return self.velocity

    def update_positions(self):
        head = self.body[0]
        if self.direction == "Right":
            new_body = [(head[0]+self.velocity,head[1])]
        elif self.direction == "Left":
            new_body = [(head[0]-self.velocity,head[1])]
        elif self.direction == "Up":
            new_body = [(head[0],head[1]+self.velocity)]
        elif self.direction == "Down":
            new_body = [(head[0],head[1]-self.velocity)]
        for i in self.body[:-1]:
            new_body.append(i)
        self.body = new_body
        self.headx = self.body[0][0]
        self.heady = self.body[0][1]

    def draw(self):
        turtle.begin_fill()
        turtle.color("black")
        self.square((self.headx,self.heady))
        turtle.end_fill()
        turtle.color("blue")
        for i in self.body[1:]:
            turtle.begin_fill()
            self.square(i)
            turtle.end_fill()

    def square(self,pos):
        turtle.penup()
        turtle.goto(pos)
        turtle.pendown()
        for i in range(4):
            turtle.fd(self.size)
            turtle.lt(90)
        turtle.penup()

def physics():#如果吃到food增长 吃到enemy判断死亡 超过边界死亡
    global enemies,foods,gameover,s,score
    if not -350 <= s.headx <= 350:
        gameover = True
        print("Outside")
        return
    if not -335 <= s.heady <= 335:
        gameover = True
        print("Outside")
        return
    for enemy in enemies.lst:
        if s.direction == "Up":
            if -enemy.size < enemy.x - s.headx < enemy.size + s.size and s.size < enemy.y - s.heady < enemy.size+s.size:
                gameover = True
                return
        elif s.direction == "Down":
            if -enemy.size < enemy.x - s.headx < enemy.size+s.size and -enemy.size < enemy.y - s.heady < 0:
                gameover = True
                return
        elif s.direction == "Right":
            if s.size < enemy.x - s.headx < s.size + enemy.size and -enemy.size < enemy.y - s.heady < enemy.size+s.size:
                gameover = True
                return
        elif s.direction == "Left":
            if -enemy.size < enemy.x -s.headx < 0 and -enemy.size < enemy.y-s.heady < enemy.size+s.size:
                gameover = True
                return
        
    for food in foods.lst:
        if s.direction == "Up":
            if -food.size < food.x - s.headx < food.size + s.size and s.size < food.y - s.heady < food.size+s.size:
                s.add()
                foods.eat(food)
                score += 1
        elif s.direction == "Down":
            if -food.size < food.x - s.headx < food.size+s.size and -food.size < food.y - s.heady < 0:
                s.add()
                foods.eat(food)
                score += 1
        elif s.direction == "Right":
            if s.size < food.x - s.headx < s.size + food.size and -food.size < food.y - s.heady < food.size+s.size:
                s.add()
                foods.eat(food)
                score += 1
        elif s.direction == "Left":
            if -food.size < food.x -s.headx < 0 and -food.size < food.y-s.heady < food.size+s.size:
                s.add()
                foods.eat(food)
                score += 1
    if len(s.body) == 1:
        return
    
    if s.direction == "Right":
        for i in s.body:
            if 0 < i[0] - s.headx < s.size and -s.size < s.heady - i[1] < s.size:
                print("eat self,right")
                gameover = True

    elif s.direction == "Left":
        for i in s.body:
            if 0 < s.headx - i[0] < s.size and -s.size < s.heady - i[1] < s.size:
                print("eat self,left")
                gameover = True

    elif s.direction == "Up":
        for i in s.body:
            if -s.size < s.headx - i[0] < s.size and 0 < i[1] - s.heady < s.size:
                print("eat self,up")
                gameover = True

    elif s.direction == "Down":
        for i in s.body:
            if -s.size < s.headx - i[0] < s.size and 0 < s.heady - i[1] < s.size:
                print("eat self,down")
                gameover = True

def draw_score():
    turtle.penup()
    turtle.goto(-350,300)
    turtle.write("Score: " + str(score) , font=("Arial", 20, "normal"))
    
def key_up():
    global direct
    direct = "Up"
    return direct

def key_down():
    global direct
    direct = "Down"
    return direct

def key_left():
    global direct
    direct = "Left"
    return direct

def key_right():
    global direct
    direct = "Right"
    return direct

global enemies,foods,gameover,t,score
t = 0
enemies = Enemies_list()
foods = Foods_list()
gameover = False
s = Snake()
score = 0

def main():
    global direct,enemies,foods,gameover,s,t
    direct = "Right"
    turtle.tracer(0,0)
    turtle.hideturtle()
    turtle.onkey(key_left,"Left")
    turtle.onkey(key_right,"Right")
    turtle.onkey(key_up, "Up")
    turtle.onkey(key_down, "Down")
    turtle.listen()

    while not gameover:
        turtle.clear()
        physics()
        enemies.draw()
        foods.draw()
        s.direction_change(direct)
        s.draw()
        draw_score()
        s.update_velocities()
        s.update_positions()
        enemies.update()
        foods.update()
        turtle.update()
        time.sleep(0.05)
        t += 1

main()
