def done(x):
  if x.upper()!='DONE':
    return True
  else:
    return False
count=0
while done(input('Count More? ')):
  print(count)
  count+=1
y=input('\nEnter Number: ')
while done(y):
  try:
    if int(y)%2==0:
      print('Even')
    else:
      print('Odd')
  except:
    pass
  y=input('Enter Number: ')