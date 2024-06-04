x=input('Enter a height:\n')
print('Height in inches: '+str((int(x[:x.find('\'')]))*12+int(x[x.find('\'')+1:x.find('\"')])))