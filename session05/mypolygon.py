import turtle
jack = turtle.Turtle()
one = turtle.Turtle()
two = turtle.Turtle()
three = turtle.Turtle()

# #right angle
# jack.fd(100)
# jack.lt(90)
# jack.fd(100)

# #exercise 1: square
# jack.lt(90)
# jack.fd(100)
# jack.lt(90)
# jack.fd(100)

# for i in range(4):
#     print('Hello!')

#exercise 2
# def square(t, length):
#     for i in range(4):
#         t.fd(length)
#         t.lt(90)

# square(jack, 300)

#exercise 2.3
# def polygon(t, length, n):
#     for i in range(n):
#         t.fd(length)
#         t.lt(360/n)

# polygon(jack, length=100, n=5)

import math
# exercise 2.4
# def circle(t, r):
#     c = 2*math.pi*r
#     n = int(c / 3) + 1
#     length = c / n
#     polygon(t, length, n)

# circle(jack, 100)

# def arc(t, r, angle):
#     arc_length = 2*math.pi*r*angle/360
#     n = int(arc_length / 3) + 1
#     step_length = arc_length / n
#     step_angle = angle / n
#     for i in range(n):
#         t.fd(step_length)
#         t.lt(step_angle)

def polyline(t, n, length, angle):
    """Draws n line segments with the given length and
    angle (in degrees) between them.  t is a turtle."""  
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def backarc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    backpolyline(t, n, step_length, step_angle)

def backpolyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.rt(angle)

def circle(t, r):
    arc(t, r, 360)

#exercise 3
def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        t.lt(360/n)

def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)

#3.1
def circleflower(t, n, r, angle):
    flower(t, n, r, angle)
    t.pu()
    t.sety(-0.9*r*math.cos(angle/2))
    t.pd()
    t.circle(0.9*r*math.cos(angle/2))
circleflower(jack, 6, 100, 45)

#3.2
def yinyang(t, r):
    t.pu()
    t.sety(-r)
    t.pd()
    t.circle(r)
    t.pu()
    t.sety(r)
    t.pd()
    backarc(t, r/2, 180)
    arc(t, r/2, 180)
    t.pu()
    t.sety(r/3)
    t.pd()
    t.circle(r/6)
    t.pu()
    t.sety(-2*r/3)
    t.pd()
    t.circle(r/6)
yinyang(jack,100)

#3.3
def pizza(t, r):
    t.pu()
    t.sety(-r)
    t.pd()
    t.circle(r)
    t.lt(90)
    t.fd(2*r)
    t.lt(80)
pizza(jack, 100)


turtle.mainloop()

#in command prompt type python -m turtledemo