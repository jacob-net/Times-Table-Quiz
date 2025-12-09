import random
score = 0
table_number = int(input('What times table would you like?'))
print('You entered:',table_number)
for jc in range(10):
  factor = random.randint(0,12)
  print('What is',factor,'x',table_number,'?')
  answer = int(input())
  if factor * table_number == answer:
    print('correct!')
    score = score +1
  else:
    print('incorrect! Answer:',factor * table_number)
  #end if
#next jc
print('Score: ',score,'/10',sep = '')
