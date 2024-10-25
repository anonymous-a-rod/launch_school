# numbers = []

# for count in ['first', 'second', 'third', 'fourth', 'fifth', 'last']:
#     numbers.append(input(f"Enter the {count} number: "))

# print(f"{numbers[-1]} is {'' if numbers[-1] in numbers[:-1] else 'not '}in {','.join(numbers[:-1])}.")

# All of these examples should print True

# def is_palindrome(s):
#     return s == s[::-1]

# print(is_palindrome('madam') == True)
# print(is_palindrome('356653') == True)
# print(is_palindrome('356635') == False)

# # case matters
# print(is_palindrome('Madam') == False)

# # all characters matter
# print(is_palindrome("madam i'm adam") == False)

def is_real_palindrome(s):
    char_list = [x.casefold() for x in list(s) if x.isalpha() or x.isnumeric()]
    return char_list == char_list[::-1]

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True

print("running totals")

# def running_total(totals):
#     running_totals = []
#     for i in range(len(totals)):
#         running_totals.append(sum(totals[:i + 1]))
#     return running_totals

def running_total(totals):
    running_total = []
    current_total = 0

    for i in range(len(totals)):
        current_total += totals[i]
        running_total.append(current_total)
    return running_total

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20]) == [14, 25, 32, 47, 67])  # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True

print("Letter Counter (Part 1)")

def word_sizes(s):
    counts = {}
    l = s.split()
    for word in l:
        length = len(word)
        if length in counts:
            counts[length] += 1 
        else:
            counts[length] = 1
    return counts


# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})

print("Letter Counter (Part 2)")


# All of these examples should print True

def word_sizes(s):
    counts = {}
    l = s.split()
    for word in l:
        length = len([char for char in word if char.isalpha()])
        if length in counts:
            counts[length] += 1 
        else:
            counts[length] = 1
    return counts

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})

print('letter swap')

def swap(s):
    reverse = ''
    for word in s.split(' '):
        if len(word) == 1:
            reverse += f"{word} "
        elif len(word) > 1:
            reverse += f"{word[-1]}{word[1:-1]}{word[0]} "
    return reverse.strip()

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True


print('Convert a String to a Number')

# could also use ord(char) - ord('0') or 48 to get the digit value

def string_to_integer(s):
    nums = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    number = 0
    l = len(s)
    for i, n in enumerate(s):
        base = 10 ** (l - i - 1)
        number += nums[n] * base
    return number

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True

def string_to_signed_integer(s):
    if s[0] == '-': return string_to_integer(s[1:]) * -1
    if s[0] == '+': return string_to_integer(s[1:])
    return string_to_integer(s)

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True

print("Convert a Number to a String")

def integer_to_string(n):
    s = ''
    if n == 0:
        return '0'
    while n > 0:
        digit = n % 10
        char = chr(digit + 48)
        s = char + s
        n = n // 10
    return s

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True

def signed_integer_to_string(n):
    if n < 0: return '-' + integer_to_string(n * -1)
    if n > 0: return '+' + integer_to_string(n)
    return integer_to_string(n)

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True
