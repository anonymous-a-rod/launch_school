# sun = ['visible', 'hidden'].sample

# puts "The sun is so bright!" if sun == 'visible'
# puts "The sun is so bright!" unless sun == 'visible'

# number = 7

# if number
#   puts "My favorite number is #{number}."
# else
#   puts "I don't have a favorite number."
# end

stoplight = ['green', 'yellow', 'red'].sample

case stoplight
when 'green'
    puts "Go!"
when 'yellow'
    puts "Slow down!"
when 'red'
    puts "Stop!"
end