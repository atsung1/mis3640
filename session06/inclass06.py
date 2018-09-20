#conditoinal statements
    # age = input('please enter your age: ')

    # if int(age) > 18:
    #     print('adult')
    # elif int(age) >= 6: #we can have as many else ifs as we need
    #     print('teenager')
    # else:
    #     print('kid')

#nested conditionals

#exercise 1.1: BMI calculator
# import webbrowser

# weight = input('please enter your weight in kg ')
# height = input('please enter your height in meters ')

# def calculateBMI(w, h):
#     bmi = float(w) / (float(h) ** 2)
#     if bmi <= 18.5:
#         webbrowser.open(insert url here)
#         return 'underweight'
#     elif bmi < 24.9:
#         return 'normal weight'
#     elif bmi < 29.9:
#         return 'overweight'
#     else:
#         return 'obesity'

# print(calculateBMI(weight, height))

#exercise 1.2:

# def twovars(varA, varB):
#     if type(varA) == str or type(varB) == str:
#         print('string involved')
#     elif varA > varB:
#         print('bigger')
#     elif varA == varB:
#         print('equal')
#     else:
#         print('smaller')

# a = 'hi'
# b = 3
# c = 5
# twovars(a, b)
# twovars(b, c)


# def compare(varA, varB):
#     if isinstance(varA, str) or isinstance(varB, str): #if and elif can be an or
#         print('string involved')
#     else:
#         if varA > varB:
#             print('bigger')
#         elif varA == varB:
#             print('equal')
#         else:
#             print('smaller')

# compare(a,b)
# compare(b, c)

#codingbat

# def diff21(n):

#  if n > 21:
#    return 2*abs(n-21)
#  else:
#    return abs(n-21)

# def cigar_party(cigars, is_weekend):
#   return is_weekend and cigars >= 40 or 40 <= cigars <= 60
  #and has higher priority over or

# try coding bat because quiz


#recursion
# def countdown(n):
#     if n <= 0:
#         print('Blastoff!')
#     else:
#         print(n)
#         countdown(n-1)

# countdown(5)

# def print_n(s, n):
#     if n <= 0:
#         return
#     print(s)
#     print_n(s, n-1)

# print_n('hello', 2)