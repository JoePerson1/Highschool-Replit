def prime(num):
  for i in range(2,abs(num//2)+1):
    if abs(num)/i==abs(num)//i:
      return 'Composite'
  return 'Prime'
while True:
  print(prime(int(input('Enter a number: '))))