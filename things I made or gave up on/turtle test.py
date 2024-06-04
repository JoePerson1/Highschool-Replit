from turtle import *
import time

s=getscreen()
guy=Turtle()
lst=[guy]
for i in lst:
  i.penup()
while True:
  guy.setpos(0,100)
  guy.setpos(-100,0)
  guy.setpos(0,-100)
  guy.setpos(100,0)
done()