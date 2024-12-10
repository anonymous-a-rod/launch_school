# Square Numbers

def squared(n):
  return n**2

numbers = [1, 2, 3, 4, 5]

squared_numbers = map(squared, numbers)

print(list(squared_numbers))

# Even Numbers

even = lambda n : n % 2 == 0

even_numbers = filter(even, numbers)

print(list(even_numbers))

# Product of Numbers

from functools import reduce

multiply = lambda a, b : a * b

product = reduce(multiply, numbers)

print(product)

# Lengths of Strings

num_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

lengths = list(map(len, num_words))

print(lengths)

# Remove None Values

values = [1, None, 'string', True, False]

not_none = lambda x : x is not None

non_none_values = list(filter(not_none, values))

print(non_none_values)

# Concatenate Strings

concatenate_strings = lambda a, b : a + b

print(reduce(concatenate_strings, num_words))

# Nested Generator Expressions

nested_lists = [[1, 2], ['a', 'b', ['kanga', ['roo']]], 'hello']

def flatten(lst):
  new_list = []
  for item in lst:
    if isinstance(item, list):
      new_list.extend(flatten(item))
    else:
      new_list.append(item)
  return new_list

print(flatten(nested_lists))

# List of lists (nested list)
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flattened_list = (item for sublist in nested_list for item in sublist)

print(list(flattened_list))

# Reverse String

text = 'hello'

reversed_text = ''.join((char for char in reversed(text)))

# Basic Generator Function

nums = list(n for n in range(1, 6))

print(nums)

# Generator with User Input

def get_user_input():
  while True:
    user_input = input('User input: ')
    if user_input == 'stop':
      break
    yield user_input

print(list(get_user_input()))