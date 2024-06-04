print('You need to try a subtraction problem!')
num=int(input('Take in a number: '))
print('Now try to guess what number is 50 less than that!')
num2=int(input('Enter guess: '))
if num2>(num-50):
  print('You guessed too high!')
elif num2<(num-50):
  print('You guessed too low!')
elif num2==(num-50):
  print('You got it!')