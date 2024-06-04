from turtle import *
from time import *

def square():
  a = Turtle()
  a.speed(100)
  a.width(3)
  count=-1
  for j in range(5000):
    if j%6 == 0:
      count=-1
    count += 1
    rb = ['red','orange','yellow','green','blue','purple']
    a.color('black')
    for i in range(1, 5):
      a.penup()
      if i%3==0:
        a.pendown()
        a.color(rb[count])
      a.forward(50+j)
      a.right(90)
      if i%3==0:
        a.color('black')
    a.penup()
    a.forward(5)
    a.right(25)

# Fullscreen the canvas
screen = Screen()
screen.bgcolor('black')
screen.setup(1.0, 1.0)

square()

sleep(100)

t = Turtle()
c = 0
while True:
  for color in ['red', 'green', 'blue', 'yellow']:
    c +=1
    t.color(color)
    t.forward(50)
    t.left(90)
    t.forward(5)
    t.speed(100)
    if c%3 == 0:
      t.forward(1)
    elif c%2 == 0:
      t.forward(150)
    if c%4 == 0:
      t.left(25)
      t.forward(10)

screen.mainloop()