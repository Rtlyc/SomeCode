import random,math
import turtle




class Character:
    def __init__(self):
        self.level = 1
        self.cur_ep = 0
        self.max_ep = 10
        self.max_hp = 50
        self.cur_hp = 50
        self.money = 10
        self.attack = (10,20)
        self.x = -100
        self.y = 0

    def draw(self):
        turtle.penup()
        turtle.goto(self.x,self.y)
        turtle.color("black")
        turtle.dot(30)
        turtle.update()

    def update(self):
        while self.cur_ep >= self.max_ep:
            self.cur_ep -= self.max_ep
            self.max_ep += 10
            self.level += 1
            self.max_hp += 20
            self.cur_hp = self.max_hp
            self.attack = (self.attack[0]+5,self.attack[1]+5)

    def recover(self):
        self.cur_hp += self.max_hp//2
        if self.cur_hp > self.max_hp:
            self.cur_hp = self.max_hp

