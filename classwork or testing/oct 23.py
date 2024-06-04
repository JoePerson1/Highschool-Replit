from random import *

def main():
  while True:
    r1,r2=randint(1,10),randint(1,3)
    try:
      u=input('Enter Number: ')
      if u.lower()=='done':
        break
      u=int(u)
      modulus(u)
      add(u,r1)
      power(u,r2)
    except:
      print('Invalid Input\n')

def modulus(u):
  if u%2==0:
    print('Even')
  else:
    print('Odd')

def add(u,r1):
  print('Plus '+str(r1)+': '+str(u+r1))

def power(u,r2):
  print('Power of '+str(r2)+': '+str(u**r2)+'\n')

main()