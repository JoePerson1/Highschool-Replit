from random import *
rpswin,rps,cscore,uscore=['paperrock','rockscissors','scissorspaper'],['rock','paper','scissors'],0,0
print('Rock Paper Scissors\nBest of 5\n')
while cscore!=3 and uscore!=3:
  cpick,upick=choice(rps),input('You pick: ').lower()
  if upick not in rps:
    print('Invalid input\n')
    continue
  print('Computer picked '+cpick.capitalize())
  if upick==cpick:
    print('Draw')
  elif upick+cpick in rpswin:
    print('You win!')
    uscore+=1
  elif cpick+upick in rpswin:
    print('You lost!')
    cscore+=1
  print('Computer '+str(cscore)+' - '+str(uscore)+' You\n')