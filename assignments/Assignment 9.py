while True:
  x=int(input('Guess a number 1-100: '))
  if x>34:
    print('Lower')
  elif x<34:
    print('Higher')
  else:
    break
print('Correct')
while True:
  print('\n3 Question Quiz, infinite attempts')
  count=0
  if input('Apple is:\n1. Red\n2. Blue\n3. Green\n')=='1':
    count+=1
  if input('Sky is:\n1. Orange\n2. Blue\n3. Purple\n')=='2':
    count+=1
  if input('Banana is:\n1. Yellow\n2. Blue\n3. Red\n')=='1':
    count+=1
  if count==3:
    break
print('Quiz complete')
while input('\nDo you want to do an addition problem?\n').upper()=='YES':
  num1=int(input('Pick a number: '))
  num2=int(input('Pick another number: '))
  if int(input('What\'s the sum?\n'))==num1+num2:
    print('Correct')
  else:
    print('Wrong')