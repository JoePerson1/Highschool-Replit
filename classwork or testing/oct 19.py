from random import *
set=[]
while True:
  try:
    l=int(input('How many names do you want? '))
    break
  except:
    print('Invalid Number')
for i in range(l):
  set.append(input('Name: '))
print('\nTry to guess the correct name in the list:\n'+str(set)+'\n')
while True:
  random,guess=choice(set).lower(),input('Guess: ').lower()
  if random==guess:
    break
  elif guess not in set:
    print('That\'s not in the list. It was '+random.capitalize())
  else:
    print('Wrong. It was '+random.capitalize())
print('You picked the correct name!')