def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count


print(linecount('wc.py'))

#on powershell
#can do python wc.py
#or can open python and then import wc

if __name__ == '__main__':
    print(linecount('wc.py'))
    #this if hides the testing code