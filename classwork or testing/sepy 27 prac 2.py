count,list=0,[]
while True:
  x=input('Enter number: ').upper()
  count+=1
  if x.isalpha()==True:
    break
  elif int(x)%2==0:
      list[count]=x
print(list)