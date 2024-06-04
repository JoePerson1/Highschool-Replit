list,name=[],input('Enter student name: ')
while name!='':
  list.append(name.upper())
  name=input('Enter student name: ')
print(list)
if input('\nWho do you want to search for? ').upper() in list:
  print('That is in the list')
else:
  print('That is not in the list')