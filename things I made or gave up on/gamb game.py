import random
cash = 10000
print('Goal: Make $100,000\nBalance: $10,000')
while True:
  chance = random.randint(1, 2)
  bet=input('Bet: ')
  while True:
    try:
      bet=int(bet)
      break
    except:
        bet=input('Invalid amount\nBet: ')
  while bet>cash or bet<0:
    bet = int(input('Invalid amount\nBet: '))
  if chance==1:
    print('You won $'+str(bet))
    cash+=bet
  elif chance==2:
    print('You lost $'+str(bet))
    cash-=bet
  print('Balance: $' + str(cash))