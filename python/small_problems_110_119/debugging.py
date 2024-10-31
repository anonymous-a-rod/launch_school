print("Countdown")

def decrease(counter):
    return counter - 1

counter = 10

for _ in range(10):
    print(counter)
    counter = decrease(counter)

print('LAUNCH!')

print("Reverse a String")

def reverse_string(string):
    new_string = ''
    for char in string:
        new_string = char + new_string

    return new_string

print(reverse_string("hello") == "olleh")

print("Multiply List")

def multiply_list(lst):
    return [item * 2 for item in lst]

print(multiply_list([1, 2, 3]) == [2, 4, 6])

print("Key Check")

def get_key_value(my_dict, key):
    if my_dict.get(key):
        return my_dict[key]
    else:
        return None

print(get_key_value({"a": 1}, "b"))

print("Calendar Event Checker")


events = {
    "2023-08-13": ["Python debugging exercises"],
    "2023-08-14": ["Read 'Automate the Boring Stuff'"],
    "2023-08-15": ["Webinar: Python for Data Science"],
}

def is_date_available(date):
    if date not in events:
        return True

    return False

print(is_date_available("2023-08-14"))  # should return False
print(is_date_available("2023-08-16"))  # should return True

print("Mutable Default Arguments")

# Mutable default argument example
def add_to_list(item, my_list=[]):
    my_list.append(item)
    return my_list

print(add_to_list(1))  # Expected: [1]
print(add_to_list(2))  # Expected: [2] but actually returns [1, 2] 😱

# Safe List Addition: Avoid Mutable Default Trap
def add_to_list(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

print(add_to_list(1))  # [1]
print(add_to_list(2))  # [2] as expected!

print("Shadow")

def multiply_sum(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(multiply_sum(numbers, 2) == 20)

print("copy issues")

import copy

original = [[1], [2], [3]]
copied = copy.deepcopy(original)

original[0][0] = 99

print(copied[0] == [1])

print("Set Modifications")

data_set = {1, 2, 3, 4, 5}

data_set = {item for item in data_set if item % 2 == 0}
# for item in data_set: or iterate over data_set.copy()
#     if item % 2 == 0:
#         data_set.remove(item)
print(data_set)

print("List Deduplication")

data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
# unique_data = list(set(data))
seen = set()
unique_data = [item for item in data if not (item in seen or seen.add(item))]
print(unique_data)
print(unique_data == [4, 2, 1, 3]) # order not guaranteed