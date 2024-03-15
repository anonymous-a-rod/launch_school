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

user_passwords = {
    aaron: "icecream",
    kelso: "steamroller",
    colin: "fasting"
}

loop do 
    puts ">> Please enter your username"
    input_username = gets.chomp.to_sym

    puts ">> Please enter your password"
    input_user_password = gets.chomp

    if user_passwords[input_username] != input_user_password
        puts ">> Authorization failed!"
        next
    end

    puts "welcome!"
    break
end




