if input('Enter your name:\n').upper() == 'JOE':
  print('That\'s my name\n')
else:
  print('You have a different name than mine\n')
if int(input('Enter a number:\n')) <= 50:
  print('That number is lower or equal to 50\n')
else:
  print('That number is bigger than 50\n')
if input('Say hello:\n').upper() == 'HELLO':
  print('Your input was successful\n')
else:
  print('Your input failed\n')
Correct=0
if input('\nQuiz:\nWho was the first President of the United States?\nA. Abraham Lincoln\nB. George Washington\nC. Benjamin Franklin\n').upper() == 'B':
  Correct+=1
if input('\nWhat color represents luck?\nA. Blue\nB. Yellow\nC. Green\n').upper() == 'C':
  Correct+=1
if input('\nWhat color shirt was I wearing when I wrote this?\nA. Blue\nB. Yellow\nC. Green\n').upper() == 'A':
  Correct+=1
print('You got '+str(Correct)+'/3 correct!\n')
if int(input('Enter a number:\n'))%2 == 1:
  print('Your number is odd\n')
else:
  print('Your number is even\n')