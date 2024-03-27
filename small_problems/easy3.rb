# numbers = []

# ['1st', '2nd', '3rd', '4th', '5th'].each do |n|
#     puts "Enter the #{n} number:"
#     numbers << gets.chomp.to_i
# end

# puts "Enter the last number:"
# last = gets.chomp.to_i
# included = numbers.include? last

# puts "The number #{last} #{included ? 'appears' : 'does not appear'} in #{numbers}."

# puts "Enter the first number:"
# first = gets.to_i

# puts "Enter the second number:"
# second = gets.to_i

# puts first + second
# puts first - second
# puts first * second
# puts first / second
# puts first % second
# puts first ** second

# puts "Please write word or multiple words:"
# text = gets.chomp

# puts "There are #{text.length} characters in \"#{text}\"."


# def multiply(a, b)
#     a * b
# end

# puts multiply(5, 3)

# def square(n)
#     n ** 2
# end

# puts square(5)
# puts square(-8)

# def xor?(a, b)
#     return false if a && b
#     return true if a || b
#     false
# end

# puts xor?(5.even?, 4.even?) == true
# puts xor?(5.odd?, 4.odd?) == true
# puts xor?(5.odd?, 4.even?) == false
# puts xor?(5.even?, 4.odd?) == false

# def palindrome?(text)
#     reverse = text.split('').reverse.join('')
#     text == reverse
# end

# puts palindrome?('madam') == true
# puts palindrome?('Madam') == false
# puts palindrome?("madam i'm adam") == false
# puts palindrome?('356653') == true

# def palindromic_number?(n)
#     n = n.to_s 
#     n == n.split('').reverse.join('')
# end

# puts palindromic_number?(34543) == true
# puts palindromic_number?(123210) == false
# puts palindromic_number?(22) == true
# puts palindromic_number?(5) == true

# def uppercase?(text)
#     text.upcase == text
# end

# puts uppercase?('t') == false
# puts uppercase?('T') == true
# puts uppercase?('Four Score') == false
# puts uppercase?('FOUR SCORE') == true
# puts uppercase?('4SCORE!') == true
# puts uppercase?('') == true