import turtle
class Hero:
    def __init__(self):
        self.money = 30
        self.max_hp = 10
        self.cur_hp = 10


class Electron:
    def __init__(self, board):
        block = board.first_block()
        self.x = block.x - 30
        self.y = block.y - 25
        self.v = 20
        self.route = board.path
        self.cur = 0

    def move(self):
        if self.cur == len(self.route):
            if self.x > 300:
                return
            else:
                self.x += self.v
            return
        block, direction = self.route[self.cur]
        x = block.x + 30
        y = block.y - 25
        if (self.x - x) ** 2 + (self.y - y) ** 2 < 1000:
            self.cur += 1
        else:
            if direction == "right":
                self.x += self.v
            elif direction == "up":
                self.y += self.v
            elif direction == "down":
                self.y -= self.v

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.dot(10)
        turtle.penup()

