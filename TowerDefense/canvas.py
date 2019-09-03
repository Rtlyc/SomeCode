import turtle,random

def rectangle(length,width):
    for i in range(2):
        turtle.fd(length)
        turtle.rt(90)
        turtle.fd(width)
        turtle.rt(90)

def frame(): #绘制大地图
    turtle.color("black")
    turtle.penup()
    turtle.goto(-300,300)
    turtle.pendown()
    for i in range(2):
        turtle.fd(600)
        turtle.rt(90)
        turtle.fd(400)
        turtle.rt(90)
    turtle.penup()
    # green bottle########
    turtle.goto(-100,-120)
    turtle.pendown()
    turtle.color("green")
    rectangle(20,40)
    turtle.penup()
    turtle.goto(-100,-180)
    turtle.write("Q: Bottle(10)",font = 30)
    # Sun #####
    turtle.penup()
    turtle.goto(-20,-120)
    turtle.pendown()
    turtle.color("purple")
    rectangle(20, 40)
    turtle.penup()
    turtle.goto(-20, -180)
    turtle.write("W: Sun(10)", font=30)
    turtle.color("black")
    ##Plane ##########
    turtle.penup()
    turtle.goto(60, -120)
    turtle.pendown()
    turtle.color("gold")
    rectangle(20, 40)
    turtle.penup()
    turtle.goto(60, -180)
    turtle.write("E: Plane(15)", font=30)
    ##Firebottle########
    turtle.penup()
    turtle.goto(140, -120)
    turtle.pendown()
    turtle.color("tomato")
    rectangle(20, 40)
    turtle.penup()
    turtle.goto(140, -180)
    turtle.write("R: FireBottle(15)", font=30)
    ###########
    turtle.color("black")
    #turtle.update()
    turtle.penup()
    turtle.goto(-150,-100)
    turtle.pendown()
    rectangle(450,200)
    turtle.penup()


class Map:
    class Block:
        def __init__(self, loc=None, path=False):
            self.loc = loc
            self.x = None  # 左上角坐标
            self.y = None
            self.path = path  # 怪物路线
            self.tower = False
            # self.color = "yellow"

        def __repr__(self):
            return str(self.loc) + str(self.path)

        def draw(self):
            turtle.penup()
            turtle.goto(self.x, self.y)
            turtle.pendown()
            turtle.color("darkblue")
            # if self.path:
            #             #     turtle.color("lightblue")
            #             #     turtle.begin_fill()
            rectangle(60, 50)
            turtle.end_fill()
            turtle.color("black")
            #turtle.write(str(self), font=10)
            turtle.penup()

    def __init__(self):
        self.lst = []
        self.path = []
        for y in range(8):
            ls = []
            for x in range(10):
                block = Map.Block(y * 10 + x)
                block.x = -300 + 60 * x
                block.y = 300 - 50 * y
                ls.append(block)
            self.lst.append(ls)

    def first_block(self):
        if self.path == []:
            raise Exception("The map has not reset yet!")
        return self.path[0][0]

    def reset(self):
        # in this function, the map randomly created a map
        # 1.randomly select a start point
        # 2.check the surroundings(except the left)
        # 3.randomly select a block from the surroundings
        # 4.cur_block move, mark the block
        # 5.if the cur_block has no right, stop the loop
        def random_start():
            front = []
            for line in self.lst:
                front.append(line[0])
            return random.choice(front)

        cur_block = random_start()
        cur_block.path = True
        self.path.append((cur_block, "right"))
        while self.right(cur_block):
            surround_blocks = self.surroundings(cur_block)
            next_block, direction = random.choice(surround_blocks)
            next_block.path = True
            self.path.append((next_block, direction))
            cur_block = next_block

    def loc_to_block(self, loc):
        x = loc % 10
        y = loc // 10
        try:
            block = self.lst[y][x]
        except:
            return
        return block

    def right(self, block):
        loc = block.loc
        x = loc % 10 + 1
        y = loc // 10
        try:
            block = self.lst[y][x]
        except:
            return
        return block

    def up(self, block):
        loc = block.loc
        x = loc % 10
        y = loc // 10 - 1
        if y < 0:
            return
        block = self.lst[y][x]
        return block

    def down(self, block):
        loc = block.loc
        x = loc % 10
        y = loc // 10 + 1
        try:
            block = self.lst[y][x]
        except:
            return
        return block

    def surroundings(self, block):
        # except left
        # except color == white
        surround_lst = []
        loc = block.loc
        x = loc % 10
        y = loc // 10
        up_block = self.up(block)
        down_block = self.down(block)
        right_block = self.right(block)
        if up_block and (not up_block.path):
            surround_lst.append((up_block, "up"))
        if down_block and (not down_block.path):
            surround_lst.append((down_block, "down"))
        if right_block and (not right_block.path):
            surround_lst.append((right_block, "right"))
        return surround_lst

    def coor_to_block(self, x, y):
        b = int(5 - y // 50)
        a = int(x // 60 + 5)
        return self.lst[b][a]

    def draw(self):
        for i in self.lst:
            for j in i:
                if j.path:
                    j.draw()
        #turtle.update()





