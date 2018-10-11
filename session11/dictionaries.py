# # # # names = ['Defne', 'Jack', 'Angela']
# # # # scores = [95, 75, 85]

# # # grades = dict()
# # # # print(grades)

# # # # grades['Defne'] = 90
# # # # # creates an item that maps from the key 'Defne' to the value 90
# # # # print(grades)

# # # grades ={'Defne': 90, 'Jack': 75, 'Angela': 85}
# # # print(grades)
# # # # # You might get different order of the key-value paris
# # # # # In general, the order of items in a dictionary is unpredictable.

# # # print(grades['Jack'])
# # # # print(grades['Sarah'])
# # # # print(len(grades))

# # # # 'Jack' in grades # only check the keys
# # # 90 in grades.values()

# def histogram(s):
#     d = dict()
#     for c in s:
#         if c not in d:
#             d[c] = 1
#         else:
#             d[c] += 1
#     return d

# h = histogram('Bookkeeper')
# # print(h)

# # number_of_e = h.get('e', 0)
# # number_of_a = h.get('a', 0)
# # print(number_of_e)
# # print(number_of_a)

# # # #ex 1
# def histogram1(s):
#     d = dict()
#     for c in s:
#         d[c] = d.get(c, 0) + 1
#     return d

# h1 = histogram1('Bookkeeper')
# # print(h1)

# def reverse_lookup(d, v):
#     for k in d:
#         if d[k] == v:
#             return k
#     raise LookupError('Value does not exist')

# h = histogram('Massachusetts')
# key = reverse_lookup(h, 2)
# # print(key)

# def invert_dict(d):
#     inverse = dict()
#     for key in d:
#         val = d[key]
#         if val not in inverse:
#             inverse[val] = [key]
#         else:
#             inverse[val].append(key)
#     return inverse
# hist = histogram('parrot')
# print(hist)


import random
class_roster = ['Ang', 'Jack', 'Iris']
grades = {}
letters = ['A', 'B', 'C', 'D', 'F']
for name in class_roster:
    if name[0] == 'A':
        grades[name] = random.randint(60,90)
    else:
        grades[name] = random.choice(letters)
print(grades)
scores = grades.values()
print(scores)