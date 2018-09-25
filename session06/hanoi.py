def move(n, source, bridge, destination):
    if n >= 1:
        move(n-1, source, destination, bridge)
        print("{} --> {}".format(source, destination))
        move(n-1, bridge, source, destination)


# '''
# 2 A C B
#         1 A B C
#             print a-c
# print a - b
# 1 c a b
#     print c - b
# print a - b

# move 2, b, a, c
#     1 b, c, a
#         print b - a




# '''

move(3, 'A', 'B', 'C')
# Expected output:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C