from turtle import *
import time

title('Narwhal Game')
s = getscreen()
s.screensize(250,250)
t1player1, t1player2, t1player3, t2player1, t2player2, t2player3=Turtle(),Turtle(),Turtle(),Turtle(),Turtle(),Turtle()
t1, t2 = [t1player1, t1player2, t1player3], [t2player1, t2player2, t2player3]
#border
border=Turtle()
border.penup()
border.setpos(-250,250)
border.pendown()
border.width(5)
for i in range(4):
  border.forward(500)
  border.right(90)
#player setups
for i in t1:
  i.color('red','red')
  i.shape('square')
for i in t2:
  i.color('blue','blue')
  i.shape('square')
#positions
for i in t1+t2:
  i.penup()
t1player1.setpos(-100,-200)
t1player2.setpos(0,-200)
t1player3.setpos(100,-200)
t2player1.setpos(100,200)
t2player2.setpos(0,200)
t2player3.setpos(-100,200)


time.sleep(5)
done()