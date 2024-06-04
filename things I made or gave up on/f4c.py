# an6s2p1.2
# bn6p1.2|s2f2

def npq(code):
  n = s = p = ''
  ivars = [n, s, p]
  iletters = ['n', 's', 'p']
  for a in range(len(ivars)):
      for b in code[code.find(iletters[a]) + 1:]:
          if b.isalpha() is True or b == '|':
              break
          ivars[a] += b
  n, s, p = ivars[0], ivars[1], ivars[2]
  n, s = int(n), int(s)
  f = n - s
  q = str(nd('d', p) - nd('n', p)) + '.' + str(nd('d', p))
  return [n, s, f, p, q]

def nd(nd, l):
  if nd == 'n':
      l = l[:l.find('.')]
  elif nd == 'd':
      l = l[l.find('.') + 1:]
  return int(l)

def lm(code, inums):
  l = m = ''
  if code[code.find('l')] == -1 and code[code.find('m')] == -1:
      return None
  if code.find('l') != -1:
      for i in code[code.find('l') + 2:]:
          if i.isdigit() is True:
              l += i
          else:
              break
      if code[code.find('l') + 1] == 'f':
          l = inums[0] - int(l)
      l = int(l)
  else:
      l = 0
  if code.find('m') != -1:
    for i in code[code.find('m') + 2:]:
        if i.isdigit() is True:
            m += i
        else:
            break
    if code[code.find('m') + 1] == 'f':
        m = inums[0] - int(m)
    m = int(m)
  else:
    m = inums[0]
  return [l, m + 1]

def specific(code):
  # [n, s, f, p, q]
  inums = npq(code)
  if lm(code, inums) == None:
      pass
  else:
      nrange = lm(code, inums)
  nrange = [inums[0], inums[0] + 1]
  for e in range(nrange[0], nrange[1]):
      numer = 1
      denom = 1
      for i in range(inums[0], inums[2], -1):
          numer *= i
      for i in range(1, inums[1]+1):
          numer //= i
      temp = nd('n', inums[3])
      temp = temp ** inums[1]
      numer *= temp
      temp = nd('n', inums[4])
      temp **= inums[2]
      numer *= temp
      pass
      temp = nd('d', inums[3])
      temp = temp ** inums[1]
      denom *= temp
      temp = nd('d', inums[4])
      temp **= inums[2]
      denom *= temp
  return str(numer) + '/' + str(denom)


while True:
  code = input('Enter: ')
  if code[0].lower() == 'a':
      print(specific(code))
  if code[0].lower() == 'b':
      pass
      # how many tries to have a chance of...
      # prob to have at least ... and at most ...