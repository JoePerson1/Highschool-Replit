import random
count, a, set, zero, zero_hun, one_hun, two_hun, three_hun, four_hun, five_hun, six_hun, seven_hun, eight_hun, nine_hun=1, 0, [1,-1], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
while abs(a)<1000:
  count+=1
  x=random.choice(set)
  a=a+x
  print('\033[F\033[F\033[F\033[F\033[F\033[F\033[F\033[F\033[F\033[F\033[F\033[F\033[Fcount: '+str(count)+'\nchance: '+str(a)+'\nzeros: '+str(zero)+'\n00: '+str(zero_hun)+'\n100: '+str(one_hun)+'\n200: '+str(two_hun)+'\n300: '+str(three_hun)+'\n400: '+str(four_hun)+'\n500: '+str(five_hun)+'\n600: '+str(six_hun)+'\n700: '+str(seven_hun)+'\n800: '+str(eight_hun)+'\n900: '+str(nine_hun))
  if a==0:
    zero+=1
  if 0<abs(a)<100:
    zero_hun+=1
  if 100<=abs(a)<200:
    one_hun+=1
  if 200<=abs(a)<300:
    two_hun+=1
  if 300<=abs(a)<400:
    three_hun+=1
  if 400<=abs(a)<500:
    four_hun+=1
  if 500<=abs(a)<600:
    five_hun+=1
  if 600<=abs(a)<700:
    six_hun+=1
  if 700<=abs(a)<800:
    seven_hun+=1
  if 800<=abs(a)<900:
    eight_hun+=1
  if 900<=abs(a)<1000:
    nine_hun+=1