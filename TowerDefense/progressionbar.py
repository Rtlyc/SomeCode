import turtle
def progression(pos,length,max_hp,cur_hp,color):
    turtle.penup()
    turtle.goto(pos)
    turtle.pendown()
    if cur_hp < 0:
        cur_hp = 0
    for i in range(2):
        turtle.fd(length)
        turtle.rt(90)
        turtle.fd(10)
        turtle.rt(90)
    turtle.penup()
    new = cur_hp/max_hp * length
    turtle.goto(pos)
    turtle.begin_fill()
    turtle.color(color)
    for i in range(2):
        turtle.fd(new)
        turtle.rt(90)
        turtle.fd(10)
        turtle.rt(90)
    turtle.end_fill()
    turtle.color("black")
    #turtle.update()