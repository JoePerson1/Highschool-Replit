from math import *

def factor(product, sum):
  productall=[]
  try:
    product=int(product)
    sum=int(sum)
  except:
    return 'Invalid Number(s)'
  for i in range(-ceil(sqrt(abs(product)))+1, \
                 floor(sqrt(abs(product)))+1):
    productone=[]
    if i == 0:
      continue
    elif product%i == 0:
      productone.append(i)
      productone.append(product//i)
      productall.append(productone)
  for a in productall:
    if a[0]+a[1] == sum:
      return 'Solution: '+str(a)
  return 'No Solution'

while True:
  print(factor(input('Product: '), input('Sum: ')))