dict={1:'one',2:'two',3:'three',4:'four',5:'five'}
for key in dict:
  if dict[key].find('two'):
    no=dict[key]
    print(key)
    index=key
    dict.pop(key)
    break
print(dict)
dict[index]=(no)
print(dict)