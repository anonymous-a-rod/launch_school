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