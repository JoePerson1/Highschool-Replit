from turtle import *
from time import *

screen=Screen()
screen.setup(1.0,1.0)

player=Turtle()

def up():
  player.forward(1)

def right():
  pass

def test():
  while True:
    print(1)

def down():
  player.forward(-1)

player.penup()
player.left(90)
player.shape('circle')
player.turtlesize(0.5)
player.goto(0,0)


onkeypress(up,'w')
onkeypress(down,'s')
listen()




screen.mainloop()