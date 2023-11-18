# exercise 1
puts "aaron" + " " + "venema"

# exercise 2
number = 5432

thousands_digit, thousands_remainder = number.divmod(1000)
puts thousands_digit

hundreds_digit, hundreds_remainder = thousands_remainder.divmod(100)
puts hundreds_digit

tens_digit, tens_remainder = hundreds_remainder.divmod(10)
puts tens_digit

ones_digit = tens_remainder % 10
puts ones_digit

# exercise 3
star_wars = {'Star Wars: Episode IV - A New Hope' => 1977,
             'Star Wars: Episode V - The Empire Strikes Back' => 1980,
             'Star Wars: Episode VI - Return of the Jedi' => 1983}


# exercise 4
release_dates = []

star_wars.each do |key, value|
  puts value
  release_dates.push value
end

p release_dates

# exercise 5
def factorial(number)
  result = 1
  while number >= 1 do
    result *= number
    number -= 1
  end
  result
end

[5, 6, 7, 8].each do |int|
  puts factorial(int)
end

# exercise 6
[2.12, 4.23, 7.32].each do |float|
  puts float**2
end

# exercise 7
# syntax error on line 2, it was expecting a '}' instead of the ')'
# i.e. the hash is not closing either because the closing curly brace is missing or and improper ) in the hash
