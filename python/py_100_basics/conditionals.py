from random import randint
random_number = randint(0, 1)

if random_number == 0:
    print(False)
else:
    print(True)

print(False) if random_number == 0 else print(True)
print(False if random_number == 0 else True)

print(bool(random_number))

weather = 'sunny'

if weather == 'sunny':
    print("It's a beautiful day!")
elif weather == 'rainy':
    print('Grab your umbrella.')
else:
    print('unknown weather forecast')

word = 'something'

match word:
    case 'turd':
        print('smells foul')
    case 'something':
        print('bingo')
    case _:
        print('other')

match weather:
    case 'sunny':
        print("It's a beautiful day!")
    case 'rainy':
        print('Grab your umbrella.')
    case _:
        print('unknown weather forecast')