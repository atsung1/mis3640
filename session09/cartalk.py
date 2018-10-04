fin = open("session09/words.txt")

def find_word():
    for line in fin:
        word = line.strip()
        if riddle(word):
            print(word)

def riddle(word):
    for x in range(len(word)-5):
        if word[x] == word[x+1]:
            if word[x+2] == word[x+3]:
                if word[x+4] == word[x+5]:
                    return True
    return False

# find_word()

def ageriddle():
    pass
    """
    “Recently I had a visit with my mom and we realized that the two digits that make up my age
    when reversed resulted in her age. For example, if she’s 73, I’m 37. We wondered how often this
    has happened over the years but we got sidetracked with other topics and we never came up with an answer.

    “When I got home I figured out that the digits of our ages have been reversible six times so far.
    I also figured out that if we’re lucky it would happen again in a few years,
    and if we’re really lucky it would happen one more time after that. In other words,
    it would have happened 8 times over all. So the question is, how old am I now?”
    """
    for i in range(10, 100):
        age = str(i)
        for x in range(11,100):
            age1 = str(x)
            if age[0] == age1[1]:
                if age[1] == age1[0]:
                    print(age)

# ageriddle()
