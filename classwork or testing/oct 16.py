def main(x):
  if x%2==0:
    print('Even')
  else:
    print('Odd')

main(int(input('Pick a Number: ')))

num,add=[],input('Number: ')
while add.upper()!='DONE':
  num.append(int(add))
  add=input('Number: ')
print(set([num for num in num if num%2==0]))