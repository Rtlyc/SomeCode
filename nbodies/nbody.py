# CS-UY 1114
# Final project

import turtle
import time
import math

# gravitional constant (to be read from file)
G = 0

# current state of all bodies (to be read from file)
# each entry in the list is a tuple consisting of:
#   body name
#   body position (x,y)
#   body velocity (x,y)
#   body mass
# This value is updated at each step of the simulation
# by the update_positions and update_velocities functions.
# sig: list(tuple(str, float, float, float, float, float))
bodies = [("Sun", 500.0, 500.0, 0.0, 0.0, 100000000.0), 
          ("Splat", 255.0, 255.0, 2.0, 0.0, 1.0)]

def readfile(filename):
    """
    signature: str -> tuple(float, list(tuple(str, float, float, float, float, float)))
    This function is called only once, when your
    program first starts. It should read the file
    named in its argument, which contains the correct value
    of the gravitional constant and the initial
    data about the planets. It should return a tuple
    consisting of two values: the value of the
    gravitational constant G, and a list of all
    the bodies read from the file.
    This function should not modify any global
    variables.
    """
    f = open(filename,'r')
    txt = f.read().splitlines()
    G = float(txt[0])
    List = txt[1:]
    bodies=[]
    for i in List:
        body = []
        body.append(i.split()[0])
        for j in i.split()[1:]:
            body.append(float(j))
        bodies.append(tuple(body))
    return G,bodies
    
    

def draw_frame():
    """
    signature: () -> NoneType
    Given the current state of the game in
    the global variables, draw all visual
    elements on the screen: the planets
    and their labels, and their current positions.
    Please note that this is your only function
    where drawing should happen (i.e. the only
    function where you call functions in the
    turtle module). Other functions in this
    program merely update the state of global
    variables.
    This function also should not modify any
    global variables.
    """
    for i in bodies:
        size = math.pow(i[-1],0.1)
        turtle.penup()
        turtle.goto(i[1]/5,i[2]/5)
        turtle.pendown()
        turtle.circle(size)
        #turtle.write(i[0])
        

def update_velocities():
    """
    signature: () -> NoneType
    This function updates the global bodies variable
    with the updated velocities of the bodies, as
    described above.
    That is, given the current velocities and
    positions of each body, calculate their velocity
    at the next frame.
    """
    global bodies
    new_bodies =[]
    for move in bodies:
        Fx_total = 0
        Fy_total = 0
        for control in bodies:
            if move != control:
                delta_x = (move[1]-control[1])
                delta_y = (move[2]-control[2])
                d = math.sqrt((move[1]-control[1])**2 + (move[2]-control[2])**2)
                Fx = -G*move[-1]*control[-1]*delta_x/(d**3)
                Fy = -G*move[-1]*control[-1]*delta_y/(d**3)
                Fx_total += Fx
                Fy_total += Fy
        ax = Fx_total/move[-1]
        ay = Fy_total/move[-1]
        vx = move[3] + ax
        vy = move[4] + ay
        new_bodies.append((move[0],move[1],move[2],vx,vy,move[-1]))
    bodies = new_bodies

def update_positions():
    """
    signature: () -> NoneType
    This function updates the global bodies variable
    with the updated positions of the bodies, as
    described above.
    That is, given the current velocities and
    positions of each body, calculate their position
    at the next frame.
    """
    global bodies
    new_bodies = []
    for i in bodies:
        new_x = i[1] + i[3]
        new_y = i[2] + i[4]
        new_bodies.append((i[0],new_x,new_y,i[3],i[4],i[-1]))
    bodies = new_bodies
    

def main():
    """
    signature: () -> NoneType
    Run the simulation. You shouldn't
    need to modify this function.
    """
    global G, bodies
    turtle.tracer(0,0)
    turtle.hideturtle()
    (G, bodies) = readfile("bodies.txt")

    while True:
        update_velocities()
        update_positions()
        turtle.clear()
        draw_frame()
        turtle.update()
        time.sleep(0.05)

main()

    

