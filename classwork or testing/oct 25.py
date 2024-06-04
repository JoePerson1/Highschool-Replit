from random import *

def three():
  global classroom
  group=[]
  for i in range(len(classroom)):
    x=choice(classroom)
    classroom.remove(x)
    group.append(x)
    if len(group)==3:
      print(group)
      group=[]

def notthree(y):
  global classroom
  group=[]
  for i in range(y*2):
    x=choice(classroom)
    group.append(x)
    classroom.remove(x)
    if len(group)==2:
      print(group)
      group=[]

classroom=[]
while True:
  student=input('Student: ')
  if student.lower()=='done':
    break
  classroom.append(student)
if len(classroom)%3==0:
  three()
elif len(classroom)%3==1:
  notthree(2)
  three()
elif len(classroom)%3==2:
  notthree(1)
  three()