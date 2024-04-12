# def sum_of_sums(array)
#   total = 0
#   array.each_with_index do |_, index|
#     total += array.slice(0, index + 1).sum
#   end
#   total
# end

# puts sum_of_sums([3, 5, 2]) == (3) + (3 + 5) + (3 + 5 + 2) # -> (21)
# puts sum_of_sums([1, 5, 7, 3]) == (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) # -> (36)
# puts sum_of_sums([4]) == 4
# puts sum_of_sums([1, 2, 3, 4, 5]) == 35

# def leading_substrings(string)
#     letter_array = []
#     string.length.times do |index|
#         letter_array << string.slice(0, index + 1)
#     end
#     letter_array
# end

# # # puts leading_substrings('abc') == ['a', 'ab', 'abc']
# # # puts leading_substrings('a') == ['a']
# # # puts leading_substrings('xyzzy') == ['x', 'xy', 'xyz', 'xyzz', 'xyzzy']

# def substrings(string)
#   array = []
#   length = string.length
#   length.times do |count|
#     array << leading_substrings(string.slice(count, length - count))
#   end
#   array.flatten
# end

# # puts substrings('abcde') == [
# #   'a', 'ab', 'abc', 'abcd', 'abcde',
# #   'b', 'bc', 'bcd', 'bcde',
# #   'c', 'cd', 'cde',
# #   'd', 'de',
# #   'e'
# # ]

# def palindromes(string)
#   array = []
#   length = string.length
#   length.times do |count|
#     leading_substrings(string.slice(count, length - count)).each do |value|
#       array << value if value.reverse == value && value.length > 1
#     end
#   end
#   p array.flatten
# end

# palindromes('abcd') == []
# palindromes('madam') == ['madam', 'ada']
# palindromes('hello-madam-did-madam-goodbye') == [
#   'll', '-madam-', '-madam-did-madam-', 'madam', 'madam-did-madam', 'ada',
#   'adam-did-mada', 'dam-did-mad', 'am-did-ma', 'm-did-m', '-did-', 'did',
#   '-madam-', 'madam', 'ada', 'oo'
# ]
# puts palindromes('knitting cassettes') == [
#   'nittin', 'itti', 'tt', 'ss', 'settes', 'ette', 'tt'
# ]

# def fizzbuzz(a, b)
#   (a..b).each do |num|
#     next puts 'FizzBuzz' if num % 3 == 0 && num % 5 == 0
#     next puts 'Buzz' if num % 5 == 0 
#     next puts 'Fizz' if num % 3 == 0
#     puts num
#   end
# end

# fizzbuzz(1, 15) # -> 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz

# def repeater(string)
#     string.split('').map { |c| c * 2 }.join('')
# end

# puts repeater('Hello') == "HHeelllloo"
# puts repeater("Good job!") == "GGoooodd  jjoobb!!"
# puts repeater('') == ''

def double_consonants(string)
    string.each_char.map do |c|
        next c if c.downcase =~ /[^b-df-hj-np-tv-z]/
        c * 2
    end.join('')
end

p double_consonants("String") # Output: "SSttrrinngg"

puts double_consonants('String') == "SSttrrinngg"
puts double_consonants("Hello-World!") == "HHellllo-WWorrlldd!"
puts double_consonants("July 4th") == "JJullyy 4tthh"
puts double_consonants('') == ""