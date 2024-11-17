# class Banner:
#     def __init__(self, message):
#         self._message = message

#     @property
#     def message(self):
#         return self._message

#     def __str__(self):
#         return "\n".join([self._horizontal_rule(),
#                           self._empty_line(),
#                           self._message_line(),
#                           self._empty_line(),
#                           self._horizontal_rule()])

#     def _empty_line(self):
#         return f"| {' ' * len(self.message)} |"

#     def _horizontal_rule(self):
#         return f"+ {'-' * len(self.message)} +"

#     def _message_line(self):
#         return f"| {self.message} |"

# hello = Banner("hello")
# print(hello.__str__())


# print('rectangle')

# class Rectangle():
#     def __init__(self, width, height):
#         self._width = width
#         self._height = height

#     @property
#     def width(self):
#         return self._width
    
#     @property
#     def height(self):
#         return self._height

#     @property
#     def area(self):
#         return self.height * self.width

# rect = Rectangle(4, 5)

# print(rect.width == 4)        # True
# print(rect.height == 5)       # True
# print(rect.area == 20)        # True

# print(rect.width)
# print(rect.height)
# print(rect.area)


# print('square')

# class Square(Rectangle):
#     def __init__(self, side):
#         self._width = side
#         self._height = side

# square = Square(5)
# print(square.area == 25)      # True

# print('Complete the Program - Cats!')

# class Pet:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age

#     @property
#     def name(self):
#         return self._name

#     @property
#     def age(self):
#         return self._age

# class Cat(Pet):
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self._color = color

#     @property
#     def color(self):
#         return self._color

#     @property
#     def info(self):
#         return f'My cat {self.name} is {self.age} years old and has {self.color} fur.'

# cocoa = Cat('Cocoa', 3, 'black')
# cheddar = Cat('Cheddar', 4, 'yellow and white')

# print(cocoa.info)
# print(cheddar.info)


# print('Animals')

# class Animal:
#     def __init__(self, name, age, legs, species, status):
#         self.name = name
#         self.age = age
#         self.legs = legs
#         self.species = species
#         self.status = status

#     def introduce(self):
#         return (f"Hello, my name is {self.name} and I am "
#                 f"{self.age} years old and {self.status}.")

# class Dog(Animal):
#     pass

# class Cat(Animal):
#     def __init__(self, name, age, status):
#         super().__init__(name, age, 4, 'Cat', status)

#     def introduce(self):
#         return super().introduce() + " Meow meow!"
    
# class Dog(Animal):
#     def __init__(self, name, age, status, owner):
#         super().__init__(name, age, 4, 'Dog', status)
#         self._owner = owner

#     @property
#     def owner(self):
#         return self._owner

#     def introduce(self):
#         return super().introduce() + " Woof! Woof!"
    
#     def greet_owner(self):
#         return f"Hi {self.owner}! Woof! Woof!"


# cat = Cat("Pepe", 4, "happy")
# expected = ("Hello, my name is Pepe and I am 4 years old "
#             "and happy. Meow meow!")
# print(cat.introduce() == expected)      # True
# print(cat.introduce())

# dog = Dog("Bobo", 9, "hungry", "Daddy")
# expected = ("Hello, my name is Bobo and I am 9 years old "
#             "and hungry. Woof! Woof!")
# print(dog.introduce() == expected)                  # True
# print(dog.greet_owner() == "Hi Daddy! Woof! Woof!") # True

# class Owner:
#     def __init__(self, name):
#         self.name = name


# class Pet:
#   def __init__(self, species, name):
#     self.species = species
#     self.name = name

#   def __str__(self):
#     return f"a {self.species} named {self.name}"

# class Owner:
#   def __init__(self, name):
#     self.name = name
#     self.pets = []

#   def number_of_pets(self):
#     return len(self.pets)

# class Shelter:
#   def __init__(self):
#     self.owners = set()

#   def adopt(self, owner, pet):
#     owner.pets.append(pet)
#     self.owners.add(owner)

#   def print_adoptions(self):
#     for owner in self.owners:
#       print(f"{owner.name} has adopted the following pets:")
#       for pet in owner.pets:
#         print(pet)
#       print()


# cocoa   = Pet('cat', 'Cocoa')
# cheddar = Pet('cat', 'Cheddar')
# darwin  = Pet('bearded dragon', 'Darwin')
# kennedy = Pet('dog', 'Kennedy')
# sweetie = Pet('parakeet', 'Sweetie Pie')
# molly   = Pet('dog', 'Molly')
# chester = Pet('fish', 'Chester')

# phanson = Owner('P Hanson')
# bholmes = Owner('B Holmes')

# shelter = Shelter()
# shelter.adopt(phanson, cocoa)
# shelter.adopt(phanson, cheddar)
# shelter.adopt(phanson, darwin)
# shelter.adopt(bholmes, kennedy)
# shelter.adopt(bholmes, sweetie)
# shelter.adopt(bholmes, molly)
# shelter.adopt(bholmes, chester)

# shelter.print_adoptions()
# print(f"{phanson.name} has {phanson.number_of_pets()} "
#       "adopted pets.")
# print(f"{bholmes.name} has {bholmes.number_of_pets()} "
#       "adopted pets.")

# print("refactoring vehicles")

# class Vehicle:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

#     def info(self):
#         return f"{self.make} {self.model}"

# class Car(Vehicle):
#     def get_wheels(self):
#         return 4

# class Motorcycle(Vehicle):
#     def get_wheels(self):
#         return 2

# class Truck(Vehicle):
#     def __init__(self, make, model, payload):
#         super().__init__(make, model)
#         self.payload = payload

#     def get_wheels(self):
#         return 6

# car = Car("Toyota", "Corolla")
# motorcycle = Motorcycle("Yamaha", "R3")
# truck = Truck("Ford", "F-150", "2 tons")

# print(car.info())           # Toyota Corolla
# print(car.get_wheels())     # 4

# print(motorcycle.info())    # Yamaha R3
# print(motorcycle.get_wheels())  # 2

# print(truck.info())         # Ford F-150
# print(truck.get_wheels())   # 6
# print(truck.payload)        # 2 tons

# print('moving')

# class Animal:
#     def walk(self):
#         return f"{self.name} {self.gait()} forward"

# class Person(Animal):
#     def __init__(self, name):
#         self.name = name

#     def gait(self):
#         return "strolls"

# class Cat(Animal):
#     def __init__(self, name):
#         self.name = name

#     def gait(self):
#         return "saunters"

# class Cheetah(Animal):
#     def __init__(self, name):
#         self.name = name

#     def gait(self):
#         return "runs"


# mike = Person("Mike")
# print(mike.walk())  # Expected: "Mike strolls forward"

# kitty = Cat("Kitty")
# print(kitty.walk())  # Expected: "Kitty saunters forward"

# flash = Cheetah("Flash")
# print(flash.walk())  # Expected: "Flash runs forward"


# print("mobility")

# class Noble(Person):
#     def __init__(self, name, title):
#         super().__init__(name)
#         self.title = title

#     def gait(self):
#         return "saunters"

#     def walk(self):
#         return f"{self.title} {super().walk()}"

# byron = Noble("Byron", "Lord")
# print(byron.walk())  # "Lord Byron struts forward"
# print(byron.name)    # "Byron"
# print(byron.title)   # "Lord"


# print("Complete the Program - Houses!")

# class House:
#     def __init__(self, price):
#         self.price = price

#     def __lt__(self, other):
#         return self.price < other.price

#     def __gt__(self, other):
#         return self.price > other.price

# home1 = House(100000)
# home2 = House(150000)

# if home1 < home2:
#     print("Home 1 is cheaper")
# if home2 > home1:
#     print("Home 2 is more expensive")

# print('wallet')

# class Wallet:
#     def __init__(self, amount):
#         self.amount = amount

#     def __add__(self, other):
#         return Wallet(self.amount + other.amount)

#     def __str__(self):
#         return f"Wallet with ${self.amount}"

# wallet1 = Wallet(50)
# wallet2 = Wallet(30)
# merged_wallet = wallet1 + wallet2
# print(merged_wallet)

print('Reverse Engineering')

class Transform:
  def __init__(self, text):
    self.text = text

  def uppercase(self):
    return self.text.upper()

  def lowercase(text):
    return text.casefold()

my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz