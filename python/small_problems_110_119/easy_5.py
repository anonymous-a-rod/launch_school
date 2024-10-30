print("Inverting Dictionary")

def invert_dict(d):
    # inverted = {}
    # for key, value in d.items():
    #     inverted[value] = key
    # return inverted
    return {v: k for k, v in d.items()}

print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }) == {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })  # True

print("Retain Specific Keys")

def keep_keys(input_dict, keys):
    return {k: v for k, v in input_dict.items() if k in keys}

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True

print("Delete Vowels")

import re

def remove_vowels(a):
    # for i, s in enumerate(a):
    #     a[i] = re.sub(r"[aeiouAEIOU]", '', s)
    # return a
    return [re.sub(r"[aeiouAEIOU]", '', s) for s in a]


# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True

print("How Long Are You?")

def word_lengths(words=''):
    if not words: return []
    return [f"{word} {len(word)}" for word in words.split(' ')]



# All of these examples should print True
words = 'cow sheep chicken'
expected_result = ['cow 3', 'sheep 5', 'chicken 7']
print(word_lengths(words) == expected_result)        # True

words = 'baseball hot dogs and apple pie'
expected_result = ['baseball 8', 'hot 3', 'dogs 4',
                   'and 3', 'apple 5', 'pie 3']
print(word_lengths(words) == expected_result)        # True

words = "It ain't easy, is it?"
expected_result = ['It 2', "ain't 5", 'easy, 5',
                   'is 2', 'it? 3']
print(word_lengths(words) == expected_result)        # True

big_word = 'Supercalifragilisticexpialidocious'
print(word_lengths(big_word) == [f'{big_word} 34'])  # True

print(word_lengths('') == [])                        # True
print(word_lengths() == [])                          # True


print("List Element Multiplication")

def multiply_items(a, b):
    return [a * b for a, b in zip(a, b)]

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True


print("Sum of Sums")

def sum_of_sums(digits):
    total = 0
    cum_sum = 0
    for digit in digits:
        cum_sum += digit
        total += cum_sum
    return total


print(sum_of_sums([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)                      # True

print("Sum of Digits")

def sum_digits(digit):
    sum = 0
    while digit:
        digit, mod = divmod(digit, 10)
        sum += mod
    return sum

print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True

print("Staggered Case (Part 1)")
print("Staggered Case (Part 2)")

def staggered_case(s):
    staggered_case = ''
    for index, letter in enumerate(s):
        if not letter.isalpha():
            staggered_case += letter
        elif index % 2 == 0:
            staggered_case += letter.upper()
        else:
            staggered_case += letter.lower()
    return staggered_case

string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True



print("Remove Consecutive Duplicates")

def unique_sequence(sequence):
    unique_sequence = []
    for digit in sequence:
        if not unique_sequence or unique_sequence[-1] != digit:
            unique_sequence.append(digit)
    return unique_sequence

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True