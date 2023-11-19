# exercise 1

# (32 * 4) >= 129
#false

# false != !true
#false

# true == 4
# false

# false == (847 == '847')
#true

# (!true || (!(100 / 5) == 20) || ((328 / 4) == 82)) || false
#true

# exercise 2

def caps(words)
  words.upcase! if words.length >= 10
  words
end

puts(caps("hello"))
puts(caps("hello world!"))

# exercise 3

def user_count(users)
  if users >= 0 && users <= 50
    puts "between 0 and 50 users"
  elsif users >= 51 && users <= 100
    puts "between 51 and 100 users"
  elsif users >= 101
    puts "101 or more users"
  end
end

user_count(25)
user_count(75)
user_count(150)

# exercise 4

# FALSE
# Did you get it right?
# Alright now!

# exercise 5

# if statement if missing the closing end

# exercise 6

# error
# false
# false
# true
# false
# true