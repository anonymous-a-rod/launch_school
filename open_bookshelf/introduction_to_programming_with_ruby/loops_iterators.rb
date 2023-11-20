# exercise 1

# [1, 2, 3, 4, 5]
# for / iterator while return back whatever was iterated over

# exercise 2

# loop do
#   puts "type something"
#   msg = gets.chomp
#   break if msg == "STOP"
# end

# exercise 3

def countdown(count)
  puts count
  countdown(count - 1) if count > 1
end

countdown(10)