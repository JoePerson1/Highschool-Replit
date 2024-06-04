from time import *
from random import *
a,b,c,d=['a'],['b'],['c'],['d']
rows=[a,b,c,d]
spawnnum=[2,2,2,2,2,2,2,2,2,4]
spawn=choice(spawnnum)
spawnrow=choice(rows)
spawnspot=randint(1,4)

#spawnrow[spawnspot]=spawnnum

while True:
  print()
  print(a)
  print(b)
  print(c)
  print(d)
  print()
  print('\033[F'*10)
  sleep(1)
  