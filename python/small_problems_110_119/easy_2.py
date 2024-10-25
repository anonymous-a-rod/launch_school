print("Cute Angles")

DEGREE = "\u00B0"

def dms(n):
    degrees = int(n)
    degrees_remainder = n % 1
    minutes = int(degrees_remainder * 60)
    minutes_remainder = (degrees_remainder * 60) % 1
    seconds = int(minutes_remainder * 60)

    return f"{degrees}°{minutes:02}'{seconds:02}\""

# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

print('combining lists')

def union(a, b):
    return set(a + b)

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True

print("Halvsies")

from math import ceil

def halvsies(l):
    # instead of ceil I could also add one then do int division (len(l) +1) // 2
    half = ceil(len(l) / 2)
    return [l[:half], l[half:]]

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])

print('Find the Duplicate')

def find_dup(l):
    l.sort()
    for i in range(len(l)):
        if l[i] == l[i + 1]:
            return l[i]

print(find_dup([1, 5, 3, 1]) == 1) # True
print(find_dup([
                  18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
                  38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
                  14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
                  78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
                  89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
                  41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
                  55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
                  85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
                  40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
                   7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
              ]) == 73)       # True

print('Combine Two Lists')

# def interleave(a, b):
#     combined = []
#     for i in range(len(a)):
#         combined += [a[i], b[i]]
#     return combined

def interleave(a, b):
    combined = []
    for i, j in zip(a, b):
        combined += [i, j]
    return combined


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True

print('Multiplicative Average')

def multiplicative_average(l):
    multiple = 1
    for n in l:
        multiple *= n
    return f"{(multiple/len(l)):.3f}"

# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")

print('Multiply Lists')

def multiply_list(a, b):
    # combined = []
    # for i, j in zip(a, b):
    #     combined.append(i * j)
    # return combined
    return [i * j for i, j in zip(a, b)]

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True

print("List of Digits")

def digit_list(digit):
    # list_of_digits = []
    # while digit > 0:
    #     digit, remainder = divmod(digit, 10)
    #     list_of_digits.append(remainder)
    # list_of_digits.reverse()
    # return list_of_digits
    return [int(n) for n in str(digit)]

print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True

print("how many?")

def count_occurrences(vehicles):
    vehicle_count = {}
    for vehicle in vehicles:
        if vehicle in vehicle_count:
            vehicle_count[vehicle] += 1
        else:
            vehicle_count[vehicle] = 1

    for vehicle, count in vehicle_count.items():
        print(f"{vehicle} => {count}")

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)


print("list average")

def average(numbers):
    return sum(numbers) // len(numbers)

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True

