# def interleave(a, b)
#   combined = []
#   a.each_with_index do |_, index|
#     combined << a[index]
#     combined << b[index]
#   end
#   combined
# end

# puts interleave([1, 2, 3], ['a', 'b', 'c']) == [1, 'a', 2, 'b', 3, 'c']

# def letter_case_count(text)
#   cases = { lowercase: 0, uppercase: 0, neither: 0 }
#   text.split('').each do |letter| 
#     next cases[:lowercase] += 1 if letter.match? /[a-z]/
#     next cases[:uppercase] += 1 if letter.match? /[A-Z]/
#     cases[:neither] += 1
#   end
#   cases
# end

# puts letter_case_count('abCdef 123') == { lowercase: 5, uppercase: 1, neither: 4 }
# puts letter_case_count('AbCd +Ef') == { lowercase: 3, uppercase: 3, neither: 2 }
# puts letter_case_count('123') == { lowercase: 0, uppercase: 0, neither: 3 }
# puts letter_case_count('') == { lowercase: 0, uppercase: 0, neither: 0 }

# def word_cap(text)
#   text.split.map do |word|
#     word.capitalize
#   end.join(" ")
# end

# puts word_cap('four score and seven') == 'Four Score And Seven'
# puts word_cap('the javaScript language') == 'The Javascript Language'
# puts word_cap('this is a "quoted" word') == 'This Is A "quoted" Word'


# def swapcase(text)
#   text.split('').map do |letter|
#     next letter.upcase if letter.match? /[a-z]/
#     next letter.downcase if letter.match? /[A-Z]/
#     letter
#   end.join('')
# end

# puts swapcase('PascalCase') == 'pASCALcASE'
# puts swapcase('Tonight on XYZ-TV') == 'tONIGHT ON xyz-tv'

# def staggered_case(text)
#   text.split('').each_with_index do |letter, index|
#     next letter.downcase! if index.odd?
#     next letter.upcase! if index.even?
#     letter
#   end.join
# end

# puts staggered_case('I Love Launch School!') == 'I LoVe lAuNcH ScHoOl!'
# puts staggered_case('ALL_CAPS') == 'AlL_CaPs'
# puts staggered_case('ignore 77 the 444 numbers') == 'IgNoRe 77 ThE 444 NuMbErS'

# def show_multiplicative_average(array)
#   elements = array.length.to_f
#   product = array.reduce(&:*).to_f
#   # "%.3f" % (product / elements)
#   (product / elements).round 3
# end

# puts show_multiplicative_average([3, 5])                # => The result is 7.500
# puts show_multiplicative_average([6])                   # => The result is 6.000
# puts show_multiplicative_average([2, 5, 7, 11, 13, 17]) # => The result is 28361.667

# def multiply_list(a, b)
#   a.map.with_index do |element, index|
#     element = a[index] * b[index]
#   end
# end

# puts multiply_list([3, 5, 7], [9, 10, 11]) == [27, 50, 77]

# def multiply_all_pairs(a, b)
#   products = []
#   a.each do |x|
#     b.each do |y|
#       products << x * y
#     end
#   end
#   products.sort
# end

# puts multiply_all_pairs([2, 4], [4, 3, 1, 2]) == [2, 4, 4, 6, 8, 8, 12, 16]

# def penultimate(text)
#     text.split[-2]
# end

# puts penultimate('last word') == 'last'
# puts penultimate('Launch School is great!') == 'is'

# def count_occurrences(array)
#     hash = { }
#     array.each do |item|
#         hash[item] = 0 if hash[item].nil?
#         hash[item] += 1
#     end
#     hash
# end

# vehicles = [
#   'car', 'car', 'truck', 'car', 'SUV', 'truck',
#   'motorcycle', 'motorcycle', 'car', 'truck'
# ]

# p count_occurrences(vehicles)