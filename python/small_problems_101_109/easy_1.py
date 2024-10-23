def odd(num):
    return abs(num) % 2 == 1

print(odd(2))
print(odd(3))
print(odd(34))

for i in range (1, 100, 2):
    print(i)

for i in range (2, 99, 2):
    print(i)

SQM_TO_SQFT = 10.7639

def area(length, width):
    sqm = length * width
    sqft = sqm * SQM_TO_SQFT
    print(f"The room is {sqm} square meters and {sqft} sqaure feet")

area(1, 1)

# bill = int(input('What is the bill? '))
# tip_percent = int(input('What is the tip percentage? '))
# tip = bill * (tip_percent / 100)

# print(f'The tip is ${tip:.2f}')
# print(f'The bill is ${bill:.2f}')

# number = int(input('Please enter an integer greater than 0: '))
# option = input('Enter "s" to compute the sum, or "p" to compute the product. s: ')

# if option == 's':
#     sum = 0
#     for i in range(1, number + 1):
#         sum += i
#     print(f"The sum of the integers between 1 and {number} is {sum}.")
# if option == 'p':
#     product = 1
#     for i in range(1, number + 1):
#         product *= i
#     print(f"The product of the integers between 1 and {number} is {product}.")


def short_long_short(a, b):
    return a + b + a if len(a) < len(b) else b + a + b
        

print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# These examples should all print True
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == False)
print(is_leap_year(1100) == False)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == False)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)


def is_leap_year(year):
    if year < 1752:
        return year % 4 == 0
    elif year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return year % 4 == 0
    
# These examples should all print True
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == True)
print(is_leap_year(1100) == True)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == True)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)

def multisum(num):
    sum = 0
    for i in range(num+1):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

# These examples should all print True
print('multisum')
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)

def utf16_value(string):
    # value = 0
    # for char in string:
    #     value += ord(char)
    # return value
    return sum(ord(char) for char in string)

# These examples should all print True
print(utf16_value('Four score') == 984)
print(utf16_value('Launch School') == 1251)
print(utf16_value('a') == 97)
print(utf16_value('') == 0)

# The next three lines demonstrate that the code
# works with non-ASCII characters from the UTF-16
# character set.
OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
print(utf16_value(OMEGA) == 937)
print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)