# loop do
#     puts 'Just keep printing...'
#     break
# end

# loop do
#     puts 'This is the outer loop.'
#     loop do
#         puts 'This is the inner loop.'
#         break
#     end
#     break
# end

# puts 'This is outside all loops.'


# iterations = 1

# loop do
#     puts "Number of iterations = #{iterations}"
#     break if iterations >= 5
#     iterations += 1
# end

# loop do
#     puts 'Should I stop looping?'
#     answer = gets.chomp
#     break if answer == "yes"
# end

# say_hello = true
# count = 1

# while say_hello
#   puts 'Hello!'
#   count += 1
#   say_hello = false if count > 5
# end

# count = 1

# while count <= 5
#   puts 'Hello!'
#   count += 1
# end

# numbers = [1, 23, 65, 64, 14]
# index = 0
# length = numbers.length

# while index < length
#     puts numbers[index]
#     index += 1
# end

# numbers = []

# while numbers.length < 5
#     numbers << rand(100)
# end

# p numbers

# count = 1

# until count == 11
#   puts count
#   count += 1
# end

numbers = [7, 9, 13, 25, 18]
index = 0

until index == numbers.length
    puts numbers[index]
    index += 1
end