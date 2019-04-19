import turtle as t
import random

"""
make a list of str(number) from 0-81
the strategy to express is to make a list str of number, after valid clicking, the str number + 0 or X
use is.digit() to determine
"""
number = []
for i in range(81):
    number.append(str(i))

winner = ""

"""
type: int 
func: 'record' limits next move on one small board
the original value is -1, the range is 0-8
if there is no space for next move, 'record' = -1, which means next move is unlimited 
"""
record = -1

"""
type:int
func:track the last move in order to draw it on the board
the range is 0-80
"""
track = -1

big_board = ["_","_","_",
             "_","_","_",
             "_","_","_"]
number2 = [[0,1,2,9,10,11,18,19,20],[3,4,5,12,13,14,21,22,23],[6,7,8,15,16,17,24,25,26],
           [27,28,29,36,37,38,45,46,47],[30,31,32,39,40,41,48,49,50],[33,34,35,42,43,44,51,52,53],
           [54,55,56,63,64,65,72,73,74],[57,58,59,66,67,68,75,76,77],[60,61,62,69,70,71,78,79,80]]

player = t.textinput("Choose a mode", "How many players?(press 1 or 2)")
player1 = True

def draw_board(number):
    global track
    t.clear()
    for i in range(10):# draw the board
        t.pensize(1)
        t.pencolor("brown")
        if i % 3 == 0:
            t.pensize(2)
            t.pencolor("black")
        t.penup()
        t.goto(-270 + i*60,270)
        t.seth(-90)
        t.pendown()
        t.fd(540)
        t.penup()
        t.goto(-270,270 - i * 60)
        t.seth(0)
        t.pendown()
        t.fd(540)
    if track != -1: #track the last move, fill one small square
        t.penup()
        x = track % 9
        y = track // 9
        t.goto(-270 + x*60,270- y*60)
        t.pendown()
        t.begin_fill()
        for i in range(4):
            t.fd(60)
            t.rt(90)
        t.color("bisque")
        t.end_fill()
        
    for i in range(len(number)): #draw "O" and "X"
        x = i % 9
        y = i // 9
        if "O" in number[i]:
            t.pencolor("blue")
            t.penup()
            t.goto(-240 + x*60, 210 - y*60)
            t.pendown()
            t.circle(30)
        elif "X" in number[i]:
            t.pencolor("red")
            t.penup()
            t.goto(-270 + x*60, 270 - y*60)
            t.pendown()
            t.goto(-210 + x*60, 210 - y*60)
            t.penup()
            t.goto(-270 + x*60, 210 - y*60)
            t.pendown()
            t.goto(-210 + x*60, 270 - y*60)

    t.penup()
    t.goto(300,270)
    t.pendown()
    t.pencolor("black")
    t.write(track,font=("Arial", 20, "normal"))
    t.update()
    

def do_user_move1(number, x, y):
    global record
    print("user clicked at "+str(x)+","+str(y))
    if x > 270 or x < -270 or y > 270 or y < -270: #out of range
        return False
    x_co = (int(x) + 270) // 60 #x coordinate
    y_co = (int(-y) + 270) // 60 #y coordinate
    num = x_co + y_co * 9 # identify number by location
    count = 0
    for i in number2[record]:
        if number[i].isdigit():
            count += 1
    if count == 0:
        record = -1
        
    if record != -1:
        if not num in number2[record]:
            return False
    if not number[num].isdigit():
        return False
    for i in range(len(number2)):
        for j in range(len(number2[0])):
            if num == number2[i][j]:
                record = j
    number[num] = number[num] + "O"
    return True

def do_user_move2(number, x, y):
    global player1
    global record
    print("user clicked at "+str(x)+","+str(y))
    if x > 270 or x < -270 or y > 270 or y < -270:
        return False
    x_co = (int(x) + 270) // 60
    y_co = (int(-y) + 270) // 60
    num = x_co + y_co * 9
    count = 0
    for i in number2[record]: # if there is space on small board, count+=1
        if number[i].isdigit():
            count += 1
    if count == 0:# meaning no space on small board
        record = -1
        
    if record != -1:# if next move is limited
        if not num in number2[record]:
            return False
    if not number[num].isdigit(): #click on the previous move
        return False
    for i in range(len(number2)): # change record after valid click
        for j in range(len(number2[0])):
            if num == number2[i][j]:
                record = j
    if player1:
        number[num] = number[num] + "O"
        player1 = not player1
    else:
        number[num] = number[num] + "X"
        player1 = not player1
    return True

def check_game_over(number):
    global winner
    global big_board
    """
    In this function, I first determine the state on the small board, and then determine the big board
    there are three possibilities to win on the board: horizontal, oblique, vertical
    """
    #horizontal
    decide = [(0,2),
               (3,5),
               (6,8)]
    for i in range(len(number)):
        if not number[i].isdigit():
            if i % 3 == 1:
                if number[i-1][-1] == number[i][-1] == number[i+1][-1]:
                    mod = int(number[i][:-1]) % 9
                    quo = int(number[i][:-1]) // 9 # quotient
                    if mod == 1:
                        for j in range(3):
                            if decide[j][0] <= quo <= decide[j][1]:
                                if big_board[j*3] == "_":
                                    big_board[j*3] = number[i][-1]
                                    print(big_board)
                    elif mod == 4:
                        for j in range(3):
                            if decide[j][0] <= quo <= decide[j][1]:
                                if big_board[j*3+1] == "_":
                                    big_board[j*3+1] = number[i][-1]
                                    print(big_board)
                    elif mod == 7:
                        for j in range(3):
                            if decide[j][0] <= quo <= decide[j][1]:
                                if big_board[j*3+2] == "_":
                                    big_board[j*3+2] = number[i][-1]
                                    print(big_board)
    #oblique
    center = [10,13,16,37,40,43,64,67,70]
    for i in range(len(center)):
        if not number[center[i]].isdigit():
            if number[center[i]][-1] == number[center[i]-10][-1] == number[center[i]+10][-1]:
                if big_board[i] == "_":
                    big_board[i] = number[center[i]][-1]
                    print(big_board)
            elif number[center[i]][-1] == number[center[i]-8][-1] == number[center[i]+8][-1]:
                if big_board[i] == "_":
                    big_board[i] = number[center[i]][-1]
                    print(big_board)
    #vertical
    vertical = [9,10,11,12,13,14,15,16,17,
                 36,37,38,39,40,41,42,43,44,
                 63,64,65,66,67,68,69,70,71]
    for i in range(len(vertical)):
        if not number[vertical[i]].isdigit():
            if number[vertical[i]][-1] == number[vertical[i]-9][-1] == number[vertical[i]+9][-1]:
                xco = i // 9
                yco = i % 9
                for j in range(3):
                    if decide[j][0] <= yco <= decide[j][1]:
                        loc = xco * 3 + j
                        if big_board[loc] == "_":
                            big_board[loc] = number[vertical[i]][-1]
                            print(big_board)
    #big board determine
    memory = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    if "_" in big_board:
        for item in memory:
            if big_board[item[0]] == big_board[item[1]] == big_board[item[2]] != "_":
                winner = big_board[item[0]]
                return True
    else:
        return True
    return False
                


def do_computer_move(number):
    global record
    global track
    """
    The strategy of AI:
    1.determine if there is spare space
    2.if spare space -> determine if there is a chance to win or prevent user winning on small board
        -> if not, random on small board
    3.if no spare space -> check if there is a chance to win or prevent user winning on another small board
        -> if not, random all the board
    """
    # memory means all possibilities to make a win
    memory = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    lst = []
    limit = number2[record]
    for item in memory:
        count = 0
        for no in item:  # no -> NO.
            if number[limit[no]][-1] == "X":
                count += 1
            elif number[limit[no]][-1] == "O":
                count -= 1
        if count == 2:
            lst.insert(0,item)
        elif count == -2:
            lst.append(item)
    if lst != []: # already have two on small board, one more step left
        for no in lst[0]:
            if number[limit[no]].isdigit():
                number[limit[no]] += "X"
                record = no
                track = limit[no]
                print("make three on the board")
                break
    else: #小棋板上没有二缺一 no chance to make threes 
        left = []
        for item in range(len(limit)):#小棋板数空位 count how many spare squares on small board
            if number[limit[item]].isdigit():
                left.append((limit[item],item))
        if left == []:#小棋板上已满 寻找二缺一空位 no spare squares on small board, find opportunity to make three on another small board
            lst_2 = []
            for record_2 in range(len(number2)):#go through 0-8, record_2 = 0,1,2..8
                limit_2 = number2[record_2] # small board, limit_2 = [0，1，3，9..
                for item in memory: #item->list of int, memory->list of list of int
                    count = 0
                    for no in item:# no -> int
                        if number[limit_2[no]][-1] == "X":
                            count += 1
                        elif number[limit_2[no]][-1] == "O":
                            count -= 1
                    if count == 2:
                        lst_2.insert(0,item)
                    elif count == -2:
                        lst_2.append(item)       
                if lst_2 != []: #其他战局有二缺一情况 there is possibility to make three on another small board
                    for no in lst_2[0]: #lst_2[0] = [0,1,2]
                        if number[limit_2[no]].isdigit():
                            number[limit_2[no]] += "X"
                            record = no
                            track = limit_2[no]
                            print("make 3 on another board")
                            break
                    else:
                        continue
                    break
                else: #No opportunity to make threes, just random
                    lst_3 = []
                    for i in range(len(number)):
                        if number[i].isdigit():
                            lst_3.append(number[i])
                    t = random.choice(lst_3)
                    for i in number2:
                        if t in i:
                            record = i.index(t)
                    number[int(t)] += "X"
                    track = int(t)
                    print("random all the board")
                    break
        else:# random on small board
            t = random.choice(left)
            number[t[0]] += "X"
            record = t[1]
            track = t[0]
            print("random on small board")
        
def clickhandler(x, y):
    global player
    if player == "1":
        if do_user_move1(number,x,y):
            draw_board(number)
            if not check_game_over(number):
                do_computer_move(number)
                draw_board(number)
                check_game_over(number)
            if check_game_over(number):
                t.textinput("Good Game!","The winner is "+winner)
    elif player == "2":
        if do_user_move2(number,x,y):
            draw_board(number)
            if not check_game_over(number):
                draw_board(number)
                check_game_over(number)
            if check_game_over(number):
                t.textinput("Good Game!",None)

def main():
    t.tracer(0,0)
    t.hideturtle()
    draw_board(number)
    t.onscreenclick(clickhandler)
    t.mainloop()
main()














