#format: r, n, p
#r3r2b4p
#c[i1][2]2.3l1.3b[i1][22]1.8p1.6a[cs1-1][3i][2233]
#c
#c[1i2]2.3l1.3b[2i22]1.8p1.6a[cs1-1][3i2233]


def fnth(group,thing,n):
   start = group.find(thing)
   while start >= 0 and n > 1:
       start = group.find(thing, start+len(thing))
       n -= 1
   return start

def fletter(string,start):
   for i in string[start:]:
     if i.isalpha() == True:
       return i.capitalize()

def fnum(string,start):
  x = ''
  for i in string[:start:-1]:
    if i.isdigit() == True:
      x += i
    else:
      break
  
  for i in string[start+1::1]:
    if i.isdigit() == True:
      x += i
    else:
      break

def custom():
   while True:
       for a in range(1, len(code)):
           fnth(code,'.',a)
           for b in code[fnth:]:
               if b.isalpha() == True:
                   diction[b.capitalize()] =
                   break




diction = []
code = input('Enter: ')
format = code[:1]


if format == 'c':
   custom()
elif format ==


