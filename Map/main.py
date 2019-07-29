import turtle,random,math,time
from Character import Character
from Enemies import Enemies,Trash,Enemy_list,Boss,Opponent
from Store import heart,sword,leave


def progression(pos,length,max_hp,cur_hp,color):
    turtle.penup()
    turtle.goto(pos)
    turtle.pendown()
    if cur_hp < 0:
        cur_hp = 0
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
    turtle.update()

def frame():
    global hero
    turtle.penup()
    turtle.goto(-200,150)
    turtle.pendown()
    turtle.color("black")
    for i in range(2):
        turtle.fd(400)
        turtle.rt(90)
        turtle.fd(300)
        turtle.rt(90)
    turtle.penup()
    turtle.goto(-320,-200)
    turtle.write("Level: " + str(hero.level), align="left", font=("Arial", 20, "normal"))
    turtle.goto(-320,-220)
    turtle.write("HP: ", align="left", font=("Arial", 20, "normal"))
    progression((-280,-205),50,hero.max_hp,hero.cur_hp,"red")
    turtle.goto(-270,-215)
    turtle.write(str(hero.cur_hp)+" / "+str(hero.max_hp), align="left", font=("Arial", 10, "normal"))
    turtle.goto(-320, -240)
    turtle.write("EP: ", align="left", font=("Arial", 20, "normal"))
    progression((-280,-225),50,hero.max_ep,hero.cur_ep,"yellow")
    turtle.goto(-270, -235)
    turtle.write(str(hero.cur_ep) + " / " + str(hero.max_ep), align="left", font=("Arial", 10, "normal"))
    turtle.goto(-320,-260)
    turtle.write("Money: " + str(hero.money), align="left", font=("Arial", 20, "normal"))
    turtle.goto(-320, -280)
    turtle.write("Attack: "+ str(hero.attack), align="left", font=("Arial", 20, "normal"))
    turtle.update()


def five(pos,size,color):
    turtle.penup()
    turtle.goto(pos)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for i in range(5):
        turtle.fd(size)
        turtle.rt(144)
    turtle.end_fill()
    turtle.color("black")
    turtle.penup()


def reaction(item):#攻击敌人
    global hero
    # if not (into or myturn):
    #     return
    dx = (item.x - hero.x) // 20
    dy = (item.y - hero.y) // 20
    def move():
        for i in range(20):
            turtle.clear()
            hero.x += dx
            hero.y += dy
            hero.draw()
            turtle.update()
        for i in range(20):
            turtle.clear()
            hero.x -= dx
            hero.y -= dy
            hero.draw()
            turtle.update()
    move()
    attack = random.randrange(hero.attack[0],hero.attack[1])
    item.cur_hp -= attack
    turtle.clear()
    turtle.update()

def enemyattack():
    global hero,gameover,myturn,finish,opponent,into
    if myturn:
        return
    rival = opponent.rival
    for item in rival:
        if item.cur_hp > 0:
            break
    else:
        turtle.clear()
        if isinstance(rival,Boss):
            hero.cur_ep += hero.max_ep
            hero.money += 10
        else:
            plus = rival.level * len(rival) * 5
            hero.cur_ep += plus
            hero.money += 2 * len(rival)
        into = False
        myturn = True
        turtle.clear()
        turtle.update()
        return # 战争结束
    for item in rival:#群体
        if item.cur_hp <= 0:
            continue
        dx = (item.x - hero.x) // 20
        dy = (item.y - hero.y) // 20
        def move(item):
            for i in range(20):
                turtle.clear()
                item.x -= dx
                item.y -= dy
                item.draw()
                turtle.update()
            for i in range(20):
                turtle.clear()
                item.x += dx
                item.y += dy
                item.draw()
                turtle.update()
        move(item)
        hero.cur_hp -= item.attack
        if hero.cur_hp <= 0:
            gameover = True
            return
    myturn = True




def my_click(clickx,clicky):
    global myturn,store,hero
    if myturn and into:
        if isinstance(opponent.rival,Boss):
            boss = opponent.rival
            if (clickx - boss.x)**2 + (clicky-boss.y)**2 <= boss.size**2:
                reaction(boss)
                myturn = False
        else:
            for trash in opponent.rival:
                if (clickx - trash.x)**2 + (clicky-trash.y)**2 <= trash.size**2:
                    reaction(trash)
                    myturn = False
        turtle.clear()
    elif store:
        if 40 < clickx < 160 and 20 < clicky < 140:
            if hero.money >= 15:
                hero.money -= 15
                hero.max_hp += 50
                hero.cur_hp += 50
                frame()
        elif -155 < clickx < -35 and 20 < clicky < 140:
            if hero.money >= 15:
                hero.money -= 15
                hero.attack = (hero.attack[0]+15,hero.attack[1]+15)
                frame()
        elif -30 < clickx < 30 and -40 < clicky < -20:
            store = False
            turtle.clear()
    turtle.update()


###################################
def square(pos,color):
    turtle.penup()
    turtle.goto(pos)
    turtle.color(color)
    for i in range(4):
        turtle.fd(60)
        turtle.rt(90)
    turtle.update()


class Block:
    def __init__(self,loc = None):
        self.visit = False
        self.loc = loc
        self.path = False
        self.store = False
        if random.random()>0.2:
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
        k = self.loc_to_block(random.randrange(0,16))
        k.store = True

    def draw(self):
        for i in range(4):
            for j in range(4):
                pos = (-200+100*j,150-75*i)
                turtle.begin_fill()
                cur = self.lst[i][j]
                if cur.visit:
                    square(pos,"grey")
                elif cur.path:
                    square(pos,"blue")
                else:
                    square(pos,"green")
                turtle.end_fill()
                if cur.store:
                    five((pos[0]+10,pos[1]-25),40,"purple")
                turtle.update()
                turtle.color("black")
                #turtle.write(str(cur))
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
        pos = (-170+100*x,120-75*y)
        turtle.goto(pos)
        turtle.color("white")
        turtle.dot(30)
        turtle.color("black")
        turtle.update()

def map_move():
    global circle, m, into, direct
    if direct:
        try:
            if direct == "Left":
                k = m.loc_to_block(circle.loc - 1)
                if not (k.loc // 4 == circle.loc // 4):
                    raise IndexError
                if k.visit or k.path:
                    circle.loc -= 1
            elif direct == "Right":
                k = m.loc_to_block(circle.loc + 1)
                if not (k.loc // 4 == circle.loc // 4):
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


def my_up():
    global direct
    direct = "Up"

def my_down():
    global direct
    direct = "Down"

def my_space():
    global into,m,hero,store
    turtle.clear()
    k = m.loc_to_block(circle.loc)
    if k.store:
        store = True
    elif not (into or k.visit):
        if k.fight:
            into = True
            turtle.clear()
            update()
        else:
            hero.recover()
            hero.cur_ep += 20
            hero.update()
        turtle.update()
        m.surroundings(m.loc_to_block(circle.loc))
    k.visit = True

def my_left():
    global direct
    direct = "Left"

def my_right():
    global direct
    direct = "Right"


def reset():
    global hero, lst, boss, myturn, gameover, finish, opponent, level
    global circle, m, direct, into, store
    store = False
    into = False
    direct = None
    circle = Circle()
    m = Map()
    level = 1
    finish = False
    gameover = False
    myturn = True
    # lst = Enemy_list(1,2)
    hero = Character()
    opponent = Opponent(level)
    # boss = Boss(3)
    # boss = None


def update():  # 更新敌人
    global level, opponent
    level += 1
    opponent = Opponent(level)


def scene1():
    map_move()
    m.draw()
    circle.draw()


def scene2():
    enemyattack()
    hero.update()
    hero.draw()
    opponent.rival.draw()

def scene3():
    sword((-100, 20))
    heart((100, 40))
    leave((-30, -20))


def main():
    global into,store
    turtle.onkey(my_down, "Down")
    turtle.onkey(my_up, "Up")
    turtle.onkey(my_right, "Right")
    turtle.onkey(my_left, "Left")
    turtle.onkey(my_space, "space")
    turtle.onscreenclick(my_click)
    turtle.listen()
    reset()
    turtle.tracer(0,0)
    turtle.hideturtle()
    turtle.pensize(2)
    while not gameover:
        turtle.update()
        if store:
            scene3()
        elif not into:
            scene1()
        else:
            scene2()
        frame()
        turtle.update()
        time.sleep(0.25)
    turtle.done()

main()
