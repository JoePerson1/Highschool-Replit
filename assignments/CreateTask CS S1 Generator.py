from random import *
def gen():
  studentNum = randint(1, 100)
  optionNum = randint(1, studentNum)
  priorityNum = randint(1, optionNum)
  print('StudentNum = ' + str(studentNum))
  print('OptionNum = ' + str(optionNum))
  print('PriorityNum = ' + str(priorityNum))
  count = 0
  mainList = []
  for i in range(1, studentNum + 1):
    studentList = []
    student = 'bob' + str(i)
    studentList.append(student)
    pickedOptions = []
    for a in range(priorityNum):
      pick = 'group' + str(randint(1, optionNum))
      while pick in pickedOptions:
        pick = 'group' + str(randint(1, optionNum))
      pickedOptions.append(pick)
      studentList.append(pick)
    #print(studentList)
    mainList.append(studentList)
  return mainList
#no one has their priority as something
#evenly split groups: true/false
#group can have no one in it: true/false
def gen2():
  print('Characteristics:')
  for i in 
  
  #make it a function