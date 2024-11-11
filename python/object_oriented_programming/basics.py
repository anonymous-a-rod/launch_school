# Comments show expected output
print(type("Hello"))                # <class 'str'>
print(type(5))                      # <class 'int'>
print(type([1, 2, 3]))              # <class 'list'>

class Cat:
  total_cats = 0
  COLOR = 'red'

  def __init__(self, name=''):
    self._name = name
    Cat.total_cats += 1

  def __str__(self):
    return f"I'm {self.name}!"

  @classmethod
  def total(cls):
    return cls.total_cats

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, value):
    self._name = value

  def rename(self, name):
    self.name = name

  def personal_greeting(self):
    print(f"Hello! My name is {self._name}!")

  def greet(self):
    print(f"Hello! My name is {self.name} and I'm a {Cat.COLOR} cat!")

  def generic_greeting(self):
    print("Hello! I'm a cat!")

  def identify(self):
    return self

print(Cat.total())
kitty = Cat('Sophie')
kitty.greet()
kitty.generic_greeting()

kitty.rename('Chloe')
print(kitty.name)             # Chloe
print(kitty.identify())
kitty.personal_greeting() 

print(Cat.total())
Cat()

print(Cat.total())
Cat()
print(Cat.total())

print(kitty)

class Person:
  def __init__(self, name="John Doe"):
    self.name = name

person1 = Person()
person2 = Person("Pepe Le Pew")

# Comments show expected output
print(person1.name)    # John Doe
print(person2.name)    # Pepe Le Pew