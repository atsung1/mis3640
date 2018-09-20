def move(n, source, bridge, destination):
    if n >= 1:
        move(n-1, source, destination, bridge)
        print("{} --> {}".format(source, destination))
        move(n-1, bridge, source, destination)


move(3, 'A', 'B', 'C')
# Expected output:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C