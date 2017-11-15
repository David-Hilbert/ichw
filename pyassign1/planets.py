
'''
planets.py: The picture of the solar system

__author__ = 'Zhou Junjie'
__pkuid__  = '1700011800'
__email__  = '1700011800@pku.edu.cn'
'''

import turtle
import math


def eee(n):
    return (0.1+0.1*n)
def ppp(n):
    return float(20+10*n)

def orbit(n,Col):

    pppp=ppp(n)
    eeee=eee(n)
    t=turtle.Pen()
    t.speed(0)
    t.color(Col)
    t.pensize(3)
    t.penup()
    t.goto((pppp)/(1-eeee),0)
    t.pendown()
    u=100
    for x in range(1,2*u+1):
        t.goto(              math.cos(x*3.14159/u)*pppp/  (1.0-eeee*math.cos(x*3.14159/u))             ,pppp*math.sin(x*3.14159/u)  /  (1.0-eeee*math.cos(x*3.14159/u))                                   )
        if x==n:
            t.begin_fill()
            t.circle(4)
            t.end_fill()
    t.hideturtle()
    return

def main():
    a=turtle.Pen()
    a.penup()
    a.goto(0,-5)
    a.pendown()
    a.color('gold')
    a.begin_fill()
    a.circle(10)
    a.end_fill()
    a.hideturtle()
    COL=['brown','blue','green','red','black','orange','cyan']
    for i in range(1,7):
        orbit(i,COL[i])
    return
if __name__=='__main__':
    main()
