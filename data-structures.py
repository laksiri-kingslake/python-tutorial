letters = ['a','b','c','d']
matrix=[[0,1],[2,3]]
zeros=[0]*5
combined=zeros+letters
numbers=list(range(20)) # iterable
chars=list("Hello World")  #string is a iterable

# print(chars)
# print(numbers)
# print(combined)
# print(matrix)
# print(letters[0])
# print(letters[-1])
# print(letters[0:3])
# print(letters[:3])

letters[0] = "A"
# print(letters)

# print(letters[::2]) # every second element
# print(letters[::-1]) # reverse the list
# print(letters[::-2]) # reverse the list and every second element

# Unpacking lists
new_numbers = [1,2,3,4,5]
first, second, *other = new_numbers
# print(first)
# print(second)
# print(other)

# Loop over list
# for letter in letters:
    # print(letter)

# for letter in enumerate(letters):
    # print(letter) # letter is a tuple

# for index, letter in enumerate(letters):
    # print(index, letter)

# Add or remove elements
letters.append('e') # add to the end
letters.insert(0, "-") # add to the given index
letters.pop() # remove the last element
letters.pop(0) # remove the element at the given index
letters.remove('b') # remove the first appearance of the given element
del letters[0:3] # remove the elements in the given range
letters.clear() # remove all elements
# print(letters)

# Find elements
# letters = ['a','b','c','d']
# print(letters.index('a')) # find the index of the given element
# if 'e' in letters:
#     print(letters.index('e')) # find the index of the given element
# else:
#     print('Not found')
# print('d' in letters) # check if the given element is in the list
# print('x' in letters) # check if the given element is in the list
# print(letters.count('d')) # count the number of the given element

# Sort lists
# numbers = [3,51,2,8,6]
# numbers.sort() # sort the list
# numbers.sort(reverse=True) # sort the list in reverse
# print(numbers)
# print(sorted(numbers)) # return a new sorted list
# print(numbers)
# print(numbers[::-1]) # reverse the list
# print(numbers)
# numbers.reverse() # reverse the list
# print(numbers)

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

# def sort_item(item):
#     return item[1]

# items.sort(key=sort_item) # sort the list
# items.sort(key=lambda item:item[1]) # sort the list - lambda function
# print(items)

# prices = []
# for item in items:
#     prices.append(item[1])

# print(prices)

# map function
prices = list(map(lambda item: item[1], items)) # map function
print(prices)