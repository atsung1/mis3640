fin = open("session09/words.txt")
# line = fin.readline()
# word = line.strip()
# print(word)

# counter = 0
# for line in fin:
#   word = line.strip()
#   counter += 1
#   # print(word)
# print(counter)

def read_long_words():
    """
    prints only the words with more than 20 characters
    """
    long_words = 0
    for line in fin:
      word = line.strip()
      if len(word) > 20:
        long_words += 1
        print(word)
        print(long_words)


# read_long_words()


def has_no_e(word):
    """
    returns True if the given word doesn’t have the letter “e” in it.
    """
    return not 'e' in word.lower()


# print(has_no_e('Babson'))
# print(has_no_e('College'))

def has_no_e_list():
  """
  print words with no e and compute % of words
  """
  no_e_words = 0
  total_words = 0
  for line in fin:
    word = line.strip()
    total_words += 1
    if has_no_e(word):
      no_e_words += 1
      print(word)
  print('{:.2f}% of words do not contain e'.format(no_e_words/total_words))

# has_no_e_list()

def avoids(word, forbidden):
    """
    takes a word and a string of forbidden letters, and that returns True
    if the word doesn’t use any of the forbidden letters.
    """
    for letter in forbidden:
      return not letter in word.lower()


# print(avoids('Babson', 'ab'))
# print(avoids('College', 'ab'))

def without_forbidden():
  forbidden = input('What are the forbidden letters?')
  avoids_words = 0
  for line in fin:
    word = line.strip()
    if avoids(word, forbidden):
      avoids_words += 1
  print('The number of words that don\'t contain the forbidden letters: {}'.format(avoids_words))

# without_forbidden()
# Can you find a combination of 5 forbidden letters that excludes the smallest number of words?????????

def uses_only(word, available):
    """
    takes a word and a string of letters, and that returns True if the word
    contains only letters in the list.
    """
    for letter in word:
      if letter not in available:
        return False
    return True


# print(uses_only('Babson', 'aBbsonxyz'))
# print(uses_only('college', 'aBbsonxyz'))


def uses_all(word, required):
    """
    takes a word and a string of required letters, and that returns True if
    the word uses all the required letters at least once.
    """
    for letter in required:
      if letter not in word:
        return False
    return True


# print(uses_all('Babson', 'abs'))
# print(uses_all('college', 'abs'))


def is_abecedarian(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    before = ord(word[0])
    for letter in word.lower():
      if ord(letter) < before:
        return False
      before = ord(letter)
    return True

# print(is_abecedarian('abs'))
# print(is_abecedarian('college'))

#Exercise 2
"""Rewrite is_abecedarian using recursion"""
def is_abecedarian1(word):
  if len(word) == 1:
    return True
  elif ord(word[1]) < ord(word[0]):
    return False
  else:
    return is_abecedarian1(word[1:])

# print(is_abecedarian1('abs'))
# print(is_abecedarian1('college'))

"""Rewrite is_abecedarian using while loop."""
def is_abecedarian2(word):
  while len(word) > 1:
    if ord(word[1]) < ord(word[0]):
      return False
    word = word[1:]
  return True

# print(is_abecedarian1('abs'))
# print(is_abecedarian1('college'))