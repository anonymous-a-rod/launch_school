print("Alphabetical Numbers")

num_list = [
        "zero", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]

# Using `sort()` without a key parameter
def alphabetic_number_sort(int_list):
    alpha_numbers_list = [num_list[n] for n in int_list]
    alpha_numbers_list.sort()
    return [num_list.index(n) for n in alpha_numbers_list]

# Using `sorted()` with a key parameter
def alphabetic_number_sort(int_list):
    return sorted(int_list, key=lambda x: num_list[x])

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)
# Prints True


print('Merge Sets')

# def merge_sets(a, b):
#     return set(a + b)

def merge_sets(a, b):
    return set(a) | set(b)

list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]
print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})
# Prints True

print('Immutable Intersection')

def intersection(a, b):
    # intersection = []
    # a.sort()
    # b.sort()
    # merged_sets = merge_sets(a, b)
    # for n in merged_sets:
    #     if n in a and n in b:
    #         intersection += [n]
    # return frozenset(intersection)
    return frozenset(a) & frozenset(b)

list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]
expected_result = frozenset({8})
print(intersection(list1, list2) == expected_result) # True

print('Arrange a Dictionary')

# Given a dictionary, return its keys sorted by the values associated with each key.

def order_by_value(dic):
    return sorted(dic, key=lambda x: dic[x])

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True

print('Unique Elements')

def unique_from_first(a, b):
    # c = set()
    # for n in a:
    #     if n not in b: c.add(n)
    # return c
    return set(a) - set(b)

list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})

print('Leading Substrings')

def leading_substrings(s):
    # substrings = []
    # for i in range(len(s)):
    #     substrings.append(s[:i + 1])
    # return substrings
    return [s[:i + 1] for i in range(len(s))]

# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])

print('All Substrings')

def substrings(s):
    substrings = []
    for i in range(len(s) + 1):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])
    print(substrings)
    return substrings

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True
