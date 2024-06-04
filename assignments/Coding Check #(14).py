from random import *
dice, score = [1,2,3,4,5,6], 0
print('3 Rolls, Get the highest score:')
for i in range(3):
  pause = input('\nPress enter to roll:')
  roll = choice(dice)
  score += num
  print('You rolled a ' + str(num) + '\nScore: ' + str(score))
print('\nFinal score: ' + str(score))