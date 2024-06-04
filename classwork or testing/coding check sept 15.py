count=int(input('How many numbers of the Fibonacci Sequence do you want?\n'))
first=0
second=1
print()
for i in range(count):
  if i%2==0:
    print(first)
    first=first+second
  elif i%2==1:
    print(second)
    second=first+second