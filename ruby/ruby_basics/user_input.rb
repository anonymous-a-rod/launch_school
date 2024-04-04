# puts ">> Type anything you want:"

# user_input = gets.chomp   

# p user_input

# puts ">> What is your age in years?"

# MONTHS_PER_YEAR = 12

# user_input = gets.chomp.to_i
# age_in_months = user_input * MONTHS_PER_YEAR

# puts "You are #{age_in_months} months old!"


# loop do
#     puts ">> Would you like me to print 'something'? (y/n)"
#     user_input = gets.chomp.downcase
#     puts "something" if user_input == "y" 

#     break if user_input == "y" || user_input == "n"
#     puts "Invalid input! Please enter y or n"    
# end
# || is the logical or operator 
# && is the logical and operator


# loop do
#     puts '>> How many output lines do you want? Enter a number >= 3:'
#     user_input = gets.chomp.to_i

#     if user_input <= 3
#         puts "That's not enough lines."
#         next
#     end  

#     user_input.times { puts 'Launch School is the best!' }
#     break
# end 

# user_passwords = {
#     aaron: "icecream",
#     kelso: "steamroller",
#     colin: "fasting"
# }

# loop do 
#     puts ">> Please enter your username"
#     input_username = gets.chomp.to_sym

#     puts ">> Please enter your password"
#     input_user_password = gets.chomp

#     if user_passwords[input_username] != input_user_password
#         puts ">> Authorization failed!"
#         next
#     end

#     puts "welcome!"
#     break
# end


# puts "Type numerator"
# numerator = gets.chomp

# puts "Type denominator"
# denominator = gets.chomp

# def valid_number?(number_string)
#     number_string.to_i.to_s == number_string
# end

# def divide(num_one, num_two)
#     return "Must be valid integer" unless valid_number?(num_one) && valid_number?(num_two)
#     return "Can't divide by zero" if num_one.to_i == 0
#     "#{num_one} divided by #{num_two} is #{num_one.to_f / num_two.to_f}"
# end

# puts divide(numerator, denominator)

# number_of_lines = nil

# loop do
#     loop do
#     puts '>> How many output lines do you want? Enter a number >= 3:'
#     number_of_lines = gets.to_i
#     break if number_of_lines >= 3
#     puts ">> That's not enough lines."
#     end

#     while number_of_lines > 0
#     puts 'Launch School is the best!'
#     number_of_lines -= 1
#     end

#     puts "Type c to continue or q to exit the program"

#     user_input = gets.chomp.downcase

#     break if user_input == "q"
# end

# def valid_number?(number_string)
#     number_string.to_i.to_s == number_string && number_string.to_i != 0
# end

# def add_opposite_sign_ints(num1, num2)
#     return "Must be valid integer" unless valid_number?(num1) && valid_number?(num2)
#     return "One number must be negative and the other positive" unless ((num1.to_i > 0 && num2.to_i < 0) || (num1.to_i < 0 && num2.to_i > 0))
#     "#{num1} plus #{num2} is #{num1.to_i + num2.to_i}"
# end

# puts "Type first int"
# first = gets.chomp

# puts "Type second int"
# second = gets.chomp

# puts add_opposite_sign_ints first, second

