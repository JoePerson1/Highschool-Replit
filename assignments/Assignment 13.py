import random
a,b,c,d,e,f,g,h,i='A','B','C','D','E','F','G','H','I'
tdict={'A':'','B':'','C':'','D':'','E':'','F':'','G':'','H':'','I':'',}
win,corner,side,all,names=[a+b+c,d+e+f,g+h+i,a+d+g,b+e+h,c+f+i,a+e+i,c+e+g],[a,c,g,i],[b,d,f,h],[a,b,c,d,e,f,g,h,i],('A','B','C','D','E','F','G','H','I')
t=0
def cpick():
  t+=1
  global corner
  x=random.randint(0,8)
  corner[x]+='X'
  print('Computer plays: '+names[x])
cpick()
upick=input('User plays: ')
