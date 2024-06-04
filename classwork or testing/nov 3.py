def alternate(x):
  y=''
  for i in range(len(x)):
    if i%2==0:
      y+=x[i].lower()
    else:
      y+=x[i].upper()
  return y
for i in range(3):
  print(alternate(input('Enter word: ')))