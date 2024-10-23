def repeat(s, n):
    for _ in range(n):
        print(s)

repeat('Hello', 3)

def crunch(s):
    crunched = ''
    for c in s:
        if not crunched.endswith(c):
            crunched += c
    return crunched

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')


def print_in_box(s):
    inner_width = len(s) + 2
    print(f"+{'-' * inner_width}+")
    print(f"|{' ' * inner_width}|")
    print(f"| {s} |")
    print(f"|{' ' * inner_width}|")
    print(f"+{'-' * inner_width}+")

print_in_box('To boldly go where no one has gone before.')
print_in_box('')

def stringy(n):
    s = ''
    for i in range(n):
        if i % 2 == 0:
            s += '1'
        else:
            s += '0'
    return s

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True


def triangle(n):
    for stars in range (1, n + 1):
        spaces = n - stars
        print(f"{spaces * ' '}{stars * '*'}")

triangle(5)
triangle(9)

# noun = input('Enter a noun: ')
# verb = input('Enter a verb: ')
# adjective = input('Enter an adjective: ')
# adverb = input('Enter an adverb: ')

# print(f"""
# Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!
# The {adjective} {noun} {verb}s {adverb} over the lazy {noun}.
# The {noun} {adverb} {verb}s up to Joe's {adjective} turtle.
# """)

def twice(n):
    s = str(n)
    length = len(s)
    half = length // 2

    if length % 2 != 0 or s[:half] != s[half:]:
        return n * 2
    else:
        return n

print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True

import statistics

def get_grade(*args):
    avg = statistics.mean(args)
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True

def clean_up(s):
    result = ''
    for c in s:
        if c.isalpha():
            result += c
        elif not result.endswith(' '):
            result += ' '
    return result

print(clean_up("---what's my +*& line?") == " what s my line ")
# True

def century(year):
    century = ((year - 1) // 100) + 1
    s = str(century)
    last = s[-1]

    if (len(s) >= 2) and (s[-2:] == '11' or s[-2:] == '12' or s[-2:] == '13'):
        return f"{century}th"
    elif last == '1':
        return f"{century}st"
    elif last == '2':
        return f"{century}nd"
    elif last == '3':
        return f"{century}rd"
    else:
        return f"{century}th"

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True
print(century(12201) == "123rd")        # True
