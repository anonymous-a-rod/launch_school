# count = 1

# loop do
#     puts "#{count} is #{count.even? ? "even" : "odd"}!"
#     count += 1
#     break if count > 5 
# end

# loop do
#     number = rand(100)
#     puts number

#     break if number >= 0 && number <= 10
# end

# process_the_loop = [true, false].sample

# if process_the_loop
#     loop do 
#         puts 'the loop was processed'
#         break
#     end
# else
#     puts "the loop wasn't processed"
# end

# loop do
#     puts 'What does 2 + 2 equal?'
#     answer = gets.chomp.to_i
#     if answer == 4
#         puts "that is correct!"
#         break
#     else
#         puts "wrong answer, try again!"
#     end
# end

# numbers = []

# loop do

#   puts 'Enter any number:'

#   input = gets.chomp.to_i

#     numbers << input 
    
#     break if numbers.length >= 5

# end

# p numbers

# names = ['Sally', 'Joe', 'Lisa', 'Henry']

# loop do
    
#     name = names.pop

#     puts name

#     break if names.length <= 0

# end

# p names


# 5.times do |index|
#     puts index
#     break if index >= 2
#   end

# number = 0

# until number == 10
#   number += 1
#   next if number.odd?
#   puts number
# end

# number_a = 0
# number_b = 0

# loop do

#   number_a += rand(2)
#   number_b += rand(2)

#   next if number_a < 5 && number_b < 5

#   puts number_a 
#   puts number_b

#   puts "5 was reached!"
#   break
  
# end

# def greeting
#     puts 'Hello!'
# end
  
# count = 0
# number_of_greetings = 2

# while count < number_of_greetings
#     count += 1
#     greeting
# end


def something
    num = rand 100
    greeting = 'hi'
    "#{greeting}, your number was #{num}"
end

puts something
