list=['RED','ORANGE','YELLOW','GREEN','BLUE','PURPLE']
while list!=[]:
  try:
    list.remove(input('Rainbow Color: ').upper())
  except:
    print('\nAlready guessed or Wrong\n')
print('Good Job')