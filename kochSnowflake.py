from turtle import *
t = Turtle()
start_level = 4

def snowflake(dist, level):
    third = dist / 3.0
    if level == 0:
        t.forward(dist)
    else:
        snowflake(third, level - 1)
        t.lt(60)
        snowflake(third, level - 1)
        t.rt(120)
        snowflake(third, level - 1)
        t.lt(60)
        snowflake(third, level - 1)

t.speed(0)
t.ht()
t.pu()
t.goto(-200, 0)
t.pd()
snowflake(300, start_level)
t.rt(120)
snowflake(300, start_level)
t.rt(120)
snowflake(300, start_level)
