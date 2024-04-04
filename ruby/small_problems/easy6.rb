# def dms(num)
#     d = num.floor
#     minutes_per_degree = 1.0 / 60.0
#     m = ((num % 1) / minutes_per_degree).floor
#     seconds_per_degree = minutes_per_degree / 60.0
#     s = ((num % minutes_per_degree) / seconds_per_degree).round
#     m += (s / 60)
#     s %= 60

#     d %= 360
#     m = "0#{m}" if m < 10 
#     s = "0#{s}" if s < 10

#     %(#{d}°#{m}'#{s}")
# end

# # All test cases should return true
#                 %(30°00'00")
# puts dms(30) == %(30°00'00")
# puts dms(76.73) == %(76°43'48")
# puts dms(254.6) == %(254°36'00")
# puts dms(93.034773) == %(93°02'05")
# puts dms(0) == %(0°00'00")
# puts dms(360) == %(360°00'00") || dms(360) == %(0°00'00")

# def remove_vowels(array)
#     array.map { |text| text.gsub(/[aeiouAEIOU]/,'')}
# end

# puts remove_vowels(%w(abcdefghijklmnopqrstuvwxyz)) == %w(bcdfghjklmnpqrstvwxyz)
# puts remove_vowels(%w(green YELLOW black white)) == %w(grn YLLW blck wht)
# puts remove_vowels(%w(ABC AEIOU XYZ)) == ['BC', '', 'XYZ']

# def find_fibonacci_index_by_length(length)
#     return 1 if length == 1
#     count = 7
#     fib = [1, 1, 2, 3, 5, 8, 13]
#     while fib.last.to_s.length < length
#         fib << (fib[-1] + fib[-2])
#     end
#     fib.length
# end

# puts find_fibonacci_index_by_length(2) == 7          # 1 1 2 3 5 8 13
# puts find_fibonacci_index_by_length(3) == 12         # 1 1 2 3 5 8 13 21 34 55 89 144
# puts find_fibonacci_index_by_length(10) == 45
# puts find_fibonacci_index_by_length(100) == 476
# puts find_fibonacci_index_by_length(1000) == 4782
# puts find_fibonacci_index_by_length(10000) == 47847

# def reverse!(array)
#     copy = array.dup
#     length = array.length

#     array.each_with_index do |element, index|
#         array[index] = copy[length - 1 -index]
#     end
# end

# list = %w(a b e d c)
# puts reverse!(list) == ["c", "d", "e", "b", "a"] # true
# # list == ["c", "d", "e", "b", "a"] # true

# list = ['abc']
# puts reverse!(list) == ["abc"] # true
# # list == ["abc"] # true

# list = []
# puts reverse!(list) == [] # true
# # list == [] # true

# puts reverse!([1,2,3,4]) == [4,3,2,1]          # => true
# puts reverse!(%w(a b e d c)) == %w(c d e b a)  # => true
# puts reverse!(['abc']) == ['abc']              # => true
# puts reverse!([]) == []                        # => true

# def merge(a, b)
#     (a + b).uniq
# end

# puts merge([1, 3, 5], [3, 6, 9]) == [1, 3, 5, 6, 9]

# def halvsies(array)
#     first = (array.length.to_f / 2).ceil
#     second = array.length / 2
#     [array.slice(0,first), array.slice(first, second)]
# end

# puts halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]]
# puts halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]]
# puts halvsies([5]) == [[5], []]
# puts halvsies([]) == [[], []]

# def find_dup(array)
#     array.sort!
#     array.each_with_index do |element, index|
#         return element if element == array[index+1]
#     end
#     nil
# end

# puts find_dup([1, 5, 3, 1]) == 1
# puts find_dup([18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
#           38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
#           14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
#           78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
#           89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
#           41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
#           55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
#           85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
#           40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
#           7,  34, 57, 74, 45, 11, 88, 67,  5, 58]) == 73

# def include?(array, value)
#     array.each do |x|
#         return true if x == value
#     end
#     false
# end

# puts include?([1,2,3,4,5], 3) == true
# puts include?([1,2,3,4,5], 6) == false
# puts include?([], 3) == false
# puts include?([nil], nil) == true
# puts include?([], nil) == false

array1 = %w(Moe Larry Curly Shemp Harpo Chico Groucho Zeppo)
array2 = []
array1.each { |value| array2 << value }
array1.each { |value| value.upcase! if value.start_with?('C', 'S') }
p array2
# => ["Moe", "Larry", "CURLY", "SHEMP", "Harpo", "CHICO", "Groucho", "Zeppo"]
p array1.object_id
# => 60
p array2.object_id
# => 80