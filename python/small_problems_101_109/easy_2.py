def greetings(list, dic):
    name = " ".join(list)
    title = dic['title'] + ' ' + dic['occupation']
    return f"Hello, {name}! Nice to have a {title} around."

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.


# name = input('What is your name?' )
# last_char = name[-1]

# if last_char == '!': # name.endswith('!')
#     print(f"HELLO {name.upper()}! WHY ARE WE YELLING?")
# else:
#     print(f"Hello {name}")

def multiply(x, y):
    return x * y

print(multiply(5, 3) == 15)  # True

def square(n):
    return multiply(n, n)

print(square(5) == 25)   # True
print(square(-8) == 64)  # True

# x = float(input('Enter the first number: '))
# y = float(input('Enter the second number: '))

# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x // y)
# print(x % y)
# print(x ** y)

def penultimate(str):
    list = str.split()
    return list[-2]
# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")

def xor(a, b):
    return bool((not (a and b)) and (a or b))

print('xor')
print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)

def oddities(list):
    # oddities = []
    # for i in range(0, len(list), 2):
    #     oddities.append(list[i])
    # return oddities
    return list[::2]

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True

from random import randint

print(f"Teddy is {randint(20, 100)} years old!")

# from datetime import date

# current_age = int(input('What is your age? '))
# retirement_age = int(input('At what age would you like to retire? '))
# remaining_years = retirement_age - current_age
# current_year = date.today().year
# retirement_year = current_year + remaining_years

# print(f"It's {current_year}. You will retire in {retirement_year}.")
# print(f"You have only {remaining_years} years of work to go!")

def center_of(s):
    length = len(s)
    middle = length // 2
    center = s[middle:middle + 1] if length % 2 == 1 else s[middle - 1:middle + 1]
    return center

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True

def negative(n):
    # return abs(n) * -1
    return -abs(n)

print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True