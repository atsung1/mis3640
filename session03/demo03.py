# 3.14e-2 #scientific notation
# len(str(2**1000000)) #number of digits

# import math
# import random
# print(random.random())
# random.choice([1, 2, 3, 4])

# Strings
# \ = escape sign, will escape the following chracter no matter what it is
# print('I\'m \"ok\".')
# print('I\'m learning\nPython.') #\n = new line
# print('\\\n\\')
# can use r for all escapes as well
# print(r'\\\t\\')
# 3 single quotations is the same as \n

# Boolean values: True and False are capitalized
# current_time = 4
# if current_time > 5:
#     print('calss is over')
# else:
#     print('You cannot leave yet')

# what's a recipe:
# sequence of steps
# flow of control
# knowing when to stop

# age = int(input('Please enter your age:'))
# if age > 21: #conditional statements
#     print('yes, you can.')
# else:
#     print('sorry, you cannot.')

# = is assign
#== is equals
#// returns int after division


#3. The time module provides a function, also named time, that returns the current Greenwich Mean Time in “the epoch”, which is an arbitrary time used as a reference point. On UNIX systems, the epoch is 1 January 1970.
#Write a script that reads the current time and converts it to a time of day in hours, minutes, and seconds, plus the number of days since the epoch.
import time
print(time.time())
minutes = time.time()//60
hours = time.time()/60//60
days = time.time()/60/60//24
seconds = time.time() - time.time()/60/60/24
print('Since the epoch it has been {} days {} hours {} minutes {} seconds'.format(int(days), int(hours), int(minutes), int(seconds)))