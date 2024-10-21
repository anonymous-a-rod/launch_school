for num in range(0, 11, 2):
    print(num)

for i in range(10, 0, -1):
    print(i)

greeting = 'Aloha!'
for _ in range(3):
    print(greeting)

for i in range(1, 101):
    print(i * 2)

lst = [1, 3, 7, 15]
index = 0

while index < len(lst):
    print(lst[index])
    index += 1

friends = ['Sarah', 'John', 'Hannah', 'Dave']

for friend in friends:
    print(f"Hello, {friend}")

cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
          'Vienna', None, 'London', 'Beijing', None]

for city in cities:
    if city == None:
        continue

    print(len(city))

while True:
    print("and on")
    break

fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']

for fish in fish_list:
    print(fish)
    if fish == 'Nemo':
        break

while True:
    print('Should I stop looping?')
    answer = input()
    if answer == 'yes':
        break