num,num2=50,25
while True:
  print(num)
  user=input('Higher, lower, or correct? ').upper()
  if str(user).upper()=='HIGHER':
    num=round(num+num2)
    num2=round(num2/2)
  if str(user).upper()=='LOWER':
    num=round(num-num2)
    num2=round(num2/2)
  if str(user).upper()=='CORRECT':
    print('Game Over')
    break