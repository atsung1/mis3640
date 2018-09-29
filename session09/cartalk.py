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

find_word()