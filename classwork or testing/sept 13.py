print('3 Question Quiz, 2 tries\n\tEnter your answer as a number')
for i in range(2):
  count=0
  if input('Apple is:\n1. Red\n2. Blue\n3. Green\n')=='1':
    count+=1
    print('Correct')
  else:
    print('Incorrect')
  if input('Sky is:\n1. Orange\n2. Blue\n3. Purple\n')=='2':
    count+=1
    print('Correct')
  else:
    print('Incorrect')
  if input('Banana is:\n1. Yellow\n2. Blue\n3. Red\n')=='1':
    count+=1
    print('Correct')
  else:
    print('Incorrect')
  if i%2==0:
    quiz1=count
  else:
    quiz2=count
if quiz1>=quiz2:
  print('\nScore: '+str(quiz1)+'/3')
if quiz1<quiz2:
  print('\nScore: '+str(quiz2)+'/3')