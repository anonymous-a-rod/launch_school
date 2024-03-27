# def repeat(word, amount)
#     return unless amount.instance_of?(Integer) && amount > 0
#     amount.times { puts word}
# end

# repeat('Hello', 3)

# def is_odd?(num)
#     num.odd?
# end

# puts is_odd?(2)    # => false
# puts is_odd?(5)    # => true
# puts is_odd?(-17)  # => true
# puts is_odd?(-8)   # => false
# puts is_odd?(0)    # => false
# puts is_odd?(7)    # => true

# def stringy(number)
#     string = ''
#     number.times { |index| string += (index.even? ? '1' : '0') }
#     string
# end

# puts stringy(6) == '101010'
# puts stringy(9) == '101010101'
# puts stringy(4) == '1010'
# puts stringy(7) == '1010101'

# def calculate_bonus(salary, bonus)
#     bonus ? salary / 2 : 0
# end

# puts calculate_bonus(2800, true) == 1400
# puts calculate_bonus(1000, false) == 0
# puts calculate_bonus(50000, true) == 25000

# def print_in_box(sentence)
#     length = sentence.length + 2
#     puts " +#{'-' * length}+"
#     puts " |#{' ' * length}|"
#     puts " | #{sentence} |"
#     puts " |#{' ' * length}|"
#     puts " +#{'-' * length}+"
# end

# print_in_box('To boldly go where no one has gone before.')
# # +--------------------------------------------+
# # |                                            |
# # | To boldly go where no one has gone before. |
# # |                                            |
# # +--------------------------------------------+

# print_in_box('')
# # +--+
# # |  |
# # |  |
# # |  |
# # +--+

# def triangle(num)
#     num.times { |i| puts "#{" " * (num - i - 1)}#{"*" * (i+1)}"}
# end

# triangle(5)
# triangle(9)

# puts "Enter a noun:"
# noun = gets.chomp
# puts "Enter a verb:"
# verb = gets.chomp
# puts "Enter a adjective:"
# adjective = gets.chomp
# puts "Enter a adverb:"
# adverb = gets.chomp

# Dputs "Do you walk your blue #{noun} quickly? That's hilarious!"

# def reversed_number(num)
#     num.to_s.reverse.to_i
# end

# puts reversed_number(12345) == 54321
# puts reversed_number(12213) == 31221
# puts reversed_number(456) == 654
# puts reversed_number(12000) == 21 # No leading zeros in return value!
# puts reversed_number(12003) == 30021
# puts reversed_number(1) == 1

# def center_of(text)
#     length = text.length
#     mid = length/2
#     return text[mid] if length.odd?
#     text.slice(mid - 1, 2)
# end

# puts center_of('I love ruby') == 'e'
# puts center_of('Launch School') == ' '
# puts center_of('Launch') == 'un'
# puts center_of('Launchschool') == 'hs'
# puts center_of('x') == 'x'