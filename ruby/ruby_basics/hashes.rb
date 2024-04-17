# car = { type: 'sedan', color: 'blue', mileage: 80_000 }
# puts car

# car = {
#   type:    'sedan',
#   color:   'blue',
#   year: 2003
# }

# puts car[:color]

# numbers = {
#   high:   100,
#   medium: 50,
#   low:    10
# }
 
# # numbers.each do | key, value |
# #     puts "A #{key} number is #{value}."
# # end

# # half_numbers = []
# # numbers.map do | key, value |
# #     half_numbers << value / 2
# # end

# # p half_numbers

# low_numbers = numbers.select! do | key, value |
#     value < 25
# end


# p low_numbers
# p numbers

# vehicles = { car: { type: 'sedan', color: 'blue', year: 2003 }, truck: { type: 'pickup', color: 'red', year: 1998 }}
# p vehicles


car = [[:type, 'sedan'],[:color, 'blue'],[:year, 2003]]

p car