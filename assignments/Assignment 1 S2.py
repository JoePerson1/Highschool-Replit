def difference(seq, row):
  lst=[]
  Adif = False
  pattern=True
  for i,num in enumerate(seq):
    if i==len(seq)-1:
      break
    dif=seq[i+1]-seq[i]
    lst.append(dif)
    if Adif==False:
      pass
    elif Adif != dif:
      pattern=False
    Adif=dif
  if pattern is True:
    return pattern, 'Add', row, dif,lst
  pattern=True
  Adif=False
  for i,num in enumerate(seq):
    if i==len(seq)-1:
      break
    if seq[i+1]%seq[i]==0:
      dif=seq[i+1]//seq[i]
    if Adif==False:
      pass
    elif Adif != dif:
      pattern=False
    Adif=dif
  return pattern, 'Mult', row, dif,lst

def split(seq):
  add=mult=[]
  for i, num in enumerate(seq):
    if i == len(seq)-2:
      break
    #x=seq[i+1]-seq[i]
    difference()

count=0
sequence=[]
while True:
  count+=1
  try:
    number=int(input('Number #'+str(count)+': '))
  except:
    break
  sequence.append(number)
print(sequence)
print(difference(sequence, '1'))
