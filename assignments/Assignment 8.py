count=int(input('Count: '))
for i in range(10,(11+(count*4)),count):
  print(i)
print()
for i in range(5):
  print('hello'*(2**i))
print()
num1, num2, num3=int(input('Enter Number 1: ')), int(input('Enter Number 2: ')), 5
for i in range(5):
  print(num3)
  num3+=num1
  print(num3)
  num3+=num2