
# def greetings(name, career)
#   "Hello, #{name[0]} #{name[1]} #{name[2]}! Nice to have a #{career[:title]} #{career[:occupation]} around."
# end

# p greetings(['John', 'Q', 'Doe'], { title: 'Master', occupation: 'Plumber' })
# # => "Hello, John Q Doe! Nice to have a Master Plumber around."

# def twice(num)
#   string = num.to_s
#   length = string.length
#   half = length / 2

#   if length.even?
#     first = string.slice(0, half)
#     second = string.slice(half, half)
#     return num if first == second
#   end
#   num * 2
# end

# puts twice(37) == 74
# puts twice(44) == 44
# puts twice(334433) == 668866
# puts twice(444) == 888
# puts twice(107) == 214
# puts twice(103103) == 103103
# puts twice(3333) == 3333
# puts twice(7676) == 7676
# puts twice(123_456_789_123_456_789) == 123_456_789_123_456_789
# puts twice(5) == 10

# def sequence(num) 
#   [*1..num]

#   # array =[]

#   # (1..num).each do |value|
#   #   array << value
#   # end

#   # array
# end

# puts sequence(5) == [1, 2, 3, 4, 5]
# puts sequence(3) == [1, 2, 3]
# puts sequence(1) == [1]

# def word_lengths(text)
#   text.split(' ').reduce([]) do |array, word|
#     array << "#{word} #{word.length}"
#   end
# end

# puts word_lengths("cow sheep chicken") == ["cow 3", "sheep 5", "chicken 7"]

# puts word_lengths("baseball hot dogs and apple pie") ==
#   ["baseball 8", "hot 3", "dogs 4", "and 3", "apple 5", "pie 3"]

# puts word_lengths("It ain't easy, is it?") == ["It 2", "ain't 5", "easy, 5", "is 2", "it? 3"]

# puts word_lengths("Supercalifragilisticexpialidocious") ==
#   ["Supercalifragilisticexpialidocious 34"]

# puts word_lengths("") == []

# def swap_name(name)
# name.split.reverse.join(', ')
# end

# puts swap_name('Joe Roberts') == 'Roberts, Joe'

# def sequence(a, b)
#   array = []
#   a.times { |count| array << (count + 1) * b }
#   array
# end

# puts sequence(5, 1) == [1, 2, 3, 4, 5]
# puts sequence(4, -7) == [-7, -14, -21, -28]
# puts sequence(3, 0) == [0, 0, 0]
# puts sequence(0, 1000000) == []

# def get_grade(a, b, c)
#   average = (a + b + c) / 3
#   return 'A' if average >= 90
#   return 'B' if average >= 80
#   return 'C' if average >= 70
#   return 'D' if average >= 60
#   'F'
# end

# puts get_grade(95, 90, 93) == "A"
# puts get_grade(50, 50, 95) == "D"

# def buy_fruit(something)
#   something.reduce([]) do |array, value|
#     value[1].times { array << value[0] }
#     array
#   end
# end

# puts buy_fruit([["apples", 3], ["orange", 1], ["bananas", 2]]) == ["apples", "apples", "apples", "orange", "bananas","bananas"]

# def anagrams(words)
#   anagrams = []

#   words.each do |word|
#     perms = word.split('').permutation.inject([]) { |perms, perm| perms << perm }

#     anagrams.each do |anagram|
#       perms.each do |perm|
#         break anagram << word if anagram.include? perm.join('')
#       end
#     end

#     anagrams << [word] unless anagrams.flatten.include? word
#   end

#   anagrams
# end


# words =  ['demo', 'none', 'tied', 'evil', 'dome', 'mode', 'live',
#           'fowl', 'veil', 'wolf', 'diet', 'vile', 'edit', 'tide',
#           'flow', 'neon', 'turd', 'dust']

# p anagrams words

# def sum(num)
#     num.digits.sum
# end

# puts sum(23) == 5
# puts sum(496) == 19
# puts sum(123_456_789) == 45

# 12345.digits #=> [5, 4, 3, 2, 1]

# def oddities(array)
#     array.select.with_index do |_, index|
#         index.even?
#     end
# end

# puts oddities([2, 3, 4, 5, 6]) == [2, 4, 6]
# puts oddities([1, 2, 3, 4, 5, 6]) == [1, 3, 5]
# puts oddities(['abc', 'def']) == ['abc']
# puts oddities([123]) == [123]
# puts oddities([]) == []
# puts oddities([1, 2, 3, 4, 1]) == [1, 3, 1]