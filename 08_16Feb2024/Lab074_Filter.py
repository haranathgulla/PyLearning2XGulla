# Filter
# It can filter the items from the list based on the logic
# return less number of items

# number = [1, 2, 3, 4, 5, 6,7,8]
# even_numbers = filter(lambda x:x%2 ==0, number)
## even_numbers = filter(lambda num:num%2 ==0, number)
# print(list(even_numbers))


number = [1, 2, 3, 4, 5, 6, 7, 10]
def even(num):
    return num % 2 == 0

even_lamba = lambda num: num % 2 == 0

even_numbers = filter(even, number)
print(list(even_numbers))