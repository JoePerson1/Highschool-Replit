name2=[]
def main():
  while True:
    name1,first,last=[],input('First Name: '),input('Last Name: ')
    if first.upper()=='DONE' or last.upper()=='DONE':
      break
    name1.append(first)
    name1.append(last)
    name2.append(name1)
    print(name1)
main()
print('\nNames:\n'+str(name2))