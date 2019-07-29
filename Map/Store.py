import turtle
def square(pos,color,size):
    turtle.penup()
    turtle.goto(pos)
    turtle.color(color)
    turtle.pendown()
    for i in range(4):
        turtle.fd(size)
        turtle.rt(90)
    turtle.penup()


def heart(pos):
    square((pos[0]-60,pos[1]+100),"black",120)
    turtle.penup()
    turtle.goto(pos)
    def curvemove():
        for i in range(200):
            turtle.right(1)
            turtle.forward(0.5)
        # turtle.update()

    turtle.color('red', 'pink')
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(111.65 / 2)
    curvemove()
    turtle.left(120)
    curvemove()
    turtle.forward(111.65 / 2)
    turtle.end_fill()
    turtle.update()
    turtle.seth(0)
    turtle.color("black")


#heart((100, 50))


def sword(pos):
    turtle.seth(0)
    square((pos[0]-55,pos[1]+120),"black",120)
    turtle.pensize(2)
    turtle.penup()
    turtle.goto(pos)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    for i in range(4):
        turtle.fd(10)
        turtle.lt(90)
    turtle.end_fill()
    turtle.lt(90)
    turtle.fd(10)
    turtle.color("brown")
    turtle.begin_fill()
    for i in range(2):
        turtle.fd(20)
        turtle.rt(90)
        turtle.fd(10)
        turtle.rt(90)
    turtle.end_fill()
    turtle.fd(20)
    turtle.lt(90)
    turtle.color("gold")
    turtle.begin_fill()
    turtle.fd(20)
    turtle.rt(90)
    turtle.fd(20)
    turtle.rt(90)
    turtle.fd(50)
    turtle.rt(90)
    turtle.fd(20)
    turtle.rt(90)
    turtle.fd(30)
    turtle.end_fill()
    turtle.seth(90)
    turtle.penup()
    turtle.fd(20)
    turtle.color("black")
    turtle.pendown()
    turtle.fd(60)
    turtle.rt(30)
    turtle.fd(10)
    turtle.rt(120)
    turtle.fd(10)
    turtle.seth(-90)
    turtle.fd(60)
    turtle.rt(90)
    turtle.fd(10)
    turtle.color("white")
    turtle.end_fill()
    turtle.seth(0)
    turtle.update()


def leave(pos):
    turtle.penup()
    turtle.goto(pos)
    turtle.pendown()
    for i in range(2):
        turtle.fd(60)
        turtle.rt(90)
        turtle.fd(20)
        turtle.rt(90)
    turtle.write("Leave",align = "left",font=("Arial", 24, "normal"))
    turtle.penup()
    turtle.update()


