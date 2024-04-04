# def ascii_value(text)
#     value = 0
#     text.split('').each do |letter|
#         value += letter.ord
#     end
#     value
# end


# puts ascii_value('Four score') == 984
# puts ascii_value('Launch School') == 1251
# puts ascii_value('a') == 97
# puts ascii_value('') == 0

# def time_of_day(time)
#     time = time % 1440
#     minutes = (time % 60).to_s
#     minutes = "0" + minutes if minutes.length < 2
#     hour = (time / 60).floor.to_s
#     hour = "0" + hour if hour.length < 2
#     hour + ":" + minutes
# end

# puts time_of_day(0) == "00:00"
# puts time_of_day(-3) == "23:57"
# puts time_of_day(35) == "00:35"
# puts time_of_day(-1437) == "00:03"
# puts time_of_day(3000) == "02:00"
# puts time_of_day(800) == "13:20"
# puts time_of_day(-4231) == "01:29"

# def after_midnight(time)
#     hours = time.slice(0,2).to_i % 24
#     minutes = time.slice(3,2).to_i
#     (hours * 60) + minutes
# end

# def before_midnight(time)
#     time = after_midnight(time)
#     time = 1440 - time unless time == 0
#     time
# end

# puts after_midnight('00:00') == 0
# puts before_midnight('00:00') == 0
# puts after_midnight('12:34') == 754
# puts before_midnight('12:34') == 686
# puts after_midnight('24:00') == 0
# puts before_midnight('24:00') == 0

# def swap(text)
#     reverse = text.split.map! do |word|
#         next word if word.length < 2
#         first = word[0]
#         last = word[-1]
#         word[0] = last
#         word[-1] = first
#         word
#     end
#     reverse.join(' ')
# end

# puts swap('Oh what a wonderful day it is') == 'hO thaw a londerfuw yad ti si'
# puts swap('Abcde') == 'ebcdA'
# puts swap('a') == 'a'

# def cleanup(text)
#     text.gsub(/[^a-zA-Z]/, ' ').gsub(/\s+/, ' ')
# end

# puts cleanup("---what's my +*& line?") == ' what s my line '




# def word_sizes(sentence)

#     word_lengths_hash = {}

#     split_words = sentence.split(" ")
# #"[^a-zA-Z]", ""
#     split_words.each do |word|
#         word.gsub!(/[^a-zA-Z]/, '')
#         word_length = word.length
#         word_lengths_hash[word_length] = 0 unless word_lengths_hash.has_key?(word_length)
#         word_lengths_hash[word_length] += 1
#     end
    
#     word_lengths_hash

# end

# puts word_sizes('Four score and seven.') == { 3 => 1, 4 => 1, 5 => 1, 6 => 1 }
# puts word_sizes('Hey diddle diddle, the cat and the fiddle!') == { 3 => 5, 6 => 1, 7 => 2 }
# puts word_sizes("What's up doc?") == { 6 => 1, 2 => 1, 4 => 1 }
# puts word_sizes('') == {}

# puts word_sizes('Four score and seven.') == { 3 => 1, 4 => 1, 5 => 2 }
# puts word_sizes('Hey diddle diddle, the cat and the fiddle!') == { 3 => 5, 6 => 3 }
# puts word_sizes("What's up doc?") == { 5 => 1, 2 => 1, 3 => 1 }
# puts word_sizes('') == {}

# def alphabetic_number_sort(array)

#     nums_array = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

#     number_names = []

#     array.each do |number|
#         number_names << nums_array[number]
#     end

#     number_names.sort!

#     number_names.map! do |number| 
#         nums_array.index number 
#     end

#     p number_names
    
# end 

# puts alphabetic_number_sort((0..19).to_a) == [
#     8, 18, 11, 15, 5, 4, 14, 9, 19, 1, 7, 17,
#     6, 16, 10, 13, 3, 12, 2, 0
# ]

# def crunch(string)
#     new_string = ''
#     string.split('').each do |letter|
#         new_string += letter unless letter == new_string[-1]  
#     end
#     new_string
# end

# puts crunch('ddaaiillyy ddoouubbllee') == 'daily double'
# puts crunch('4444abcabccba') == '4abcabcba'
# puts crunch('ggggggggggggggg') == 'g'
# puts crunch('a') == 'a'
# puts crunch('') == ''

# def spin_me(str)
#     puts str.object_id
#     str.split.each do |word|
#       word.reverse!
#     end.join(" ")
# end
  
# puts spin_me("hello world").object_id # "olleh dlrow"

def digit_list(n)
    n.to_s.split('').map(&:to_i)
end

puts digit_list(12345) == [1, 2, 3, 4, 5]     # => true
puts digit_list(7) == [7]                     # => true
puts digit_list(375290) == [3, 7, 5, 2, 9, 0] # => true
puts digit_list(444) == [4, 4, 4]             # => true