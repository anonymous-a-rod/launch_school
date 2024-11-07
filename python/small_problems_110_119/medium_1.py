print("rotation part 1")

# All of these examples should print True

def rotate_list(og_list):
    if not isinstance(og_list, list): return None
    return og_list[1:] + og_list[:1]

print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])

print("part 2")

def rotate_rightmost_digits(digit, count):
    if count <= 1: return digit
    str_digit = str(digit)
    fixed_front = str_digit[0:-count]
    rotated_part = str_digit[-count + 1:] + str_digit[-count]
    return int(fixed_front + rotated_part)

print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True

print("part 3")

def max_rotation(digit):
    for i in range(len(str(digit)), 0, -1):
        digit = rotate_rightmost_digits(digit, i)
    return digit

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True

print('Stack Machine Interpretation')

def minilang(text):
    stack = []
    register = 0

    for token in text.split(' '):
        if token.lstrip('-').isdigit():
            register = int(token)
            continue

        match token:
            case 'PRINT':
                print(register)
            case 'PUSH':
                stack.append(register)
            case 'POP':
                register = stack.pop()
            case 'ADD':
                register += stack.pop()
            case 'SUB':
                register -= stack.pop()
            case 'MULT':
                register *= stack.pop()
            case 'DIV':
                register //= stack.pop()
            case 'REMAINDER':
                register %= stack.pop()

minilang('PRINT')
# 0

minilang('5 PUSH 3 MULT PRINT')
# 15

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# 5
# 3
# 8

minilang('5 PUSH POP PRINT')
# 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# 5
# 10
# 4
# 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12

minilang('-3 PUSH 5 SUB PRINT')
# 8

minilang('6 PUSH')
# (nothing is printed)

print("Word to Digit")

def word_to_digit(string):
    string = string.replace('zero', '0')
    string = string.replace('one', '1')
    string = string.replace('two', '2')
    string = string.replace('three', '3')
    string = string.replace('four', '4')
    string = string.replace('five', '5')
    string = string.replace('six', '6')
    string = string.replace('seven', '7')
    string = string.replace('eight', '8')
    string = string.replace('nine', '9')
    return string


message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True


print("Is It Prime?")

def is_prime(digit):
    if digit < 2: return False
    for i in range(2, int(digit**0.5) + 1):
        if digit % i == 0: return False
    return True


print(is_prime(1) == False)              # True
print(is_prime(2) == True)               # True
print(is_prime(3) == True)               # True
print(is_prime(4) == False)              # True
print(is_prime(5) == True)               # True
print(is_prime(6) == False)              # True
print(is_prime(7) == True)               # True
print(is_prime(8) == False)              # True
print(is_prime(9) == False)              # True
print(is_prime(10) == False)             # True
print(is_prime(23) == True)              # True
print(is_prime(24) == False)             # True
print(is_prime(997) == True)             # True
print(is_prime(998) == False)            # True
print(is_prime(3_297_061) == True)       # True
print(is_prime(23_297_061) == False)     # True

print('Fibonacci Numbers (Procedural)')

fibonaccis = { 1: 1, 2: 1 }

def fibonacci(x):
    if x in fibonaccis: return fibonaccis[x]
    fibonaccis[x] = fibonacci(x - 1) + fibonacci(x - 2)
    return fibonaccis[x]

print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True

# def find_fibonacci_index_by_length(n):
#     index = 1
#     fib_val = 1
#     while fib_val <= n:
#         fibonacci(x)

# # All of these examples should print True
# # The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
# print(find_fibonacci_index_by_length(2) == 7)
# print(find_fibonacci_index_by_length(3) == 12)
# print(find_fibonacci_index_by_length(10) == 45)
# print(find_fibonacci_index_by_length(16) == 74)
# print(find_fibonacci_index_by_length(100) == 476)
# print(find_fibonacci_index_by_length(1000) == 4782)

# # Next example might take a little while on older systems
# print(find_fibonacci_index_by_length(10000) == 47847)
