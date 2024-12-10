# Default to a Period

def greet(name, greeting, punctuation='.'):
  return f"{greeting}, {name}{punctuation}"

print(greet("Antonina", "Hello")) # Hello, Antonina.
print(greet("Pete", "Good morning", "!")) # Good Morning, Pete!

# Create User

def create_user(name, *, email, age):
  return { 'username': name, 'email': email, 'age': age }

print(create_user("Srdjan", email="srdjan@example.com", age=39))
# {"username": "Srdjan", "email": "srdjan@example.com", "age": 39}
# print(create_user("Srdjan", "srdjan@example.com", age=39))
# Raises an exception

# Build Profile

def build_profile(first, last, **kwargs):
  profile =  { 'first_name': first, 'last_name': last }
  profile.update(kwargs)
  return profile


print(build_profile("Max", "Hawkins", location="San Francisco", field="Software Engineering"))
# {'first_name': 'Max', 'last_name': 'Hawkins', 'location': 'San Francisco', 'field': 'Software Engineering'}

# Concatenate any Number of Strings

def concatenate(*args):
  return ' '.join(args)

print(concatenate("Launch", "School", "is", "great")) # Launch School is great
print(concatenate("I", "am", "working", "on", "the", "PY130", "course")) # I am working on the PY130 course

# Display Info

def display_info(data, *, reverse=False, uppercase=False):
  if reverse:
    data = data[::-1]
  if uppercase:
    data = data.upper()
  return data

print(display_info("Launch", reverse=True)) # hcnuaL
print(display_info("School", uppercase=True)) # SCHOOL
print(display_info("cat", uppercase=True, reverse=True)) # TAC

# Unpack a List

lst = [10, 20, 30, 40]
a, b, c, d = lst

print(a, b, c, d)