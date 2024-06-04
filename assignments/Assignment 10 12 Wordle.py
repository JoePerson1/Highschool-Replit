import random
from colorama import Fore
with open('library.txt') as file:
  word=random.choice(file.readlines())[0:5].upper()
print(Fore.WHITE+'Wordle:')
for i in range(6):
  guess=input(Fore.RED+'\n').upper()
  while len(guess)!=5 or guess.isalpha() is False:
    guess2=input(Fore.WHITE+'\n\033[FWord must be 5 letters\nTry again.\n'+Fore.RED+'')
    print('\033[F\033[F\033[F\033[F')
    guess=guess2.upper()
  print('\n\n\x1b[2K\033[F\x1b[2K\033[F\x1b[2K\033[F\x1b[2K\033[F')
  for p in range(5):
    green=0
    for m in range(5):
      if guess[m]==word[m]==guess[p]:
        green+=1
    if word[p]==guess[p]:
      print(Fore.GREEN+guess[p],end='')
    else:
      for a in range(5):
        if word.count(guess[p])-green>=guess[:p+1].count(guess[p]):
          print(Fore.YELLOW+guess[p],end='')
          break
        elif green==word.count(guess[p]) and green!=0 or green<guess.count(guess[p]):
          print(Fore.WHITE+guess[p],end='')
          break
  if guess==word:
    print(Fore.WHITE+'\n\nYou win!')
    break
  elif i==5:
    print(Fore.WHITE+'\n\nGame over. You lost.\nThe word is '+word)