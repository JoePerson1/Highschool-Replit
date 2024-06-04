#Copy and paste the quiz code you had IN A NEW REPL and adds the following options.
#Provide the user two options. To do the first 5 problems or to do all 10 problems. The score of A, B, C, D, or F at the end should still apply regardless of which route they chose.
#If the user gets a questions wrong, give them one additional chance per problem to get it correct.
#At the conclusion, ask the user if they are going to do quiz corrections. If they say yes, let them know their possible score after quiz corrections (they would get half of their missed points back).

count=0
option=input('Pick an option:\n-Option 1:\n\tAnswer the first 5 questions\n-Option 2:\n\tAnswer all 10 Questions\nYour grade will still be based out of the\ntotal questions you\'ve answered.\nEnter your answer as 1 or 2 for each\nof their respective options.\n\n')
if option=='1':
  print('\033[FOption 1 selected')
elif option=='2':
  print('\033[FOption 2 selected')
else:
  print('\033[FInvalid option selected\nOption 1 has been selected by default')
  option='1'
print('\nQuiz:\n\nEnter your answer in terms of\nthe letter it is assigned to')
if input('\nWhats 52-29?\n\tA. 33\n\tB. 19\n\tC. 23\nAnswer: ').upper()=='C':
  count+=1
else:
  if input('Incorrect! Please reanswer\nAnswer: ').upper()=='C':
    count+=1
if input('\nWhats 12/4?\n\tA. 3\n\tB. 1\n\tC. 2\nAnswer: ').upper()=='A':
  count+=1
else:
  if input('Incorrect! Please reanswer\nAnswer: ').upper()=='A':
    count+=1
if input('\nWhats 5**2?\n\tA. 16\n\tB. 25\n\tC. 26\nAnswer: ').upper()=='B':
  count+=1
else:
  if input('Incorrect! Please reanswer\nAnswer: ').upper()=='B':
    count+=1
if input('\nWhats 11*12?\n\tA. 121\n\tB. 101\n\tC. 132\nAnswer: ').upper()=='C':
  count+=1
else:
  if input('Incorrect! Please reanswer\nAnswer: ').upper()=='C':
    count+=1
if input('\nWhats 54/3?\n\tA. 17\n\tB. 19\n\tC. 18\nAnswer: ').upper()=='C':
  count+=1
else:
  if input('Incorrect! Please reanswer\nAnswer: ').upper()=='C':
    count+=1
#Second part
if option=='2':
  if input('\nWhats the remainder of 94/7\n\tA. 0\n\tB. 3\n\tC. 10\nAnswer: ').upper()=='B':
    count+=1
  else:
    if input('Incorrect! Please reanswer\nAnswer: ').upper()=='B':
      count+=1
  if input('\nWhats the 52% of 200?\n\tA. 102\n\tB. 104\n\tC. 52\nAnswer: ').upper()=='B':
    count+=1
  else:
    if input('Incorrect! Please reanswer\nAnswer: ').upper()=='B':
      count+=1
  if input('\nIs 153 divisible by 3?\n\tA. Yes\n\tB. No\nAnswer: ').upper()=='A':
    count+=1
  else:
    if input('Incorrect! Please reanswer\nAnswer: ').upper()=='A':
      count+=1
  if input('\nIs 133 a prime number?\n\tA. Yes\n\tB. No\nAnswer: ').upper()=='B':
    count+=1
  else:
    if input('Incorrect! Please reanswer\nAnswer: ').upper()=='B':
      count+=1
  if int(input('\nHow many questions did\nyou get right so far?\n\nEnter you answer as a number:\n\tA. 1\n\tB. 2\n\tC. 3\n\tD. 4\n\tE. 5\n\tF. 6\n\tG. 7\n\tH. 8\n\tI. 9\nAnswer: '))==count:
    count+=1
  else:
    if int(input('Incorrect! Please reanswer\nAnswer: '))==count:
      count+=1
if option=='2':
  print('\nYou got '+str(count)+' out of 10 right!')
  print('Percentage: '+str((((5-count)/2)+(count))*10)+'%')
else:
  print('\nYou got '+str(count)+' out of 5 right!')
  print('Percentage: '+str((+(count))*20)+'%')
#fix grade
#thing can't go higher than max
if option=='2':
  grade_count=count/10
else:
  grade_count=count/5
if grade_count<.6:
  grade='F'
elif .6<=grade_count<.7:
  grade='D'
elif .7<=grade_count<.8:
  grade='C'
elif .8<=grade_count<.9:
  grade='B'
elif grade_count>=.9:
  grade='A'
print('Grade: '+grade)
#quiz corrections
if input('\nAre you going to do quiz corrections?\nY/N: ').upper()=='Y':
  if option=='2':
    print('\nScore after quiz corrections:\n'+str(((10-count)/2)+(count))+' out of 5\nPercentage: '+str((((10-count)/2)+(count))*10)+'%\nGrade: ')
  else:
    print('\nScore after quiz corrections:\n'+str(((5-count)/2)+(count))+' out of 5\nPercentage: '+str((((5-count)/2)+(count))*20)+'%\nGrade: ')
else:
  print('End')