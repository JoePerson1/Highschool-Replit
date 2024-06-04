from math import ceil

def priority(studentNum, optionNum, priorityNum):
  maxGroup = ceil(studentNum / optionNum)
  mainList = []
  optionList = []
  for a in range(1, optionNum + 1):
    option = input('Option ' + str(a) + ': ').lower()
    optionList.append(option)
  print('\nGreatest Priority to Least Priority\nGreatest being 1\n')
  for b in range(1, studentNum + 1):
    studentList = []
    student = input('Student ' + str(b) + ': ').lower()
    studentList.append(student)
    for c in range(1, priorityNum + 1):
      priority = input(student + '\'s Priority ' + str(c) + ': ').lower()
      while priority not in optionList:
        priority = input(student + '\'s Priority ' + str(c) + ': ').lower()
      studentList.append(priority)
    mainList.append(studentList)
  groups = []
  finalGroups = []
  count = -1
  for i in optionList:
    groups.append([])
    finalGroups.append('i')
  for option in optionList:
    count += 1
    for personPriorities in mainList:
      if option == personPriorities[1]:
        groups[count].append(personPriorities[0])
  noOverflow = True
  for group in groups:
    if len(group) > maxGroup:
      noOverflow = False
  if noOverflow is True:
    return groups
  globalCount = 1
  globalCount2 = 0
  while True:
    globalCount2 += 1
    if globalCount2 == globalCount*studentNum or globalCount <= 1:
      globalCount += 1
    count = -1
    for group in groups:
      count += 1
      if len(group) == maxGroup:
        finalGroups[count] = group
        groups[count] = 'i'
    finish = True
    for group in groups:
      if len(group) > maxGroup:
        finish = False
    if finish is True:
      return finalGroups
    lowGroup = False
    count = -1
    for group in groups:
      count += 1
      if group == 'i':
        continue
      if lowGroup is False:
        lowGroup = group
        lowGroupName = optionList[count]
        continue
      if len(group) < len(lowGroup):
        lowGroup = group
        lowGroupName = optionList[count]
    lowGroup = lowGroupName
    breack = False
    for group in groups:
      if breack is True:
        break
      if group == 'i':
        continue
      if len(group) > maxGroup:
        for person in group:
          if breack is True:
            break
          for personPriorities in mainList:
            if personPriorities[0] == person and personPriorities[globalCount] == lowGroup:
              group.remove(personPriorities[0])
              count = -1
              for option in optionList:
                count += 1
                if option == lowGroup:
                  groupIndex = count
              groups[groupIndex].append(personPriorities[0])
              breack = True
              break

while True:
  print(priority(int(input('How many students do you have?\n')), \
          int(input('How many options does each student have to pick from?\n')), \
          int(input('How many options does each student have to select for their priority list?\n'))))