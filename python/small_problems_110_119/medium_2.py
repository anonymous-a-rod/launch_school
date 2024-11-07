print('Lettercase Percentage Ratio')

def letter_percentages(string):
  lower = 0
  upper = 0
  neither = 0
  total = len(string)

  for c in string:
    if c.islower():
      lower += 1
    elif c.isupper():
      upper += 1
    else:
      neither += 1

  expected_result = {
    'lowercase': f"{lower*100/total:.2f}",
    'uppercase': f"{upper*100/total:.2f}",
    'neither': f"{neither*100/total:.2f}",
    }

  return expected_result

expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)


# print('Triangle Sides')

# def valid_triangle(a, b, c):
#   if a <= 0 or b <= 0 or c <= 0: return False
#   if a + b <= c or b + c <= a or c + a <= b: return False
#   return True

# def triangle(a, b, c):
#   if not valid_triangle(a, b, c): return 'invalid'
#   if a == b == c: return "equilateral"
#   if len(set({a, b, c})) == 2: return "isosceles"
#   return "scalene"


# print(triangle(3, 3, 3) == "equilateral")  # True
# print(triangle(3, 3, 1.5) == "isosceles")  # True
# print(triangle(3, 4, 5) == "scalene")      # True
# print(triangle(0, 3, 3) == "invalid")      # True
# print(triangle(3, 1, 1) == "invalid")      # True

print('Tri-Angles')

def triangle(a, b, c):
  # if a + b + c != 180: return 'invalid'
  # if a <= 0 or b <= 0 or c <= 0: return 'invalid'
  # if a > 90 or b > 90 or c > 90: return 'obtuse'
  # if a == 90 or b == 90 or c == 90: return 'right'
  # return 'acute'

  angles = (a, b, c)
  if any(angle <= 0 for angle in angles) or sum(angles) != 180: return 'invalid'
  if any(angle > 90 for angle in angles): return 'obtuse'
  if any(angle == 90 for angle in angles): return 'right'
  return 'acute'

print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True


print("Unlucky Days")

from datetime import date

def friday_the_13ths(year):
  fridays = 0
  for month in range(1, 13):
    if date(year, month, 13).weekday() == 4:
      fridays += 1
  return fridays

print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True


print('Next Featured Number Higher than a Given Value')

from math import ceil

def unique_digits(n):
  return len(str(n)) == len(set(str(n)))

def next_featured(n):
  n = ceil((n + 1) / 7) * 7
  while (n % 2 == 0 or not unique_digits(n)) and n <= 9876543201:
    n += 7
  if n > 9876543201: return "There is no possible number that fulfills those requirements."
  return n

print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that fulfills those requirements.")
print(next_featured(9876543201) == error)       # True


print('Sum Square - Square Sum')

def sum_square_difference(n):
  return sum(range(n + 1))**2 - sum([x**2 for x in range(n + 1)])


print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True

print('Bubble Sort')

def bubble_sort(lst):
  swaps = True
  n = len(lst)

  while swaps:
    for i in range(n):
      if i == 0: swaps = False
      if i == n - 1: continue
      if lst[i] > lst[i + 1]:
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
        swaps = True

lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True