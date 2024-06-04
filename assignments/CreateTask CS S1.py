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
  #first priority sorting
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
  print(0)
  print(groups)
  print(0.1)
  print(finalGroups)
  #check if none overflow
  noOverflow = True
  for group in groups:
    if len(group) > maxGroup:
      noOverflow = False
  if noOverflow is True:
    return groups
  #resorting
  globalCount = 1
  globalCount2 = 0
  while True:
    globalCount2 += 1
    if globalCount2 == globalCount*studentNum or globalCount <= 1:
      globalCount += 1
    #sort capped groups
    count = -1
    for group in groups:
      count += 1
      if len(group) == maxGroup:
        finalGroups[count] = group
        groups[count] = 'i'
    #check for finish
    finish = True
    for group in groups:
      if len(group) > maxGroup:
        finish = False
    if finish is True:
      return finalGroups
    print(1)
    print(groups)
    print(1.1)
    print(finalGroups)
    #find low group
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
    #actual sorting
    breack = False
    print('a         '+str(lowGroup))
    for group in groups:
      if breack is True:
        break
      if group == 'i':
        continue
      if len(group) > maxGroup:
        print('a')
        for person in group:
          if breack is True:
            break
          for personPriorities in mainList:
            #print(personPriorities[0], person, personPriorities[globalCount], lowGroup)
            if personPriorities[0] == person and personPriorities[globalCount] == lowGroup:
              print('b')
              group.remove(personPriorities[0])
              count = -1
              for option in optionList:
                count += 1
                if option == lowGroup:
                  print('c')
                  groupIndex = count
              groups[groupIndex].append(personPriorities[0])
              breack = True
              break
              #if their 2nd priority or lower is the last group then append
              #then make it so that this lowgroup is excluded next time
              #dont forget finalgroups
    print(2)
    print(groups)
    print(2.1)
    print(finalGroups)
      

    
while True:
  print(priority(int(input('How many students do you have?\n')), \
          int(input('How many options does each student have to pick from?\n')), \
          int(input('How many options does each student have to select for their priority list?\n'))))

#if noone has their priority as something