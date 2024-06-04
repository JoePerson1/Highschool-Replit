from random import *

def deal(hand):
  dealt = choice(deck)
  deck.remove(dealt)
  hand.append(dealt)

def playmid(hand, play):
  x = mid[0]
  deck.append(x)
  mid.append(play)
  hand.remove(play)
  print()

def colorprint(set):
  if type(set) != list:
    set = [set]
  for i, card in enumerate(set):
    if 'red' in card:
      print('\u001b[31m'+card, end='')
    elif 'blue' in card:
      print('\u001b[34m'+card, end='')
    elif 'green' in card:
      print('\u001b[32m'+card, end='')
    elif 'yellow' in card:
      print('\u001b[33m'+card, end='')
    else:
      print('\u001b[35m'+card, end='')
    if i != len(set)-1:
      print('\u001b[39m'+', ', end='')
    else:
      print('\u001b[39m')

def clear():
  print(('\033[F'+'\x1b[2K')*15)
  colorprint(middle)

def move(hand, play):
  if 'draw' in play.lower():
    deal(hand)
  elif play.lower() in hand:
    for i in hand:
      if i == play.lower():
        playmid(hand, play)
  elif 'end' in play.lower():
    return True

def turns():
  turn = -1
  turndirection = 1
  while True:
    turn += turndirection
    x = turn%(bots+1)
    if botnames[x]=='You':
      while y is not True:
        y = move(hands[x],input('Move: '))
    else:
      pass
      
def midswap():
  pass

deck = []
mid = []
colors = ['red ', 'green ', 'blue ', 'yellow ']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'skip', 'reverse', '+2']
middle = None

while True:
  try:
    bots = int(input('Bot Count: '))
  except ValueError or NameError:
    print('\u001b[31m'+'Invalid Number. Try Again'+'\u001b[39m')
    continue
  if 0 < bots < 4:
    break
  else:
    print('\u001b[31m' + 'Bot Count must be 1-3' + '\u001b[39m')


for color in colors:
  for num in numbers:
    deck.append(color+num)
numbers.remove('0')

for color in colors:
  for num in numbers:
    deck.append(color+num)

for i in range(4):
  deck.append('wild')
  deck.append('wild +4')

handA, handB, handC, handD = [], [], [], []
hands = [handA, handB, handC, handD]
botnames = {0:'You', 1:'', 2:'', 3:''}
for i in range(1,bots+1):
  with open('names.txt') as file:
    while True:
      name=choice(file.readlines())[:-1]
      botnames[i] = name
      if name in botnames:
        pass
      else:
        break
for i in range(3-bots):
  botnames.popitem()
shuffle(botnames)

for i in range(bots):
  hands.pop()
for i in range(7):
  for hand in hands:
    deal(hand)


colorprint(deck)
print()
colorprint(handA)
print(botnames)

turn = -1
turndirection = 1
while True:
  turn += turndirection
  x = turn%(bots+1)
  print(turn, bots+1, x)
  if turn==100:
    break