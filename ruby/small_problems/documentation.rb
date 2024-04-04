# require 'date'

# puts Date.civil
# puts Date.civil(2016)
# puts Date.civil(2016, 5)
# puts Date.civil(2016, 5, 13)

# puts Date.new
# puts Date.new(2016)
# puts Date.new(2016, 5)
# puts Date.new(2016, 5, 13)

# def my_method(a, b = 2, c = 3, d)
#     p [a, b, c, d]
# end
  
# my_method(4, 5, 6)

# # => [4, 5, 3, 6]

# a = [1, 4, 8, 11, 15, 19]

# puts a.bsearch { |element| element >= 8 }

a = %w(a b c d e)
# puts a
# puts a.fetch(7)
puts a.fetch(7, 'beats me')
puts a.fetch(7) { |index| index**2 }

# 5.step(to: 10, by: 3) { |value| puts value }

# s = 'abc'
# puts s.public_methods.inspect

# a = [5, 9, 3, 11]
# puts a.min