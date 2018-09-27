# #exercise 3.1
def price(item):
    price = 0
    item.lower()
    for letter in item:
        price += ord(letter) - 96
    return price

# print(price('bananas'))

# def receipt(groceries):
#     total = 0
#     for item in groceries:
#         total += price(item)
#         print('{} ${}'.format(item, price(item)))
#     print('-'*24)
#     print('Total ${}'.format(total))

# buy = ['bananas', 'rice', 'paprika', 'potato chips']
# receipt(buy)

# #exercise 3.2
# def receipt2(groceries):
#     total = 0
#     for item in groceries:
#         total += price(item)
#         print('{} ${:.2f}'.format(item.ljust(len()), price(item)))
#     print('-'*24)
#     print('Total'.ljust(16), '${:.2f}'.format(total))

# receipt2(buy)

#exercise 3.3
def receipt3(groceries):
    total = 0
    longest=len(groceries[1])
    for item in groceries:
        if len(item) > longest:
            longest = len(item)
    for item in groceries:
        total += price(item)
        print('{} ${:.2f}'.format(item.ljust(longest+5), price(item)))
    print('-'*3*longest)
    print('Total'.ljust(longest+4), '${:.2f}'.format(total))

buy1 = ['apples', 'bananas', 'rice']
receipt3(buy1)