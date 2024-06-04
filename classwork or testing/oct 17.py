def main(x,y):
  try:
    z=int(x)+int(y)
    return 'Sum: '+str(z)
  except:
    return 'Invalid Number(s)'
while True:
  print(main(input('Number 1: '),input('Number 2: ')))