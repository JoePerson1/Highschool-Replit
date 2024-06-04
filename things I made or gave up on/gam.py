import random
chance=[0,1,2,3,4,5,6,7,8,9]
m=10000
print('Money: $10000')
while m < 100000:
  i=int(input('Amount:\n'))
  if random.choice(chance) <= 5:
    m-=i
  else:
    m+=i
print('Money: $'+str(m))