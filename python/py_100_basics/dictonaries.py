car = {
    'type': 'sedan',
    'color': 'blue',
    'milage': 80_000
}

car['year'] = 2003
del car['milage']

print(car['color'])
print(len(car))
print(car)

student = {
    'id': 123,
    'grade': 'B',
}

print('name' in student and 'grade' in student)
print('name' in student)
print('grade' in student)

truck = {
    'type': 'pickup',
    'color': 'red',
    'year': 1998
}

vehicles = {
    'car': car,
    'truck': truck
}

print(vehicles)

vehicles['car'] = list(vehicles['car'])

print(vehicles)

numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}

nums = []
for n in numbers.values():
    nums.append(n // 2)

print(nums)

for key, value in numbers.items():
    print(f"A {key} number is {value}.")