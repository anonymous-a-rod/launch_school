words = "These aren't the droids you're looking for."

print(len(words))

print(words.upper())

def same_word(first, second):
    # also casefold()
    return first.lower() == second.lower()

name = 'Roger'
name_2 = 'RoGeR'
name_3 = 'Dave'

print(same_word(name, name_2))
print(same_word(name_3, name_2))

print("ß".casefold())
print("ß".lower())
print("SS".casefold())
print("SS".lower())

char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'

print('x' in char_sequence)

def is_empty(s):
    return not s
    # return bool(len(text))

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True

def is_empty_or_blank(s):
    return not s.strip()

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True

# .title()
s = 'launch school tech & talk'
new_s = ''
words = s.split()
for index, word in enumerate(words):
    new_s += word.capitalize()
    if index < len(words) - 1:
        new_s += ' '

print(new_s)

# def starts_with(word, start):
#     return word[:len(start)] == start

def starts_with(word, start):
    return word.startswith(start)

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True

def count_substrings(s, sub):
    return s.count(sub)

print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA", "la")) # 2
print(count_substrings("launch", "uno")) # 0