name,phonebook=input('Name: ').upper(),{'JOE':'(317) 123-4567','JOHN':'(317) 234-5678','JACK':'(317) 345-6789','JAKE':'(317) 456-7890'}
while name.upper()!='DONE':
  x=0
  for i in phonebook:
    if name==i:
      print(phonebook[i])
      x+=1
  if x==0:
    print('Sorry, I don\'t know them')
  name=input('Name: ').upper()