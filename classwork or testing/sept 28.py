namelist=[]
while True:
  x,y,name=input('First Name: ').capitalize(),input('Last Name: ').capitalize(),[]
  if x=='':
    break
  name.append(x+' '+y)
  namelist.append(name)
print(namelist)