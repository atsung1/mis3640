#Lists

# [10, 20, 30, 40]
# ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']

# b = ['spam', 2.0, 5, [10, 20]]
# b[3][0]
# b[0][2]

# b[3][1] = 'hello'

# AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
# numbers = [42, 123]
# empty = []
# print(AFC_east, numbers, empty)

# AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
# print('Buffalo Bills' in AFC_east)

# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', ['Ruby','On Rail'], 'PHP'],
#     ['Adam', 'Bart', 'Lisa']    
# ]
# print(L[0][0])
# print(L[-1][-1])
# print(L[1][2][1])

# for team in AFC_east:
#     print(team)

# numbers = [2, 0, 1, 6, 9]

# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 2
    
# print(numbers)

# my_list = ['spam', 1, ['New England Patriots', \
#                        'Buffalo Bills', 'Miami Dolphins', \
#                        'New York Giants'], \
#            [1, 2, 3]]
# print(my_list)
# print(len(my_list))

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(c)

# t = ['a', 'b', 'c', 'd', 'e', 'f']
# Q. How do we get ['b', 'c']? ['a', 'b', 'c', 'd']? ['d', 'e', 'f'] ? The entire list?
# t[1:3] = ['x', 'y']
# print(t)

#exercise 2
t = ['a', 'b', 'c']
t.append('d')
a = [1,2,3]
c = [4,5]
a.extend(c)
print(a)
b = [5,4,7,2,6,7]
b.sort()
print(b)