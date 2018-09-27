# team = 'New England Patriots'
# letter = team[1] #The expression in brackets is called an index. 
# print(letter)

# print(team[0])
# #index must be integers

# len(str(2**10000))

# #last character?
# team[-1]
# team[len(team)-1]
# #team[-20] = team[0]

#Traversal with a for loop
# index = 0
# while index < len(team):
#     letter = team[index]
#     print(letter)
#     index = index + 1

# Another way
# for letter in team:
#     print(letter)

##exercise 1
# prefixes = 'JKLMNOPQ'
# suffix = 'ack'
# for letter in prefixes:
#     if letter == 'O' or letter =='Q':
#         print(letter + 'u' + suffix)
#     else:
#         print(letter + suffix)

# team = 'New England Patriots'
# print(team[0:11]) #11 is exclusive not inclusive
# print(team[:11])
# print(team[12:20])
# print(team[12:])
# print(team[:])
# #step size
# print(team[0:20:2])
# print(team[::2])
# print(team[::-2]) #backwards intervals

#Strings are immutable and can't be changed after declared
# team = 'New England Patriots'
# new_team = team[:12]+'Seahawks'
# print(new_team)

# def find(word, letter):
#     index = 0
#     while index < len(word):
#         if word[index] == letter:
#             return index
#         index = index + 1
#     return -1

# print(find(team, 'E'))

#needs enumerate to use a for loop for this
# for i in range(len(team)):
#     ...:     if team[i] == 'a':
#     ...:         print(i)

# for i, letter in enumerate(team):
#     if letter == 'a':
#         print(i, letter)


#looping and counting
# def count(s, let):
#     c = 0
#     for letter in s:
#         if letter == let:
#             c = c + 1
#     print(c)

# count('hello', "l")


#string methods
# team = 'New England Patriots'
# new_team = team.upper()
# print(new_team)
# index = team.find('a')
# print(index)
# team.split('a')

# s = '        abc            '
# s.strip()
#gets rid of all spaces

# 'a' in team # returns True
#does this container contain the elements

# groceries = 'bananas apples bread'
# groceries.split()

# team = 'New England Patriots'
# index = team.find('a')
# print(index)
# print(team.find('En'))
# print(team.find('a', 10))
# #slices the string and finds awithin the slice (after 10)
# team.casefold()
# team.center(50)
# team.count('a')
# team.encode()
# team.endswith('Patr')
# 'the sum of 1 + 2 is {hello}'.format(hello=3)

# class Default(dict):
#     def __missing__(self, key):
#         return key
# print('{name} was born in {country}'.format_map(Default(name='Guido')))

# team.join(['a', 'b', 'c'])

# team.ljust(50)
# team.lower()
# team.lstrip('e')
# 'www.example.com'.lstrip('cmowz.')
# team.partition('n')
# team.replace('Patriots', 'Seahawks')
# team.rfind('a')
# team.rindex('a')
# team.rjust(50)
# team.split()
# team.split(maxsplit = 1)
# team.split('a', 1)
# team.strip()
# a = '#....... Section 3.2.1 Issue #32 .......'
# a.strip('.# S 2 ! ')
# a.swapcase().swapcase()
# b = 'hello hello hello lsadfkl'
# b.title()
# print

# #exercise 3
# # Split
# x = 'the quick brown fox jumps over the lazy dog'
# new_x = x.split(' ')
# for word in new_x:
#     print(word)

# # Strip
# y = '       ;lakjf.                  '
# new_y = y.strip()
# print(new_y)

# # Replace
# a = 'Hello hello hello hello.'
# new_a = a.replace('h', 'H')
# print(new_a)
