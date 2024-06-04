from random import *

from time import *

chance=[0,0,0]
print('If it\'s not aligned, you lost\n')
while True:
  chance.append(1)
  rythmn=[]
  for i in range(10):
    note=choice(chance)
    rythmn.append(note)
  for i in rythmn:
    sleep(4/len(chance))
    print(i,end = ' ',flush=True)
  print()
  played=''
  for i,num in enumerate(rythmn):
    sleep(4/len(chance))
    if num==1:
      played+='1 '
      start=time()
      beat=input('1 ')
      print('\033[A'+played,end='',flush=True)
      end=time()
      stopwatch=end-start
      #print(stopwatch)
      if 0<stopwatch<(4/len(chance)):
        continue
      else:
        print('Fail')
    elif num==0:
      played+='0 '
      print('0 ',end='',flush=True)
      continue
  print()