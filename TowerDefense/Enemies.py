import turtle,random
from progressionbar import progression

class Enemy:
    def __init__(self,board):
        block = board.first_block()
        self.v = None
        self.max_hp = None
        self.cur_hp = None
        self.x = block.x - 30
        self.y = block.y - 25
        self.route = board.path
        self.size = None
        self.color = None
        self.valid = False
        self.cur = 0


    def draw(self):
        turtle.penup()
        if not -300 < self.x < 310:
            return
        turtle.goto((self.x,self.y))
        turtle.color(self.color)
        turtle.pendown()
        turtle.dot(self.size)
        turtle.color("black")
        turtle.penup()
        progression((self.x-self.size/2,self.y + self.size),self.size,self.max_hp,self.cur_hp,"red")
        #turtle.update()

    def move(self):
        if self.cur == len(self.route):
            if self.x < 350:
                self.x += self.v
            return
        if self.x > -300:
            self.valid = True
        block, direction = self.route[self.cur]
        x = block.x + 30
        y = block.y - 25
        if (self.x - x) ** 2 + (self.y - y) ** 2 < 50:
            self.cur += 1
        else:
            if direction == "right":
                self.x += self.v
            elif direction == "up":
                self.y += self.v
            elif direction == "down":
                self.y -= self.v


class Trash(Enemy):
    def __init__(self,speed,level,board):
        Enemy.__init__(self,board)
        self.color = "green"
        self.size = 20
        self.v = speed
        self.level = level
        self.cur_hp = self.max_hp = self.hpset(level)
        self.money = 2

    def hpset(self,level):
        """
        :param level:
        :return: max_hp
        """
        hp = level * 20 - 5
        if hp < 20:
            hp = 20
        return hp

class Boss(Enemy):
    def __init__(self,level,board):
        Enemy.__init__(self,board)
        self.color = "pink"
        self.size = 30
        self.v = 2
        self.level = level
        self.cur_hp = self.max_hp = self.hpset(level)
        self.money = 20

    def hpset(self,level):
        hp = level * 100
        return hp

class Enemies:
    def __init__(self,level,board):
        r = random.randrange(0,3)
        speed = random.randrange(3,7)
        self.t = 0
        if r >= 1:
            self.lst = [Trash(speed,level,board) for i in range(random.randrange(10,20))]
        else:
            self.lst = [Boss(level,board) for i in range(random.randrange(1,5))]
        self.queue = []

    def physics(self):
        try:
            if self.t % 40 == 0:
                self.queue.insert(0,self.lst.pop())
        except:
            pass
        self.t += 1
        for enemy in self.queue:
            if enemy:
                enemy.move()

    def draw(self):
        for enemy in self.queue:
            if enemy:
                enemy.draw()
            #turtle.update()

    def remove(self,enemy):
        try:
            self.queue.remove(enemy)
            return True
        except:
            return False

    def is_empty(self):
        return len(self.queue) == 0




