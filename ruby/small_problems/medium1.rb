# def rotate_array(array)
#     array[1..-1] << array[0]
# end

# # puts rotate_array([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7]
# # puts rotate_array(['a', 'b', 'c']) == ['b', 'c', 'a']
# # puts rotate_array(['a']) == ['a']

# # x = [1, 2, 3, 4]
# # rotate_array(x) == [2, 3, 4, 1]   # => true
# # x == [1, 2, 3, 4]                 # => true

# def rotate_rightmost_digits(number, places)
#     nums_array = number.digits.reverse
#     (nums_array << rotate_array(nums_array.pop places)).flatten.join('').to_i
# end

# # puts rotate_rightmost_digits(735291, 1) == 735291
# # puts rotate_rightmost_digits(735291, 2) == 735219
# # puts rotate_rightmost_digits(735291, 3) == 735912
# # puts rotate_rightmost_digits(735291, 4) == 732915
# # puts rotate_rightmost_digits(735291, 5) == 752913
# # puts rotate_rightmost_digits(735291, 6) == 352917

# def max_rotation(number)
#   length = number.digits.length

#   length.times do |index|
#     places = length - index
#     number = rotate_rightmost_digits(number, places)
#   end
#   number
# end

# puts max_rotation(735291) == 321579
# puts max_rotation(3) == 3
# puts max_rotation(35) == 53
# puts max_rotation(105) == 15 # the leading zero gets dropped
# puts max_rotation(8_703_529_146) == 7_321_609_845

def thousand_lights(n)
  lights = Array.new n, false

  n.times do |index|
    i = index + 1
    lights.map!.with_index do |state, num|
      number = num + 1
      number % i == 0 ? !state : state
    end
  end
  
  lights.each_with_index.reduce([]) do |acc, (light_on, index)|
    acc << index + 1 if light_on
    acc
  end 
end

p thousand_lights 10