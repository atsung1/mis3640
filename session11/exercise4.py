def binary_search(my_list, x):
    '''
    this function adopts bisection/binary search to find the index of a given
    number in an ordered list
    my_list: an ordered list of numbers from smallest to largest
    x: a number
    returns the index of x if x is in my_list, None if not.
    '''
    start = 0
    end = len(my_list)-1
    midpoint = int((start+end)/2)
    if x not in my_list:
        return None
    while my_list[midpoint] != x:
        if my_list[midpoint] > x:
            end = midpoint - 1
        elif my_list[midpoint] < x:
            start = midpoint + 1
        midpoint = int((start + end)/2)
    return midpoint



test_list = [1, 3, 5, 235425423, 23, 6, 0, -23, 6434]
test_list.sort()

print(binary_search(test_list, -23))
print(binary_search(test_list, 0))
print(binary_search(test_list, 235425423))
print(binary_search(test_list, 30))

# expected output
# 0
# 1
# 8
# None