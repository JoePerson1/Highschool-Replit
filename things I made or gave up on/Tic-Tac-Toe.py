import random
ABC=DEF=GHI=ADG=BEH=CFI=AEI=CEG='NNN'
win_c={ABC:'',DEF:'',GHI:'',ADG:'',BEH:'',CFI:'',AEI:'',CEG:''}
A=B=C=D=E=F=G=H=I='N'
corner=('A','C','G','I')
side=('B','D','F','H')
for t in range(9):
  comp=random.choice(list(win_c))
  #make it so it adds the thing
  if t==5:
    win_c[9]=(no)
  print('Computer plays '+comp)
  for i in win_c:
    if i=='XXX':
      print('Computer wins')
      break
    elif 'X' in i and 'O' in i and 'N' in i:
      if t==2:
        no=i
        win_c.pop(i)
    elif 
  user=input('Your move: ').upper()
  #copy line 9ish comment here