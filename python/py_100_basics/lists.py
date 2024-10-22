def first(list):
    return list[0]

print(first(['Earth', 'Moon', 'Mars']))  # Earth

def last(list):
    return list[-1]

print(last(['Earth', 'Moon', 'Mars']))  # Mars

energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']
energy.remove('fossil')
energy.append('geothermal')

print(energy)

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = list(alphabet)
print(alphabet)

scores = [96, 47, 113, 89, 100, 102]

good_scores = [score for score in scores if score >= 100]
print(len(good_scores))

vocabulary = [
    ['happy', 'cheerful', 'merry', 'glad'],
    ['tired', 'sleepy', 'fatigued', 'drained'],
    ['excited', 'eager', 'enthused', 'animated'],
]

for synonyms in vocabulary:
    for word in synonyms:
        print(word)

# happy
# cheerful
# merry
# glad
# tired
# sleepy
# etc...

list1 = [2, 6, 4]
list2 = [2, 6, 4]

print(list1 == list2)  # true
print(list1 is list2)  # False

some_value1 = [0, 1, 0, 0, 1]
some_value2 = 'I leave you my Kingdom, take good care of it.'

print(type(some_value1) is list)
print(type(some_value2) is list)

isinstance(some_value1, list)  # True
isinstance(some_value2, list)  # False

def contains(city, destinations):
    i = 0
    amount = len(destinations)

    while i < amount:
        if city == destinations[i]:
            return True
        i += 1
    return False 

destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

contains('Barcelona', destinations)  # True
contains('Nashville', destinations)  # False


passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']

# Write some code here.
# Expected output: 11-jZ5-hQ3f*-8!7g3-p3Fs

print("-".join(passcode))

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

for item in list(grocery_list):
    print(item)
    grocery_list.remove(item)
# Your code.

print(grocery_list)

# an empty sequence is also falsey, so you could use while grocery_list and pop(0)