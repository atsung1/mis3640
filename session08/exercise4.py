# #exercise 3
# # Split
# x = 'the quick brown fox jumps over the lazy dog'
# new_x = x.split(' ')
# for word in new_x:
#     print(word)

# # Strip
# y = '       ;lakjf.                  '
# new_y = y.strip()
# print(new_y)

# # Replace
# a = 'Hello hello hello hello.'
# new_a = a.replace('h', 'H')
# print(new_a)


groceries = ['bananas', 'rice', 'paprika', 'potato chips']

def receipt(groceries):
    sum = 0
    max_length = len(max(items, key=len)) + 10
    for item in groceries:
        price = 0
        for letter in item:
            price += ord(letter)-96
        print(f'{item} ${price}')
        sum += price
        price_string = '${0:.2f}'.format(price)
        num_of_spaces = max_length - len(item) - len(price_string)
        item_string = item + ' ' * num_of_spaces + price_string
        print(item_string)

    print('-' * max_length)
    total_price_string = '${0:.2f}'.format(total_price)
    num_of_spaces = max_length - len('Total') - len(total_price_string)
    print('Total' + ' ' * num_of_spaces + total_price_string)

receipt(groceries)