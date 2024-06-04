from random import *
u=int(input('You will guess a number\nbetween 0 and your number\n\nNumber: '))
r,x=randint(0,u),0
while True:
  c=int(input('Guess: '))
  x+=1
  if c<r:
    print('Higher')
  elif c>r:
    print('Lower')
  else:
    print('You got it!\n')
    break
print('Attempts: '+str(x))