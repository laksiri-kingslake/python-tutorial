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

# Enumerate
for letter in letters:
    print(letter)

for letter in enumerate(letters):
    print(letter) # returns a tuple

for index, letter in enumerate(letters):
    print(index, letter)