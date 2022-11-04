# CS-UY 1114
# Final project

import turtle
import time

# This variable store the horizontal position
# of the player's ship. It will be adjusted
# when the user press left and right keys, and
# will be used by the draw_frame() function to draw
# the ship. The ship never moves vertically, so
# we don't need a variable to store its y position.
userx = 0
usery = -210

# This variable is a list of enemies currently in
# the game. Each enemy is represented by a tuple
# containing its x,y position as well as a string
# indicated the enemy's current direction of travel
# (either left or right). 
# Your final game should include more enemies, although
# the exact arrangement is up to you.
enemies = [(300,50, "left"), (400,50, "left"), (350, -50, "right")]

# This variable is a list of all bullets currently
# in the game. It is a list of tuples of (x,y)
# coordinates, one for each bullet. An elements will
# be added when a new bullet is fired, and removed
# when a bullet is destroyed (either by leaving
# the screen or by hitting an enemy).
bullets = []
enemy_bullets = []

# This variable is checked by the game's main
# loop to determine when it should end. When
# the game ends (either when the player's ship
# is destroyed, or when all enemies have been 
# destroyed), your code should set this variable
# to True, causing the main loop to end.
gameover = False

def draw_frame():
    """
    signature: () -> NoneType
    Given the current state of the game in
    the global variables, draw all visual
    elements on the screen: the player's ship,
    the enemies, and the bullets.
    Please note that this is your only function
    where drawing should happen (i.e. the only
    function where you call functions in the
    turtle module). Other functions in this
    program merely update the state of global
    variables.
    This function also should not modify any
    global variables.
    Hint: write this function first!
    """
    turtle.penup()
    turtle.pencolor("black")
    turtle.goto(-350,-200)
    turtle.pendown()
    turtle.goto(350,-200)
    turtle.bgcolor("lightsteelblue")
    turtle.penup()
    turtle.goto(-350,300)
    turtle.pendown()
    turtle.pencolor("yellow")
    turtle.write("Score: " + str(score) , font=("Arial", 20, "normal"))
    turtle.pencolor("black")
    turtle.penup()
    turtle.goto(-350,250)
    turtle.pendown()
    turtle.write("Bullets_left: " + str(bullets_left) , font=("Arial", 20, "normal"))
    turtle.penup()
    turtle.goto(userx,usery)
    turtle.pendown()
    turtle.pensize(3)
    turtle.pencolor("deeppink")
    for i in range(3):
        turtle.fd(20)
        turtle.lt(120)
    for i in enemies:
        turtle.pencolor("brown")
        turtle.penup()
        turtle.goto(i[0]/5,i[1])
        turtle.pendown()
        turtle.dot(20)
    for i in bullets:
        turtle.penup()
        turtle.goto(i[0],i[1])
        turtle.pendown()
        turtle.pencolor("blue")
        turtle.seth(90)
        turtle.fd(10)
        turtle.seth(0)
    for i in enemy_bullets:
        turtle.penup()
        turtle.goto(i[0],i[1])
        turtle.pendown()
        turtle.pencolor("red")
        turtle.seth(-90)
        turtle.fd(20)
        turtle.seth(0)
    
def key_up():
    global usery
    if -320 <= usery < -200:
        usery += 20

def key_down():
    global usery
    if -300 <= usery <= -180:
        usery -= 20
    
def key_left():
    """
    signature: () -> NoneType
    This function is called by turtle whenever
    the user press the left arrow. It should
    adjust the position of the player's ship
    appropriately by modifying the variable
    userx.
    """
    global userx
    if userx > -330:
        userx -= 20

def key_right():
    """
    signature: () -> NoneType
    This function is called by turtle whenever
    the user press the left arrow. It should
    adjust the position of the player's ship
    appropriately by modifying the variable
    user1x.
    """
    global userx
    if userx < 330:
        userx += 20

def key_space():
    """
    signature: () -> NoneType
    This function is called by turtle whenever
    the user press the space key. It should
    add a new bullet to the list of bullets.
    """
    global bullets_left
    if bullets_left > 0:
        bullets.append((userx + 10,-180))
        bullets_left -= 1

def physics():
    """
    signature: () -> NoneType
    Update the state of the game world, as
    stored in the global variables. Here, you
    should check the positions of the bullets,
    and remove them if they go off the screen
    or collide with an enemy. In the later case
    you should also remove the enemy. That is,
    given the current position of the bullets,
    calculate their position in the next frame.
    """
    global bullets
    global enemies
    global score
    global enemy_bullets
    for enemy_bullet in enemy_bullets:
        if enemy_bullet[1] < -300:
            enemy_bullets.remove(enemy_bullet)
    for bullet in bullets:
        if bullet[1] > 300:
            bullets.remove(bullet)
        for enemy in enemies:
            if enemy[-1] == "right":
                if (bullet[0] - enemy[0]/5)**2 + (bullet[1] - enemy[1])**2 <= 200:#(下一帧问题)
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 1
            if enemy[-1] == "left":
                if (bullet[0] - enemy[0]/5 )**2 + (bullet[1] - enemy[1])**2 <= 200:#(下一帧问题)
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 1

def ai():
    """
    signature: () -> NoneType
    Perform the 'artificial intelligence' of
    the game, by updating the position of the
    enemies, storied in the enemies global
    variable. That is, given their current
    position, calculate their position
    in the next frame.
    If the enemies reach the player's ship,
    you should set the gameover variable
    to True. Also, if there are no more
    enemies left, set gameover to True.
    """
    global enemies
    global gameover
    global bullets
    global bullets_left
    global enemy_bullets
    if bullets_left <= 0:
        if bullets == []:
            gameover = True
    if enemies == []:
        gameover = True
    for enemy_bullet in enemy_bullets:
        if enemy_bullet[1] -10 >= usery:
            if (enemy_bullet[0] - userx -10)**2 + (enemy_bullet[1]-usery -10)**2 <= 400:
                gameover = True
    else:
        new_enemies = []
        turn = 0
        for enemy in enemies:
            if enemy[-1] == "left" and enemy[0] > -1500:
                new_enemies.append((enemy[0]-50,enemy[1],enemy[2])) #速度
            elif enemy[-1] == "right" and enemy[0] < 1500:
                new_enemies.append((enemy[0]+50,enemy[1],enemy[2]))
            elif enemy[-1] == "left" and enemy[0] <= -1500:
                new_enemies.append((enemy[0]+20,enemy[1]-50,"right"))
            else:
                new_enemies.append((enemy[0]-20,enemy[1]-50,"left"))
        for enemy in enemies:
            if enemy[1] <= -200: #gameover
                gameover = True
        for enemy in enemies:
            if -20 <= enemy[0] - userx <= 20:
                enemy_bullets.append((enemy[0],enemy[1]))
        enemies = new_enemies
        new_bullets = []
        for bullet in bullets:
            new_bullets.append((bullet[0],bullet[1]+30))
        new_enemy_bullets = []
        for enemy_bullet in enemy_bullets:
            new_enemy_bullets.append((enemy_bullet[0],enemy_bullet[1]-10))
        bullets = new_bullets
        enemy_bullets = new_enemy_bullets
        
        

def reset():
    """
    signature: () -> NoneType
    This function is called when your game starts.
    It should set initial value for all the
    global variables.
    """
    global enemies
    global bullets
    global userx
    global usery
    global gameover
    global score
    global bullets_left
    global enemy_bullets
    enemies = [(300,50, "left"), (400,50, "left"), (450, 0, "right"),(300, 0, "right"),(300, 0, "left"),(300,150,"right"),(200,150,"right"),(400,150,"right"),(100,150,"right"),(0,150,"right"),(0,250,"left"),(100,250,"left"),(200,250,"left"),(300,250,"left"),(400,250,"left")]
    bullets = []
    enemy_bullets = []
    userx = 0
    usery = -220
    gameover = 0
    score = 0
    bullets_left = 20

def main():
    """
    signature: () -> NoneType
    Run the game. You shouldn't need to
    modify this function.
    """
    turtle.tracer(0,0)
    turtle.hideturtle()
    turtle.onkey(key_left, "Left")
    turtle.onkey(key_right, "Right")
    turtle.onkey(key_space, "space")
    turtle.onkey(key_up, "Up")
    turtle.onkey(key_down, "Down")
    turtle.listen()
    reset()
    while not gameover:
        physics()
        ai()
        turtle.clear()
        draw_frame()
        turtle.update()
        time.sleep(0.05)

main()
