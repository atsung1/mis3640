#Variables, expressions, and statements
# print('Hello,world!')

# print('Hey Jude, Don\'t make it bad')
#backslash will ignore the quotation mark in the string

# print('The sum is', 2 + 2 + 2 + 2)

# name = input()
# print('Hello', name)

# variables are stored in the RAM
# message = "I learned something cool today" string
# n = 100 #integer
# pi = 3.14 #float
#variable names can contain letters, numbers, and underscore, cannot begin with number; conventionally only lower case
#cannot use reserved keywords in python

# print(n)

#expression: combination of values/variables/operators
#statement: unit that has an effect, like creating or displaying a variable/value

#dynamic language: variables can be declared again

# x = 10
# print (x)
# x = x + 2
# print (x)
# x = 'x + 2'
# print(x)

# a = 'ABC'
# b = a
# a = 'XYZ'
# print(b)

# '2' - '1'
#minus sign not supported between 2 strings
#can use + sign between two strings (concatenate)
# '2' + '1'

# first_name = 'Angela'
# last_name = 'Tsung'
# name = first_name + ' ' + last_name
# print(name)

# print('Hello, {}'.format('world'))
#brackets is a placeholder; will replace with what's in the format function
# name = 'python'
# print('Hello, {}'.format(name))

# print('Congratulations, {:s}, you won {:d}th Academy Award'.format(name, 90))

# print('Pi equals {:10.2f}'.format(3.14156265))
#f = floating decimal numbers
#the number before the . is the number of placeholders, if you ad a 0 it fills the spaces with 0s

# print('Growth rate: {:.2f}%'.format(2.5))

# print('Coordinates of Babson: {lat}, {lon}'.format(lat='42.30N', lon='71.27W'))
#the order of declaring variables in the format funciton doesn't matter