count=0
print('Grade 3 Mathematics Test:\n\tEnter you answers as a letter\n\tunless instructed otherwise\n')
if input('\nWhats 52-29?\nA. 33\nB. 19\nC. 23\n').upper()=='C':
  count+=1
if input('\nWhats 12/4?\nA. 3\nB. 1\nC. 2\n').upper()=='A':
  count+=1
if input('\nWhats 5**2?\nA. 16\nB. 25\nC. 26\n').upper()=='B':
  count+=1
if input('\nWhats 11*12?\nA. 121\nB. 101\nC. 132\n').upper()=='C':
  count+=1
if input('\nWhats 54/3?\nA. 17\nB. 19\nC. 18\n').upper()=='C':
  count+=1
if input('\nWhats the remainder of 94/7\nA. 0\nB. 3\nC. 10\n').upper()=='B':
  count+=1
if input('\nWhats the 52% of 200?\nA. 102\nB. 104\nC. 52\n').upper()=='B':
  count+=1
if input('\nIs 153 divisible by 3?\nA. Yes\nB. No\n').upper()=='A':
  count+=1
if input('\nIs 133 a prime number?\nA. Yes\nB. No\n').upper()=='B':
  count+=1
if int(input('\nHow many questions did\nyou get right so far?\n\tEnter you answer as a number:\nA. 1\nB. 2\nC. 3\nD. 4\nE. 5\nF. 6\nG. 7\nH. 8\nI. 9\n'))==count:
  count+=1

print('You got '+str(count)+' out of 10 right!')
percent=count*10
print('Percentage: '+str(percent)+'%')
if count<6:
  grade='F'
elif count==6:
  grade='D'
elif count==7:
  grade='C'
elif count==8:
  grade='B'
elif count>8:
  grade='A'
print('Grade: '+grade)