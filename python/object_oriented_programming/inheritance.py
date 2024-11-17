# class Vehicle:
#     def __init__(self, year):
#         self._year = year

#     @property
#     def year(self):
#         return self._year

#     def start_engine(self):
#         return 'Ready to go!'

# class Car(Vehicle):
#     pass

# class Truck(Vehicle):
#     def __init__(self, year, bed_type):
#         super().__init__(year)
#         self.bed_type = bed_type

#     def start_engine(self, speed):
#         return f'Ready to go! Drive {speed}, please!'



# # Comments show expected output
# truck1 = Truck(1994, 'Short')
# print(truck1.year)            # 1994
# print(truck1.bed_type)        # Short
# print(truck1.start_engine('fast'))

# car1 = Car(2006)
# print(car1.year)              # 2006
# # print(car1.bed_type)
# # AttributeError: 'Car' object has no attribute 'bed_type'





# class WalkingMixin:
#     def walk(self):
#         print("Let's go for a walk!")

# class Cat(WalkingMixin):
#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):
#         return self._name

#     def greet(self):
#         print(f"Hello! My name is {self.name}!")

# # Comments show expected output
# kitty = Cat('Sophie')
# kitty.greet()       # Hello! My name is Sophie!
# kitty.walk()        # Let's go for a walk!


# class Towable:
#     def tow(self):
#         return "I can tow a trailer!"

# class Vehicle():
#     def __init__(self, year):
#         self._year = year

#     @property
#     def year(self):
#         return self._year


# class Truck(Towable, Vehicle):
#     pass

# class Car(Vehicle):
#     pass

#  # Comments show expected output
# truck1 = Truck(1994)
# print(truck1.year)            # 1994
# print(truck1.tow())           # I can tow a trailer!

# car1 = Car(2006)
# print(car1.year)              # 2006


class Animal:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

class Cat(Animal):
    pass

class Bird(Animal):
    pass

cat1 = Cat('Black')
print(cat1.color)

print(Cat.mro())
