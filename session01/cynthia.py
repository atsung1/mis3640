def string(character):
    index = 0
    while index < len(character):
        letter = character[len(character)-index-1]
        print(letter)
        index = index + 1

string('apple')