import turtle
from time import *
from random import *

def go_up():
  y = player.ycor()
  if y<280:
    player.sety(y+20)
def go_down():
  y = player.ycor()
  if y>-120:
   player.sety(y-20)
def go_left():
  x = player.xcor()
  if x>-280:
    player.setx(x-20)
def go_right():
  x = player.xcor()
  if x<280:
    player.setx(x+20)

sc = turtle.Screen()
sc.title("Game")
sc.bgcolor('white')
sc.setup(width=600, height=600)

player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("black")
player.penup()
player.goto(0,100)
player.direction = "stop"

sc.listen()
sc.onkeypress(go_up, "w")
sc.onkeypress(go_down, "s")
sc.onkeypress(go_left, "a")
sc.onkeypress(go_right, "d")
go_up()

e1 = turtle.Turtle()
e1.speed(0)
e1.shape("square")
e1.color("red")
e1.penup()
e1.direction = "stop"

e2 = turtle.Turtle()
e2.speed(0)
e2.shape("square")
e2.color("blue")
e2.penup()
e2.goto(0,400)
e2.direction = "stop"

e3 = turtle.Turtle()
e3.speed(0)
e3.shape("square")
e3.color("green")
e3.penup()
e3.goto(0,400)
e3.direction = "stop"

def spawn():
  global num
  global num2
  global num3
  num=randint(1,4)
  if num == 1:
    e1.goto(player.xcor(),player.ycor()+200)
  elif num == 2:
    e1.goto(player.xcor()+200,player.ycor())
  elif num == 3:
    e1.goto(player.xcor()-200,player.ycor())
  elif num == 4:
    e1.goto(player.xcor(),player.ycor()-200)
  e1.direction = "stop"
  if score>=10:
    num2=randint(1,4)
    if num2 == 1:
      e2.goto(player.xcor()-40,player.ycor()+200)
    elif num2 == 2:
      e2.goto(player.xcor()+200,player.ycor()+40)
    elif num2 == 3:
      e2.goto(player.xcor()-200,player.ycor()-40)
    elif num2 == 4:
      e2.goto(player.xcor()+40,player.ycor()-200)
    e2.direction = "stop"
  if score>=20:
    num3=randint(1,4)
    if num3 == 1:
      e3.goto(player.xcor()+20,player.ycor()+200)
    elif num3 == 2:
      e3.goto(player.xcor()+200,player.ycor()-20)
    elif num3 == 3:
      e3.goto(player.xcor()-200,player.ycor()+20)
    elif num3 == 4:
      e3.goto(player.xcor()-20,player.ycor()-200)
    e3.direction = "stop"

wait=.1
score=0
while True:
  score+=1
  lose=False
  sc.update()
  spawn()
  for i in range(20):
    sleep(wait)
    x1=e1.xcor()
    y1=e1.ycor()
    if num==1:
      e1.sety(y1-20)
    elif num==2:
      e1.setx(x1-20)
    elif num==3:
      e1.setx(x1+20)
    elif num==4:
      e1.sety(y1+20)
    if score>=10:
      x2=e2.xcor()
      y2=e2.ycor()
      if num2==1:
        e2.sety(y2-20)
      elif num2==2:
        e2.setx(x2-20)
      elif num2==3:
        e2.setx(x2+20)
      elif num2==4:
        e2.sety(y2+20)
      if score>=20:
        x3=e3.xcor()
        y3=e3.ycor()
        if num3==1:
          e3.sety(y3-20)
        elif num3==2:
          e3.setx(x3-20)
        elif num3==3:
          e3.setx(x3+20)
        elif num3==4:
          e3.sety(y3+20)
    if e1.xcor()==player.xcor() and e1.ycor()==player.ycor():
      lose=True
      break
    elif e2.xcor()==player.xcor() and e2.ycor()==player.ycor():
      lose=True
      break
    elif e3.xcor()==player.xcor() and e3.ycor()==player.ycor():
      lose=True
      break
  if wait>.06:
    wait-=.01
  if 45>=score>=30 and score%5==0:
    wait-=.01
  print('Score: '+str(score))
  if lose==True:
    break

print('Game Over')

sc.mainloop()

