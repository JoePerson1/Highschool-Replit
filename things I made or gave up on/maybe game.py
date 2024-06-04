from turtle import *
from math import *

screen = Screen()
screen.setup(1.0,1.0)

a = Turtle()

def up():
  global rotation
  a.right(abs(360-rotation))
  rotation = 0

def down():
  global rotation
  a.right(abs(180-rotation))
  rotation = 180

def right():
  global rotation
  a.right(abs(90-rotation))
  rotation = 90

def left():
  global rotation
  a.right(abs(270-rotation))
  rotation = 270
  
rotation = 90
a.speed(10)
a.penup()
a.shape('circle')
x=1
#up left down

while True:
  if x == 1:
    a.fd(1)
  onkeypress(up, 'w')
  onkeypress(down,'s')
  onkeypress(right,'d')
  onkeypress(left,'a')
  listen()

mainloop()