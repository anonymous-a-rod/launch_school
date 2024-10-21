name = "Victor"
profession = "programmer"

greeting = "Hello, {}. You are a {}"

print(greeting.format(name, profession))

greeting = f"Hello, {name}. You are a {profession}"

print(greeting)

ice_cream_density = 10

while ice_cream_density > 0:
    print('Drip...')
    ice_cream_density -= 1

print('The ice cream melted.')

print(4 * 5 + 3**2 / 10)

from datetime import datetime

print(datetime.now())

from datetime import date

today = date.today()

today_year = today.year
iso_year = today.isocalendar()[0]

print(today_year)
print(iso_year)
print(today.isocalendar())

print(' '.join(['the', 'person', 'is', 'learning']))

speed_limit = 60
current_speed = 80

if current_speed > speed_limit:
    print('"People are so bad at driving cars that '
          "computers don\'t have to be that good to be "
          'much better." -- Marc Andreessen')