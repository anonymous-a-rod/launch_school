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

def leading_substrings(string)
    letter_array = []
    string.length.times do |index|
        letter_array << string.slice(0, index + 1)
    end
    letter_array
end

puts leading_substrings('abc') == ['a', 'ab', 'abc']
puts leading_substrings('a') == ['a']
puts leading_substrings('xyzzy') == ['x', 'xy', 'xyz', 'xyzz', 'xyzzy']