def multiply(x, y):
    return x * y

print(multiply(12, 4))

def bruce_eckel_quote():
    print('Python is executable pseudocode.')

bruce_eckel_quote()

def cite(author, quote):
    print(f"{author}: {quote}")

cite('Bruce Eckel', 'Python is executable pseudocode.')

def squared_number(n):
    return n**2

print(squared_number(3))

def multiples_of_three():
    divisor = 1

    for dividend in range(3, 31, 3):
        print(f'{dividend} / {divisor} = 3')
        divisor += 1

multiples_of_three()

def compare_by_length(a, b):
    len_a = len(a)
    len_b = len(b)

    if len_a < len_b:
        return -1
    if len_a == len_b:
        return 0
    else:
        return 1

print(compare_by_length('patience', 'perseverance')) # -1
print(compare_by_length('strength', 'dignity'))     #  1
print(compare_by_length('humor', 'grace'))           #  0

words = 'Captain Ruby'

new_words = words.replace('Ruby', 'Python')

print(words)
print(new_words)

def greet(code, region=''):
    match code:
        case 'en':
            match region:
                case 'US':
                    return 'Hey!'
                case 'GB':
                    return 'Hello!'
                case 'AU':
                    return 'Howdy!'
                case _:
                    return 'Hi!'
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Olá!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af':
            return 'Haai!'
        case _:
            return 'unknown language code'

print(greet('en'))         # Hi!
print(greet('fr'))         # Salut!
print(greet('pt'))         # Olá!
print(greet('de'))         # Hallo!
print(greet('sv'))         # Hej!
print(greet('af'))         # Haai!

def extract_language(locale):
    return locale[:2]

print(extract_language('en_US.UTF-8'))      # en
print(extract_language('en_GB.UTF-8'))      # en
print(extract_language('ko_KR.UTF-16'))     # ko

def extract_region(locale):
    start_index = locale.index('_') + 1
    end_index = locale.index('.')
    return locale[start_index:end_index]

print(extract_region('en_US.UTF-8'))    # US
print(extract_region('en_GB.UTF-8'))    # GB
print(extract_region('ko_KR.UTF-16'))   # KR

def local_greet(locale):
    language = extract_language(locale)
    region = extract_region(locale)
    return greet(language, region)

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!
print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!