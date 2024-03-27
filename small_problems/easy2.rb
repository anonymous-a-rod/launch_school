# puts "Teddy is #{rand(20..200)} years old!"

# puts "Enter the length of the room in meters:"
# length = gets.chomp.to_f

# puts "Enter the width of the room in meters:"
# width = gets.chomp.to_f

# square = length * width

# puts "The area of the room is #{square.round 1} square meters (#{(square * 10.7639).round 2} square feet)."

# puts "What is the bill?"
# bill = gets.chomp.to_f
# puts "What is the tip percentage?"
# tip_percent = gets.chomp.to_f
# tip = bill * (tip_percent/100)
# total = bill + tip

# puts "The tip is $#{tip.round 2}"
# puts "The total is $#{total.round 2}"

# require 'date'
# current_year = Date.today.year

# puts "What is your age?"
# current_age = gets.chomp.to_i

# puts "At what age would you like to retire?"
# retirement_age = gets.chomp.to_i

# years_till_retirement = retirement_age - current_age
# retirement_year = current_year + years_till_retirement

# puts "It's #{current_year}. You will retire in #{retirement_year}."
# puts "You have only #{years_till_retirement} years of work to go!"

# puts "What is your name?"
# name = gets.chomp

# if name[-1] == '!'
#     puts "HELLO #{name.gsub('!','').upcase}. WHY ARE WE SCREAMING?"
# else
#     puts "Hello #{name}."
# end

# [*1..99].each { |n| puts n if n.odd? }
# [*1..99].each { |n| puts n if n.even? }

# puts " Please enter an integer greater than 0:"
# int = gets.to_i

# puts "Enter 's' to compute the sum, 'p' to compute the product."
# option = gets.chomp

# if option == 's'
#     sum = [*1..int].sum
#     puts "The sum of the integers between 1 and #{int} is #{sum}."
# end

# if option == 'p'
#     product = [*1..int].reduce(:*)
#     puts "The product of the integers between 1 and #{int} is #{product}."
# end

# name = 'Bob'
# save_name = name
# name.upcase!
# puts name, save_name

def negative(n)
    return n if n < 0
    n * -1
end

puts negative(5) == -5
puts negative(-3) == -3
puts negative(0) == 0      # There's no such thing as -0 in ruby