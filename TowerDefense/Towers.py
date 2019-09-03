import turtle,math

def rectangle(length,width):
    turtle.penup()
    turtle.fd(-length/2)
    turtle.lt(90)
    turtle.fd(width/2)
    turtle.pendown()
    turtle.seth(0)
    for i in range(2):
        turtle.fd(length)
        turtle.rt(90)
        turtle.fd(width)
        turtle.rt(90)

class Tower:
    ############## Bottle###########
    class Bottle:

        class Bottle_bullet:#编辑子弹
            def __init__(self,tower,angle):
                self.x,self.y = self.loc_to_coor(tower.loc)
                self.speed = 30
                self.color = "blue"
                self.attack = tower.attack
                self.parent = tower # the parent
                self.angle = angle # the angle

            def loc_to_coor(self, loc):
                x = loc % 10
                y = loc // 10
                x = -300 + x * 60 + 30
                y = 300 - y * 50 - 25
                return x, y

            def draw(self):
                turtle.penup()
                turtle.goto(self.x,self.y)
                turtle.color(self.color)
                turtle.pendown()
                turtle.dot(10)
                turtle.color("black")
                turtle.penup()

            def move(self):
                x = self.speed * math.cos(math.radians(self.angle))
                y = self.speed * math.sin(math.radians(self.angle))
                self.x += x
                self.y += y

        class Bottle_bullets_lst:#整合子弹为列表
            def __init__(self):
                self.lst = []

            def append(self,tower,angle):
                # bullet -> Bottle_bullet
                self.lst.append(Tower.Bottle.Bottle_bullet(tower,angle))

            def draw(self):
                for i in self.lst:
                    i.draw()

            def remove(self,bullet):
                try:
                    self.lst.remove(bullet)
                except:
                    pass

            def move(self):
                for bullet in self.lst:
                    bullet.move()


        def __init__(self, loc):#编辑瓶子
            self.loc = loc
            self.bullets = Tower.Bottle.Bottle_bullets_lst()
            self.x,self.y = self.loc_to_coor(loc)
            self.range = 100 #瓶子的设计范围
            self.t = 0
            self.speed = 8 #攻击速度
            self.attack = 10
            self.level = 1

        def level_up(self): # 升级
            # 攻速提升，攻击范围增加，攻击力增加
            if self.attack < 40:
                self.range *= 1.2
                self.speed += 2
                self.attack *= 2
                self.level += 1
                return True
            return False

        def loc_to_coor(self,loc):
            x = loc % 10
            y = loc // 10
            x = -300 + x * 60 + 30
            y = 300 - y * 50 - 25
            return x,y

        def add_bullet(self,angle):
            self.bullets.append(self,angle)


        def draw(self):
            turtle.penup()
            turtle.goto(self.x,self.y)
            turtle.color("green")
            rectangle(20,40)
            turtle.penup()

    ############ SUN #########
    class Sun:

        class Sun_bullet:#编辑⭕子弹
            def __init__(self,tower):
                self.x,self.y = self.loc_to_coor(tower.loc)
                #self.speed = 10
                self.distance = 0
                self.color = "red"
                self.attack = tower.attack
                self.parent = tower # the parent

            def loc_to_coor(self, loc):
                x = loc % 10
                y = loc // 10
                x = -300 + x * 60 + 30
                y = 300 - y * 50 - 25
                return x, y

            def draw(self):
                turtle.penup()
                turtle.goto(self.x,self.y-self.distance)
                turtle.color(self.color)
                turtle.pendown()
                turtle.circle(self.distance)
                turtle.color("black")
                turtle.penup()

            def move(self):
                self.distance += 8

        class Sun_bullets_lst:#整合子弹为列表
            def __init__(self):
                self.lst = []

            def append(self,tower):
                # bullet -> Bottle_bullet
                self.lst.append(Tower.Sun.Sun_bullet(tower))

            def draw(self):
                for i in self.lst:
                    i.draw()

            def remove(self,bullet):
                try:
                    self.lst.remove(bullet)
                except:
                    pass

            def move(self):
                for bullet in self.lst:
                    bullet.move()

        def __init__(self, loc):#编辑太阳
            self.loc = loc
            self.bullets = Tower.Sun.Sun_bullets_lst()
            self.x,self.y = self.loc_to_coor(loc)
            self.range = 80 #太阳的攻击范围
            self.t = 0
            self.speed = 3 #攻击速度
            self.attack = 10

        def level_up(self): # 升级
            # 攻速提升，攻击范围增加，攻击力增加
            if self.attack < 40:
                self.range *= 1.2
                self.speed += 1
                self.attack *= 2
                return True
            return False

        def loc_to_coor(self,loc):
            x = loc % 10
            y = loc // 10
            x = -300 + x * 60 + 30
            y = 300 - y * 50 - 25
            return x,y

        def add_bullet(self):
            self.bullets.append(self)


        def draw(self):
            turtle.penup()
            turtle.goto(self.x,self.y)
            turtle.color("purple")
            rectangle(20,40)
            turtle.penup()


    ############ PLANE ########
    class Plane:

        class Plane_bullet:#编辑子弹
            def __init__(self,tower,direction):
                self.x,self.y = self.loc_to_coor(tower.loc)
                self.speed = 40
                self.color = "skyblue"
                self.attack = tower.attack
                self.parent = tower # the parent
                self.direction = direction # the direction

            def loc_to_coor(self, loc):
                x = loc % 10
                y = loc // 10
                x = -300 + x * 60 + 30
                y = 300 - y * 50 - 25
                return x, y

            def draw(self):
                turtle.penup()
                turtle.goto(self.x,self.y)
                turtle.color(self.color)
                turtle.pendown()
                turtle.dot(30)
                turtle.color("black")
                turtle.penup()

            def move(self):
                if self.direction == "Up":
                    self.y += self.speed
                elif self.direction == "Down":
                    self.y -= self.speed
                elif self.direction == "Left":
                    self.x -= self.speed
                elif self.direction == "Right":
                    self.x += self.speed


        class Plane_bullets_lst:#整合子弹为列表
            def __init__(self):
                self.lst = []

            def append(self,tower,direction):
                # bullet -> Plane_bullet
                self.lst.append(Tower.Plane.Plane_bullet(tower,direction))

            def draw(self):
                for i in self.lst:
                    i.draw()

            def remove(self,bullet):
                try:
                    self.lst.remove(bullet)
                except:
                    pass

            def move(self):
                for bullet in self.lst:
                    bullet.move()


        def __init__(self, loc):#编辑飞机
            self.loc = loc
            self.bullets = Tower.Plane.Plane_bullets_lst()
            self.x,self.y = self.loc_to_coor(loc)
            self.range = 120 #飞机的设计范围
            self.t = 0
            self.speed = 3 #攻击速度
            self.attack = 15
            self.level = 1

        def level_up(self): # 升级
            # 攻速提升，攻击范围增加，攻击力增加
            if self.level < 3:
                self.range *= 1.5
                self.speed += 1
                self.attack *= 2
                self.level += 1
                return True
            return False

        def loc_to_coor(self,loc):
            x = loc % 10
            y = loc // 10
            x = -300 + x * 60 + 30
            y = 300 - y * 50 - 25
            return x,y

        def add_bullet(self,angle):
            self.bullets.append(self,angle)


        def draw(self):
            turtle.penup()
            turtle.goto(self.x,self.y)
            turtle.color("gold")
            rectangle(20,40)
            turtle.penup()

    ######## FireBottle ############
    class Firebottle:
        def __init__(self, loc):#编辑瓶子
            self.loc = loc
            self.x,self.y = self.loc_to_coor(loc)
            self.range = 100 #瓶子的攻击范围
            self.attack = 3
            self.level = 1
            self.target = None
            self.t = 0
            self.count = 0
            self.limit = 100

        def level_up(self): # 升级
            # 攻速提升，攻击范围增加，攻击力增加
            if self.attack < 40:
                self.range *= 1.2
                self.attack *= 2
                self.level += 1
                self.limit *= 1.5
                return True
            return False

        def loc_to_coor(self,loc):
            x = loc % 10
            y = loc // 10
            x = -300 + x * 60 + 30
            y = 300 - y * 50 - 25
            return x,y

        def fire_reset(self):
            self.target = None
            self.t = 0

        def draw(self):
            turtle.penup()
            turtle.goto(self.x,self.y)
            turtle.color("tomato")
            rectangle(20,40)
            turtle.penup()
            if self.target:
                self.bullet_draw()

        def bullet_draw(self):
            turtle.penup()
            turtle.goto(self.x,self.y)
            turtle.pendown()
            turtle.color("chocolate")
            turtle.pensize(5)
            turtle.goto(self.target.x,self.target.y)
            turtle.penup()
            turtle.color("black")
            turtle.pensize(1)



    def __init__(self):#整合所有防御塔
        self.towers = []

    def append(self,tower):
        self.towers.append(tower)

    def draw(self):
        for tower in self.towers:
            tower.draw()

    def loc_to_tower(self,val):
        for tower in self.towers:
            if tower.loc == val:
                return tower

    def __iter__(self):
        for i in self.towers:
            yield i



