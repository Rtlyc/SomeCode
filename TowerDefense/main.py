import turtle,time,math
from Enemies import Enemies
from canvas import frame,Map
from Towers import Tower
from Hero import Hero,Electron
from progressionbar import progression


def hero_draw():
    global hero
    # wave drawing
    turtle.goto(-320, -180)
    turtle.write("Wave: " + str(level) + "/" + str(wave), align="left", font=("Arial", 20, "normal"))
    turtle.goto(-320, -220)
    turtle.write("HP: ", align="left", font=("Arial", 20, "normal"))
    progression((-280, -205), 50, hero.max_hp, hero.cur_hp, "red")
    turtle.goto(-270, -215)
    turtle.write(str(hero.cur_hp) + " / " + str(hero.max_hp), align="left", font=("Arial", 10, "normal"))
    turtle.goto(-320, -260)
    turtle.write("Money: " + str(hero.money), align="left", font=("Arial", 20, "normal"))
    #turtle.update()

def quick_draw():
    global hero
    turtle.goto(-320,-180)
    turtle.color("black")
    turtle.write(str(level)+ "/" + str(wave),font = 20)
    turtle.penup()
    turtle.goto(-320,-260)
    turtle.color("orange")
    turtle.pendown()
    turtle.write(str(hero.money),font = 20)
    turtle.color("red")
    turtle.penup()
    turtle.goto(-320,-220)
    turtle.pendown()
    turtle.write(str(hero.cur_hp),font = 20)
    turtle.color("black")

def all_bullets_draw():#所有的子弹都画出来
    for tower in towers:
        if isinstance(tower, Tower.Firebottle):
            continue
        bullets_lst = tower.bullets
        bullets_lst.draw()
        #turtle.update()

def physics():
    global towers,enemies,hero
    '''
    if the bullet is far from the parents, it disappear *
    if the bullet and the enemy is close enough, the enemy is eliminated by the bullet
    the bullet and the enemy disappear
    :return:
    '''
    for enemy in enemies.queue:
        if enemy.x > 300:
            hero.cur_hp -= 1
            enemies.remove(enemy)
    for tower in towers:
        if isinstance(tower,Tower.Firebottle):
            if not tower.target:
                continue
            else:
                if tower.target.cur_hp <= 0:
                    if enemies.remove(tower.target):
                        hero.money += tower.target.money
                    tower.fire_reset()
                elif (tower.target.x - tower.x) ** 2 + (tower.target.y - tower.y) ** 2 > tower.range ** 2:
                    tower.fire_reset()
                else:
                    tower.t += 1
                    if tower.t > tower.limit:
                        tower.t = tower.limit
                    damage = (tower.t * 0.1 + tower.attack) * 0.2
                    tower.target.cur_hp -= damage


        else:
            bullets_lst = tower.bullets
            bullets_lst.move()#一个塔的所有子弹移动
            distance = tower.range
            if isinstance(tower, Tower.Bottle):
                for one_bullet in bullets_lst.lst:
                    if (one_bullet.x - tower.x) ** 2 + (one_bullet.y - tower.y) ** 2 > distance **2:
                        bullets_lst.remove(one_bullet)
                        continue # remove the outside bullets
                    for one_enemy in enemies.queue:
                        if not one_enemy.valid:
                            continue
                        elif (one_bullet.x - one_enemy.x) ** 2 + (one_bullet.y - one_enemy.y)**2 <= one_enemy.size**2:
                            bullets_lst.remove(one_bullet)
                            one_enemy.cur_hp -= one_bullet.attack
                            if one_enemy.cur_hp <= 0:
                                enemies.remove(one_enemy)
                                hero.money += one_enemy.money
            elif isinstance(tower,Tower.Sun):
                for one_bullet in bullets_lst.lst:
                    if one_bullet.distance > distance:
                        bullets_lst.remove(one_bullet)
                        continue # remove the outside bullets
                    for one_enemy in enemies.queue:
                        if not one_enemy.valid:
                            continue
                        elif -10 < (math.sqrt((one_enemy.x - tower.x) ** 2 + (one_enemy.y - tower.y) ** 2) - one_bullet.distance) < 0:
                            one_enemy.cur_hp -= one_bullet.attack
                            if one_enemy.cur_hp <= 0:
                                enemies.remove(one_enemy)
                                hero.money += one_enemy.money
            elif isinstance(tower,Tower.Plane):
                for one_bullet in bullets_lst.lst:
                    bullet_distance = (one_bullet.x - tower.x) ** 2 + (one_bullet.y - tower.y) ** 2
                    if bullet_distance > distance ** 2:
                        bullets_lst.remove(one_bullet)
                        continue
                    for one_enemy in enemies.queue:
                        if not one_enemy.valid:
                            continue
                        elif (one_bullet.x - one_enemy.x) ** 2 + (one_bullet.y - one_enemy.y) ** 2 <= one_enemy.size**2:
                            one_enemy.cur_hp -= one_bullet.attack
                            if one_enemy.cur_hp <= 0:
                                enemies.remove(one_enemy)
                                hero.money += one_enemy.money




def ai():
    global towers,enemies
    '''
    if time is over something
    iterate all the towers to see if the distance from rightmost enemy is legal
    if it is legal, add bullets
    :return:
    '''
    for tower in towers:
        if isinstance(tower,Tower.Firebottle):
            if tower.target:
                continue
            else:
                for one_enemy in enemies.queue:
                    if (one_enemy.x - tower.x) ** 2 + (one_enemy.y - tower.y) ** 2 <= tower.range**2:
                        tower.target = one_enemy
        else:
            tower.t += tower.speed
            if tower.t >= 100:
                for one_enemy in enemies.queue:
                    if (one_enemy.x - tower.x) ** 2 + (one_enemy.y - tower.y) ** 2 <= tower.range**2:
                        if isinstance(tower, Tower.Bottle):
                            try:
                                rad = math.atan((tower.y - one_enemy.y) / (tower.x - one_enemy.x))
                                angle = math.degrees(rad)
                                if tower.y > one_enemy.y:#塔在上面
                                    if tower.x > one_enemy.x:#塔在右边
                                        angle = angle - 180
                                    # else:#塔在左边
                                    #     pass
                                else:#塔在下面
                                    if tower.x > one_enemy.x:#塔在右边
                                        angle = 180 + angle
                                    #else:#塔在左边
                                tower.add_bullet(angle)
                                tower.t = 0
                                break
                            except:
                                continue
                        elif isinstance(tower, Tower.Sun): # Sun自动加子弹
                            tower.add_bullet()
                            tower.t = 0
                    if isinstance(tower,Tower.Plane):# Plane 判断方位 定义direction
                        dif = 10
                        if (one_enemy.y - tower.y) ** 2 <= 100:
                            if dif < one_enemy.x - tower.x < tower.range:
                                tower.add_bullet("Right")
                                tower.t = 0
                            elif dif < tower.x - one_enemy.x < tower.range:
                                tower.add_bullet("Left")
                                tower.t = 0
                        elif (one_enemy.x - tower.x) ** 2 <= 100:
                            if dif < one_enemy.y - tower.y < tower.range:
                                tower.add_bullet("Up")
                                tower.t = 0
                            elif dif < tower.y - one_enemy.y < tower.range:
                                tower.add_bullet("Down")
                                tower.t = 0



def qbutton():
    global q
    if hero.money >= 10:
        q = True

def wbutton():
    global w
    if hero.money >= 10:
        w = True

def ebutton():
    global e
    if hero.money >= 15:
        e = True

def rbutton():
    global r
    if hero.money >= 15:
        r = True

def pbutton():
    global pause
    pause = not pause

def myup():
    global levelup
    if hero.money >= 30:
        levelup = True



def myclick(clickx,clicky):
    global towers,board,q,hero,levelup,w,e,r
    if -300 < clickx < 300 and -100 < clicky < 300:
        block = board.coor_to_block(clickx,clicky)
        if not block.path:#不是怪物路线
            if not block.tower:#没有防御塔
                if q:##选中瓶子
                    towers.append(Tower.Bottle(block.loc))
                    q = False
                    hero.money -= 10
                    block.tower = True
                elif w:# 选中太阳
                    towers.append(Tower.Sun(block.loc))
                    w = False
                    hero.money -= 10
                    block.tower = True
                elif e:# 选中飞机✈️
                    towers.append(Tower.Plane(block.loc))
                    e = False
                    hero.money -= 15
                    block.tower = True
                elif r:# 选中🔥
                    towers.append(Tower.Firebottle(block.loc))
                    r = False
                    hero.money -= 15
                    block.tower = True
            else: #有防御塔
                if levelup:#如果选择升级
                    curr_tower = towers.loc_to_tower(block.loc)
                    if curr_tower.level_up():#是否升级成功
                        hero.money -= 30
                    levelup = False




def reset():
    global q,enemies,hero,wave,towers,board,pause,electron,level,gameover,t,levelup,e,w,r
    levelup = False
    t = 0
    gameover = False
    level = 1
    pause = False
    board = Map()
    board.reset()
    q = w = e = r = False
    electron = Electron(board)
    enemies = Enemies(level,board)
    wave = 20
    hero = Hero()
    towers = Tower()


def main():
    global q,enemies,hero,wave,towers,pause,electron,level,board,gameover,t,levelup
    turtle.tracer(0,0)
    turtle.hideturtle()
    turtle.onkey(qbutton,"q")
    turtle.onkey(pbutton,"p")
    turtle.onkey(wbutton,"w")
    turtle.onkey(ebutton,"e")
    turtle.onkey(rbutton,"r")
    turtle.onkey(myup,"Up")
    turtle.onscreenclick(myclick)
    turtle.listen()
    reset()
    while not gameover:
        if not pause:
            enemies.physics()
            physics()
            ai()
        if enemies.is_empty():
            level += 1
            enemies = Enemies(level,board)
            if level >= wave:
                gameover = True
        if hero.cur_hp == 0:
            gameover = True
        turtle.clear()
        frame()
        #electron.move()
        #electron.draw()
        all_bullets_draw()
        board.draw()
        hero_draw()
        #quick_draw()
        towers.draw()
        enemies.draw()
        turtle.update()
        time.sleep(0.05)
main()
turtle.done()


