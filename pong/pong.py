# CS-UY 1114
# Final project

import turtle
import time
import random
import math

# This variable represents the x position
# of the player's paddle. Initially, it
# will be 0 (i.e. in the center). The y
# position of the paddles never changes,
# so we don't need a variable for it.
user1x = 0

# This variable represents the x position
# of the computer's paddle. Initially, it
# will be 0 (i.e. in the center)
user2x = 0

# These variables store the current x and y
# position of the ball. Their values will be
# updates on each frame, as the ball moves.
ballx = 0
bally = 0

# These variables store the current x and y
# velocity of the ball. Their values will be
# updates on each frame, as the ball moves.
ballvx = 0
ballvy = 0

# These variables store the current score 
# of the game.
user1points = 0
user2points = 0

def draw_frame():
    """
    signature: () -> NoneType
    Given the current state of the game in
    the global variables, draw all visual
    elements on the screen: the paddles,
    the ball, and the current score.
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
    turtle.pensize(3)
    turtle.penup()
    turtle.goto(user1x,-250)
    turtle.pendown()
    turtle.fd(80) #板长
    turtle.penup()
    turtle.goto(user2x,250)
    turtle.pendown()
    turtle.fd(80) #板长
    turtle.penup()
    turtle.goto(-350,-300)
    turtle.pendown()
    turtle.write("Score: " + str(user1points) , font=("Arial", 20, "normal"))
    turtle.penup()
    turtle.goto(-350,300)
    turtle.write("Score: " + str(user2points) , font=("Arial", 20, "normal"))
    turtle.penup()
    turtle.goto(ballx,bally)
    turtle.pendown()
    turtle.dot(20) #小球直径

def key_left():
    """
    signature: () -> NoneType
    This function is called by turtle whenever
    the user press the left arrow. It should
    adjust the position of the user's paddle
    appropriately by modifying the variable
    user1x. It should not draw anything on the
    screen.
    """
    global user1x
    if user1x > -350: #向左最大距离
        user1x -= 20

def key_right():
    """
    signature: () -> NoneType
    This function is called by turtle whenever
    the user press the left arrow. It should
    adjust the position of the user's paddle
    appropriately by modifying the variable
    user1x. It should not draw anything on the
    screen.
    """
    global user1x
    if user1x < 280:
        user1x += 20

def reset():
    """
    signature: () -> NoneType
    Reset the global variables representing
    the position and velocity of the ball and
    the position of the paddles to their initial
    state, effectively restarting the game. The
    initial velocity of the ball should be random
    (but there there must be nonzero vertical
    velocity), but the speed of the ball should
    be the same in every game.
    """
    global user1x, user2x
    global ballvx, ballvy
    global ballx, bally
    user1x = 0
    user2x = 0
    ls = [-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,
          5,6,7,8,9,10,11,12,13,14,15]
    ballvx = random.choice(ls)
    ballvy = random.choice(ls)
    ballx = 0
    bally = 0

def ai():
    """
    signature: () -> NoneType
    Perform the 'artificial intelligence' of
    the game, by moving the computer's paddle
    to an appropriate location by updating
    the user2x variable. The computer
    paddle should move towards the ball in an
    attempt to get under it. THis function
    should not draw anything on the screen.
    """
    global user2x
    if ballvy > 0:
        if ballx >= user2x + 80:
            user2x += 10
        if ballx <= user2x:
            user2x -= 10

def physics():
    """
    signature: () -> NoneType
    This function handles the physics of the game
    by updating the position and velocity of the
    ball depending on its current location. This
    function should detect if the ball has collided
    with a paddle or a wall, and if so, adjust the
    direction of the ball (as stored in the ballvx
    and ballvy variables) appropriately. If the ball
    has not collided with anything, the position of the
    ball should be updated according to its current
    velocity.
    This function should also detect if one of
    the two players has missed the ball. If so, it
    should award a point to the other player, and
    then call the reset() function to start a new
    round.
    This function should not draw anything on the
    screen.
    """
    global ballx, bally
    global ballvx, ballvy
    global user1points, user2points
    if ballx > 340 or ballx < -350: #触墙
        ballvx = -ballvx
    if bally >= 230: # rivals
        if user2x <= ballx <= user2x + 80:
            d = -(ballx - user2x - 40)
            angle = 1.5 * d + 90
            if angle == 90:
                ballvx = 0
            else:
                rad = angle * math.pi / 180
                ballvx = ballvy/math.tan(rad)
            ballvy = -ballvy
        else:
            user1points += 1
            reset()
    elif bally <= -230: # player
        if user1x <= ballx <= user1x + 80:
            d = ballx - user1x - 40
            angle = 1.5 * d + 90
            if angle == 90:
                ballvx = 0
            else:
                rad = angle * math.pi / 180
                ballvx = ballvy/math.tan(rad)
            ballvy = -ballvy
        else:
            user2points += 1
            reset()
    ballx += ballvx
    bally += ballvy

def is_game_over():
    """
    signature: () -> bool
    Returns true when the game is over, according
    to the rules specified in the assignment.
    """
    return user2points == 5

        
def read_high_scores():
    """
    signature: () -> list(tuple(int, str))
    Reads the current contents of the high score
    file. It returns a list of tuples, where
    each tuple contains a score and a player's
    name. The scores should be returned in
    decreasing order, with the best score
    first. If the high score file does not
    exist, the function should return an
    empty list.
    """
    f = open("high_score_files",'r')
    ls = []
    for line in f:
        line = line.strip()
        ls.append(eval(line))
    ls.sort(key=lambda x:x[0], reverse = True)
    f.close()
    print(ls)
    return ls
    
    

def update_high_scores():
    """
    signature: () -> bool
    Determine if the player's score deserves a
    position on the high score table. If so,
    prompt the user for their name and update
    the table.
    This function should call read_high_scores
    to get the current high score values.
    """
    ls = read_high_scores()
    point = ls[0][0]
    for i in ls:
        if i[0] < point:
            point = i[0]
    if len(ls) < 5 or user1points > point:
        f = open("high_score_files","w")
        name = turtle.textinput("Highscore Table","Enter Your Name:")
        ls.append((user1points,name))
        for line in ls[0:5]:
            f.write(str(line)+"\n")
        f.close()
        return True
    return False
        

def display_high_scores():
    """
    signature: () -> bool
    Get the current content of the high score
    table from a file and display it in the
    turtle window.
    This function should call read_high_scores
    to get the current high score values.
    """
    ls = read_high_scores()
    turtle.penup()
    for i in range(len(ls)):
        turtle.goto(200,200-i*10)
        turtle.write(ls[i][1]+"->"+str(ls[i][0]))
    return True
    
    

def main():
    """
    signature: () -> NoneType
    Run the pong game. You shouldn't need to
    modify this function.
    """
    turtle.tracer(0,0)
    turtle.hideturtle()
    turtle.onkey(key_left, "Left")
    turtle.onkey(key_right, "Right")
    turtle.listen()
    reset()
    while not is_game_over():
        physics()
        ai()
        turtle.clear()
        draw_frame()
        turtle.update()
        time.sleep(0.05)
    update_high_scores()
    turtle.clear()
    display_high_scores()

main()
