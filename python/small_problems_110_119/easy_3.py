print("After Midnight (Part 1)")

def time_of_day(n):
    n %= 1440
    hours, mins = divmod(n, 60)
    return f"{hours:02}:{mins:02}"

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True

print("After Midnight (Part 2)")

def after_midnight(s):
    hours, mins = map(int, s.split(':'))
    # hours = int(s[:2])
    # mins = int(s[3:])
    return (hours * 60 + mins) % 1440

def before_midnight(s):
    return (1440 - after_midnight(s)) % 1440


print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True

print('Double Char (Part 1)')

def repeater(s):
    return ''.join([c * 2 for c in s])

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True

print("Double Char (Part 2)")

def double_consonants(s):
    return ''.join([c if c in 'aeiouAEIOU' or not c.isalpha() else c * 2 for c in s])

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")

print('Reverse Number')

def reverse_number(n):
    # numbers_list = list(str(n))
    # numbers_list.reverse()
    # return int(''.join(numbers_list))
    return int(str(n)[::-1])

print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True

print("Counting Up")

def sequence(n):
    return list(range(1, n + 1))

print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True

print('Name Swapping')

def swap_name(full_name):
    first_name, last_name = full_name.split(' ')
    return f"{last_name}, {first_name}"

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True

print('Sequence Count')

def sequence(times, num):
    # nums = []
    # for i in range(1, times + 1):
    #     nums.append(i * num)
    # return nums
    return [i * num for i in range(1, times + 1)]

print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True


print('Reversed Lists')

def reverse_list(l):
    # copied_l = l.copy()
    # length = len(l)
    # for i in range(length):
    #     l[i] = copied_l[length - i - 1]
    # return l
    left, right = 0, len(l) - 1
    while left < right:
        l[left], l[right] = l[right], l[left]
        left += 1
        right -= 1
    return l

list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])               # True
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True

print('Matching Parenthesis?')

def is_balanced(s):
    # parentheses_only = ''.join([p for p in s if p in '()'])
    # while parentheses_only:
    #     before_length = len(parentheses_only)
    #     parentheses_only = parentheses_only.replace('()', '')
    #     after_length = len(parentheses_only)
    #     if before_length == after_length:
    #         return False
    # return True

    count = 0

    for c in s:
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1

        if count < 0:
            return False

    return count == 0


print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True

