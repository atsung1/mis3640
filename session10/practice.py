def nested_sum(t):
    """Computes the total of all numbers in a list of lists.
    t: list of list of numbers
    returns: number
    Expected output:
    >>> t = [[1, 2], [3], [4, 5, 6]]
    >>> nested_sum(t)
    21
    """
    # #mine
    # sum = 0
    # for x in range(len(t)):
    #     if len(t[x]) > 1:
    #         for y in range(len(t[x])):
    #             sum += t[x][y]
    #     else:
    #         sum += t[x][0]
    # return sum

    sum = 0
    for x in t:
        sum += sum(x)
    return sum

# t = [[1, 2], [3], [4, 5, 6]]
# print(nested_sum(t))


def cumsum(t):
    """Computes the cumulative sum of the numbers in t.
    t: list of numbers
    returns: list of numbers
    Expected output:
    >>> t = [1, 2, 3]
    >>> cumsum(t)
    [1, 3, 6]
    """
    new = []
    total = 0
    for i in t:
        total += i
        new.append(total)
    return new

# t = [1, 2, 3]
# cumsum(t)

def middle(t):
    """Returns all but the first and last elements of t.
    t: list
    returns: new list
    Expected output:
    >>> t = [1, 2, 3, 4]
    >>> middle(t)
    [2, 3]
    """
    return t[1:-1]

# t = [1, 2, 3, 4]
# print(middle(t))

def chop(t):
    """Removes the first and last elements of t.
    t: list
    returns: None
    Expected output:
    >>> t = [1, 2, 3, 4]
    >>> chop(t)
    >>> t
    [2, 3]
    """
    t.pop()
    t.pop(0)

# t = [1, 2, 3, 4]
# chop(t)
# print(t)

def is_sorted(t):
    """Checks whether a list is sorted.
    t: list
    returns: boolean
    Expected output:
    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted(['b', 'a'])
    False
    """
    return t == sorted(t)
    # for i in range(len(t)-1):
    #     if t[i] > t[i+1]:
    #         return False
    # return True

# print(
# is_sorted([1, 2, 2]), 
# is_sorted(['b', 'a']))

def is_anagram(word1, word2):
    """Checks whether two words are anagrams
    Two words are anagrams if you can rearrange the letters from one to 
    spell the other.
    word1: string or list
    word2: string or list
    returns: boolean
    Expected output:
    >>> is_anagram('stop', 'pots')
    True
    >>> is_anagram('different', 'letters')
    False
    >>> is_anagram([1, 2, 2], [2, 1, 2])
    True
    """
    return sorted(word1) == sorted(word2)


def has_duplicates(s):
    """Returns True if any element appears more than once in a sequence.
    s: string or list
    returns: bool
    output:
    >>> print(has_duplicates('cba'))
    False
    >>> print(has_duplicates('abba'))
    True
    """
    # new = sorted(s)
    # for i in range(1, len(new)):
    #     if new[i] == new[i-1]:
    #         return True
    # return False
    for i in s:
        if s.count(i) > 1:
            return True
    return False


def has_adjacent_duplicates(s):
    """Returns True if there are two same adjacent elements.
    s: string or list
    returns: bool
    output:
    >>> print(has_adjacent_duplicates('cba'))
    False
    >>> print(has_adjacent_duplicates('abca'))
    Flase
    >>> print(has_adjacent_duplicates('abbc'))
    True
    """
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            return True
    return False


def main():
    t = [[1, 2], [3], [4, 5, 6]]
    # print(nested_sum(t))

    # t = [1, 2, 3]
    # print(cumsum(t))

    # t = [1, 2, 3, 4]
    # print(middle(t))
    # chop(t)
    # print(t)

    # print(is_sorted([1, 2, 2]))
    # print(is_sorted(['b', 'a']))

    # print(is_anagram('stop', 'pots'))
    # print(is_anagram('different', 'letters'))
    # print(is_anagram([1, 2, 2], [2, 1, 2]))

    # print(has_duplicates('cba'))
    # print(has_duplicates('abba'))

    print(has_adjacent_duplicates('cba'))
    print(has_adjacent_duplicates('abca'))
    print(has_adjacent_duplicates('abbc'))


if __name__ == '__main__':
    main()