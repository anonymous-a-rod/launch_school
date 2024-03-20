# def print_me 
#     puts "I'm printing within the method"
# end

# print_me

# def print_me 
#     "I'm printing the return value!"
# end

# puts print_me

# def hello
#     "Hello"
# end

# def world
#     'World'
# end

# def greet
#     puts "#{hello} #{world}"
# end

# greet


# def car(string_a, string_b)
#     puts "#{string_a} #{string_b}"
# end

# car("Honda", "Accord")

# def time_of_day(daylight)
#     puts daylight ? "It's daytime" : "It's nightime"
# end

# daylight = [true, false].sample

# time_of_day daylight

# def dog(name)
#     return name
# end

# def cat(name)
#     return name
# end

# puts "The dog's name is #{dog('Spot')}."
# puts "The cat's name is #{cat('Spot')}."

# def assign_name(name = "Bob")
#     "#{name}"
# end

# puts assign_name('Kevin') == 'Kevin'
# puts assign_name == 'Bob'

# def add(a, b)
#     a + b 
# end

# def multiply(a, b)
#     a * b
# end

# puts add(2, 2) == 4
# puts add(5, 4) == 9
# puts multiply(add(2, 2), add(5, 4)) == 36

# names = ['Dave', 'Sally', 'George', 'Jessica']
# activities = ['walking', 'running', 'cycling']

# def name(names)
#     names.sample
# end

# def activity(activities)
#     activities.sample
# end

# def sentence(name, activity)
#     "To alleviate constipation #{name} likes to go #{activity}"
# end

# puts sentence(name(names), activity(activities))

# "hello"

['h', 'e', 'l', 'l', 'o']

['h', nil, 'l', 'l', nil].compact.reverse.join => 'llh'
[nil, 'e', nil, 'o']