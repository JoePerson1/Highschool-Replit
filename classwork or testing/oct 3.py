def red(x):
  x='\033[31m'+x
  return x
i=input('\033[0m'+'Enter something: ')
while i.upper()!='DONE':
  print(red(i))
  i=input('\033[0m'+'Enter something: ')