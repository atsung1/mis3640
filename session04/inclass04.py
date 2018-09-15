# print(type(42))
# a = type(2)
# print(type (a)) # class is type

#inputs are always strings
# age = input('what is your age')
# int(age)

#abs = absolute value
#max is the max of multiple numbers

#try round(), min(), ord(), chr()

#python challenge
#g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.

# message = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
# new_message = ''
# for letter in message:
#     # if letter == ' ':
#     #     new_message += ' '
#     # else:
#     new_message += chr(ord(letter)+2)
# print(new_message)

#module.function ex: math.log10

# def print_lyrics():
#     print('asdf')
#     print('lsa;dfjsa;l')

# def print_twice(whatever): #using parameters
#     print('first time:')
#     print(whatever)
#     print('the second time:')
#     print(whatever)

# name = input('What is your name')
# print_twice(name)
# #range of variables // global or local
# def my_abs(n):
#     if n < 0:
#         return -round(n)
#     else:
#         return round(n)
# print(my_abs(14.5))

#local variable: when the function terminates, the variable is destroyed

#return values
# def give_a_break():
#     return 'break'

# print(give_a_break())

# def give_me_another_break():
#     str1 = 'break'
#     print('another break')
#     return str1 # returns are the end of the function


# print(give_me_another_break())

#pass just amkes the function run example:
# def nop():
#     pass

#argument checking
#return x,y

import math
def quadratic(a, b, c):
    if 2 * a == 0:
        print('Does not exist')
        return None
    else:
        one = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        two = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        return 'x = {} or x = {}'.format(one, two)
        #one, two

    #(-b+- sqrt b**2 - 4 a c) / 2 a

print(quadratic(100, 100, -10))