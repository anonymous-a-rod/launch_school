# exercise 1

arr = [1, 3, 5, 7, 9, 11]
number = 3

puts arr.include?(number)

# exercise 2

arr = ["b", "a"]
arr = arr.product(Array(1..3))
# [["b", 1], ["b", 2], ["b", 3], ["a", 1], ["a", 2], ["a", 3]]
arr.first.delete(arr.first.last)
# [["b"], ["b", 2], ["b", 3], ["a", 1], ["a", 2], ["a", 3]]

arr = ["b", "a"]
arr = arr.product([Array(1..3)])
# [["b", [1, 2, 3]], ["a", [1, 2, 3]]]
arr.first.delete(arr.first.last)
# [["b"], ["a", [1, 2, 3]]]

# exercise 3

arr = [["test", "hello", "world"],["example", "mem"]]
puts arr[1][0]

# exercise 4

arr = [15, 7, 18, 5, 12, 8, 5, 1]

puts arr.index(5)
# 3

# puts arr.index[5]
# NoMethodError: undefined method `[]'

puts arr[5]
# 8

# exercise 5

# e
# A
# nil

# exercise 6

# square brackets are used to find the value at a given index. needs to be an integer

# exercise 7

word = ''

hello = ['h', 'e', 'l', 'l', 'o']
hello.each_with_index do |value, index|
  word += value
  puts index
end

puts word

# exercise 8

arr2 = []

arr = [1, 2, 3, 4, 5]

arr.each do |x|
  arr2.push(x + 2)
end

p arr
p arr2
