for i in range(10):
  print('ok')

def clear():
  print('yo')
  print(('\033[F'+'\x1b[2K')*15)
  print('yo')

clear()