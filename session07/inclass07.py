result = 0

# for i in range(10):
#     print(i+1)
#     result = result + i + 1
# print(result)

# for i in range(10):
#     print('current number to be added:', i+1)
#     result = result + i + 1
#     print('new result after this iteration:', result)

# print('The final result:', result)

# for i in range(1,11):
#     print('current number to be added:', i)
#     result = result + i
#     print('new result after this iteration:', result)

# print('The final result:', result)

# exercise 1.3 sum of all odd integers from 1 to 1000
# for i in range(1, 1001):
#     if i%2 == 1:
#         result = result + i

# print('The sum of odd numbers is', result)

# #exercise 1.3 sum of all even integers from 1 to 1000
# for i in range(1, 1001):
#     if i%2 == 0:
#         result = result + i

# print('The sum of even numbers is', result)

# for i in range(1,11,3):
#     print(i)

result = 1
# #factorial of a number 10 using for loopo
# for i in range (1,10):
#     result = result * i
# print(result)
#last number is exclusive

# import time
# def countdown(n):
#     while n > 0:
#         print(n)
#         time.sleep(1)
#         n = n - 1
#     print('Blastoff!')

# countdown(5)


# counter = 0
# while counter < 10:
#     print(r"Here's Johnny!")
#     counter += 1

# a = 1
# a += 1
# print(a)

# message = 'angela'
# for whatever in message:
#     print(whatever)



#exercise 2

# iteration = 0
# count = 0
# while iteration < 5:
#     # the variable 'letter' in the loop stands for every 
#     # character, including spaces and commas!
#     for letter in "hello, world": 
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 

# iteration = 0
# while iteration < 5:
#     count = 0
#     for letter in "hello, world":
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 

# iteration = 0
# while iteration < 5:
#     count = 0
#     for letter in "hello, world":
#         count += 1
#         if iteration % 2 == 0:
#             break
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 

# while True:
#     line = input('> ')
#     print('press "q" to quit')
#     if line == 'q':
#         break
#     print(line)

# print('Done!')

# mysum = 0
# for i in range(5, 11, 2):
#     mysum += i
#     if mysum == 5:
#         break
# print(mysum)

a = 4
x = 3
y = (x + a/x) / 2
print(y)

x = y
y = (x + a/x) / 2
print(y)

x = y
y = (x + a/x) / 2
print(y)

x = y
y = (x + a/x) / 2
print(y)

x = y
y = (x + a/x) / 2
print(y)

x = y
y = (x + a/x) / 2
print(y)