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

groceries = 'bananas apples bread'
groceries.split()