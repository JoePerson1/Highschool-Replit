
import random
numbers=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#Uses Sequencing
#Uses Selection
#Uses Iteration
#Serves a practical purpose
#INCLUDE COMMENTS
#THEN, in your canvas response tell me:
#Lines of Selection
#Lines of Iteration
#It is a reasonable amount of work & serves a practical purpose.

#plan-sequencing for sequencing for splice
#selection for if
#interation for for

num='12'
book='i am doing a certain thing that is'
book_list=[]
book_temp=book
while True:
  book_index=book_temp.find(' ')
  print(book_index)
  book_temp=book[book_index+1:book.find(' ')]
  book_list.append(book_temp)
  if not book.find(' '):
    break
for b in book_list:
  book+=book_list[-b]
book=book_list[::-1]
password=book
print(password)
for l in range(len(password)):
  if random.choice(numbers)>7:
    password=password[:l]+num+password[l:]
password+=str(password.count(num))
print(password)