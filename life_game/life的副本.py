import turtle as t
import time

def readfiles(filename):
    fo = open(filename,'r')
    txt = fo.read().splitlines()
    ls = []
    for i in txt:
        ls += [i.split()]
    for y in range(len(ls)):
        for x in range(len(ls[y])):
            ls[y][x] = eval(ls[y][x])
    fo.close()
    return ls
       
def drawframe():
    global lifes
    global side
    for y in range(len(lifes)):
        for x in range(len(lifes[y])):
            t.penup()
            if lifes[y][x]:
                t.begin_fill()
            t.goto(x*side,y*-side)
            t.pendown()
            for i in range(4):
                t.fd(side)
                t.rt(90)
            t.end_fill()
            
def my_click(clickx,clicky):
    global lifes
    if 0 <= clickx <= side * len(lifes) and -side * len(lifes) <= clicky <= 0:
        y = int(-clicky) // side
        x = int(clickx) // side
        lifes[y][x] = not lifes[y][x]
        
def my_space():
    global pause
    pause = not pause


def life_game():
    global lifes
    new_lifes = readfiles("model_lifes.txt").copy()
    for y in range(len(lifes)):#中心判断
        for x in range(len(lifes)):
            ls = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
            count = 0
            for i in range(len(ls)):
                try:
                    if lifes[y+ls[i][0]][x+ls[i][-1]]:
                        if y + ls[i][0] != -1 and x + ls[i][-1] != -1:
                            count+=1
                except IndexError:
                    pass
                continue
            if lifes[y][x]: # 存活状态判断
                if 2 <= count <= 3: # 生命2到3个 -》存活
                    new_lifes[y][x] = True
            else: #死亡状态判断
                if count == 3: #繁殖
                    new_lifes[y][x] = True
    lifes = new_lifes.copy()
                            
def main():
    global lifes
    global side
    global pause
    pause = False
    side = 8
    lifes = readfiles("lifes.txt")
    t.tracer(0,0)
    t.hideturtle()
    t.onscreenclick(my_click)
    t.onkey(my_space,"space")
    t.listen()
    while True:
        t.clear()
        drawframe()
        if not pause:
            life_game()
        t.update()
        time.sleep(0.01)
main()
