def main(x):
  try:
    if int(x)%2==0:
      x='Even'
    elif int(x)%2==1:
      x='Odd'
  except:
    x='Invalid'
  return x
y=input('Enter a number: ')
while y.upper()!='DONE':
  print(main(y))
  y=input('Enter a number: ')