from math import ceil
from random import *

def priority(studentNum, optionNum, priorityNum):
  maxGroup = ceil(studentNum / optionNum)
  mainList = []
  optionList = []
  for a in range(1, optionNum + 1):
    option = input('\nOption ' + str(a) + ': ').lower()
    optionList.append(option)
  print('\nGreatest Priority to Least Priority\nGreatest being 1')
  for b in range(1, studentNum + 1):
    studentList = []
    student = input('\nStudent ' + str(b) + ': ').lower()
    studentList.append(student)
    for c in range(1, priorityNum + 1):
      priority = input(student.capitalize() + '\'s Priority ' + str(c) + ': ').lower()
      while priority not in optionList:
        priority = input(student.capitalize() + '\'s Priority ' + str(c) + ': ').lower()
      studentList.append(priority)
    mainList.append(studentList)
  groups = []
  finalGroups = []
  for i in range(len(optionList)):
    groups.append([])
    finalGroups.append('i')
  for i, option in enumerate(optionList):
    for personPriorities in mainList:
      if option == personPriorities[1]:
        groups[i].append(personPriorities[0])
  globalCount = 1
  globalCount2 = 0
  while True:
    #max group
    sortGroup = sorted(groups)
    sortOption = []
    for i, option in enumerate(optionList):
      
    #b
    globalCount2 += 1
    if globalCount2 == globalCount*studentNum or globalCount <= 1:
      globalCount += 1
    finish = True
    for group in groups:
      if len(group) > maxGroup:
        finish = False
    if finish is True:
      for i, group in enumerate(groups):
        if group == 'i':
          continue
        finalGroups[i] = group
      return finalGroups, optionList
    for i, group in enumerate(groups):
      if len(group) == maxGroup:
        finalGroups[i] = group
        groups[i] = 'i'
    lowGroup = False
    for i, group in groups:
      if group == 'i':
        continue
      if lowGroup is False:
        lowGroup = group
        lowGroupName = optionList[i]
        continue
      if len(group) < len(lowGroup):
        lowGroup = group
        lowGroupName = optionList[i]
    lowGroup = lowGroupName
    group = resort(groups, maxGroup, lowGroup, mainList, optionList, globalCount)

def resort(groups, maxGroup, lowGroup, mainList, optionList, globalCount):
  for group in groups:
    if group == 'i':
      continue
    if len(group) > maxGroup:
      for person in group:
        for personPriorities in mainList:
          if personPriorities[0] == person and personPriorities[globalCount] == lowGroup:
            group.remove(personPriorities[0])
            for i, option in enumerate(optionList):
              if option == lowGroup:
                groupIndex = i
            groups[groupIndex].append(personPriorities[0])
            return group, optionList

def gen():
  studentNum = randint(1, 100)
  optionNum = randint(1, studentNum)
  priorityNum = randint(1, optionNum)
  print('StudentNum = ' + str(studentNum))
  print('OptionNum = ' + str(optionNum))
  print('PriorityNum = ' + str(priorityNum))
  mainList = []
  for i in range(1, studentNum + 1):
    studentList = []
    student = 'student' + str(i)
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

def main():
  groups, options = priority(int(input('How many students do you have?\n')), \
          int(input('How many options does each student have to pick from?\n')), \
          int(input('How many options does each student have to select for their priority list?\n')))
  for i, option in enumerate(options):
    print(option.capitalize() + ': ' + groups[i])

main()

#if noone has their priority as something
#list out group names
#sort biggest to lowest groups
#enumerate